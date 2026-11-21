#!/usr/bin/env python3
"""
Валидатор runbook'а Career Intelligence / AI Profession Intelligence.

Проверяет артефакты этапов против декларации в docs/ops/assertions/.
НЕ запускает тесты продукта и НЕ оценивает качество кода — только наличие,
структуру и внутреннюю согласованность артефактов.

Запуск:
    python tools/runbook_validate.py                  # все проверки
    python tools/runbook_validate.py --stage STAGE-00 # один этап (+ его входы)
    python tools/runbook_validate.py --prereq         # только входы и зависимости
    python tools/runbook_validate.py --list           # список этапов и проверок
    python tools/runbook_validate.py --strict         # BLOCKED_HUMAN считать FAIL

Код возврата: 0 — нет FAIL, 1 — есть FAIL, 2 — ошибка запуска.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSERTIONS_DIR = ROOT / "docs" / "ops" / "assertions"

# Канонические события из 03_EVENT_CONTRACTS_SPEC.md.
CANONICAL_EVENTS = [
    "profile.created",
    "profile.updated",
    "resume.ingested",
    "occupation.matched",
    "task.identified",
    "workflow.created",
    "recommendation.generated",
    "recommendation.accepted",
    "implementation.started",
    "implementation.completed",
    "outcome.recorded",
    "tool.verified",
    "policy.blocked",
    "consent.granted",
    "consent.revoked",
    "subscription.changed",
    "partner.attributed",
]

PASS, FAIL, WAIT, SKIP = "PASS", "FAIL", "WAIT", "SKIP"


def out(text: str = "") -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    print(text)


class Ctx:
    def __init__(self, root: Path):
        self.root = root
        self.cache: dict[str, object] = {}

    def path(self, rel: str) -> Path:
        return self.root / rel

    def exists(self, rel: str) -> bool:
        return self.path(rel).exists()


# --------------------------------------------------------------------------
# Проверки. Сигнатура: fn(ctx, params: dict) -> (status, detail)
# --------------------------------------------------------------------------


def check_file_exists(ctx: Ctx, p: dict) -> tuple[str, str]:
    rel = p["path"]
    return (PASS, rel) if ctx.exists(rel) else (FAIL, f"нет файла: {rel}")


def check_dir_exists(ctx: Ctx, p: dict) -> tuple[str, str]:
    rel = p["path"]
    return (PASS, rel) if ctx.path(rel).is_dir() else (FAIL, f"нет каталога: {rel}")


def check_json_valid(ctx: Ctx, p: dict) -> tuple[str, str]:
    rel = p["path"]
    path = ctx.path(rel)
    if not path.exists():
        return FAIL, f"нет файла: {rel}"
    try:
        json.loads(path.read_text(encoding="utf-8"))
        return PASS, rel
    except Exception as exc:
        return FAIL, f"{rel}: невалидный JSON ({exc})"


def check_tsv_rows_min(ctx: Ctx, p: dict) -> tuple[str, str]:
    rel, minimum = p["path"], int(p.get("min", 1))
    path = ctx.path(rel)
    if not path.exists():
        return FAIL, f"нет файла: {rel}"
    rows = [r for r in path.read_text(encoding="utf-8").splitlines() if r.strip()]
    ok = len(rows) >= minimum
    return (PASS, f"{len(rows)} строк") if ok else (FAIL, f"{len(rows)} < {minimum} строк")


def _resolve(data, pointer: str):
    """Поддерживает pointers вида: tasks[*].customer_value, a.b.c."""
    current = [data]
    for part in pointer.split("."):
        nxt = []
        if part.endswith("[*]"):
            key = part[:-3]
            for item in current:
                if isinstance(item, dict) and isinstance(item.get(key), list):
                    nxt.extend(item[key])
        elif part == "[*]":
            for item in current:
                if isinstance(item, list):
                    nxt.extend(item)
        else:
            for item in current:
                if isinstance(item, dict) and part in item:
                    nxt.append(item[part])
        current = nxt
        if not current:
            break
    return current


def check_nonempty_field(ctx: Ctx, p: dict) -> tuple[str, str]:
    rel, pointer = p["path"], p["pointer"]
    path = ctx.path(rel)
    if not path.exists():
        return FAIL, f"нет файла: {rel}"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return FAIL, f"{rel}: невалидный JSON ({exc})"
    values = _resolve(data, pointer)
    if not values:
        return FAIL, f"{rel}: pointer '{pointer}' не найден"
    empty = [
        v
        for v in values
        if v is None
        or (isinstance(v, str) and not v.strip())
        or (isinstance(v, (list, dict)) and len(v) == 0)
    ]
    if empty:
        return FAIL, f"{rel}: {len(empty)} пустых значений по '{pointer}'"
    return PASS, f"{rel}: '{pointer}' заполнен ({len(values)})"


def check_deps_exist(ctx: Ctx, p: dict) -> tuple[str, str]:
    rel = p.get("path", "docs/tasks/MASTER_BACKLOG.json")
    path = ctx.path(rel)
    if not path.exists():
        return FAIL, f"нет файла: {rel}"
    tasks = json.loads(path.read_text(encoding="utf-8")).get("tasks", [])
    ids = {t["id"] for t in tasks}
    missing = sorted({d for t in tasks for d in t.get("depends_on", []) if d not in ids})
    if missing:
        return FAIL, f"{rel}: зависимости вне бэклога: {', '.join(missing)}"
    return PASS, f"{rel}: все зависимости существуют"


def check_deps_acyclic(ctx: Ctx, p: dict) -> tuple[str, str]:
    rel = p.get("path", "docs/tasks/MASTER_BACKLOG.json")
    path = ctx.path(rel)
    if not path.exists():
        return FAIL, f"нет файла: {rel}"
    tasks = json.loads(path.read_text(encoding="utf-8")).get("tasks", [])
    deps = {t["id"]: list(t.get("depends_on", [])) for t in tasks}
    state: dict[str, int] = {}

    def visit(node: str) -> bool:
        mark = state.get(node, 0)
        if mark == 1:
            return False
        if mark == 2:
            return True
        state[node] = 1
        for dep in deps.get(node, []):
            if dep in deps and not visit(dep):
                return False
        state[node] = 2
        return True

    cycle = next((n for n in deps if not visit(n)), None)
    if cycle:
        return FAIL, f"{rel}: цикл зависимостей, начиная с {cycle}"
    return PASS, f"{rel}: циклов нет"


def _rows(ctx: Ctx) -> list[tuple[str, int, str]]:
    """Строки SPEC_INDEX_DATA.tsv с кэшем по (mtime, size) файла.

    Кэш инвалидируется при перезаписи TSV — иначе повторный вызов в том же
    Ctx вернул бы устаревшие строки.
    """
    tsv = ctx.path("docs/specs/SPEC_INDEX_DATA.tsv")
    if not tsv.exists():
        return []
    stat = tsv.stat()
    key = ("archive_rows", stat.st_mtime_ns, stat.st_size)
    if key in ctx.cache:
        return ctx.cache[key]  # type: ignore[return-value]
    rows = []
    for line in tsv.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) == 3:
            rows.append((parts[0], int(parts[1]), parts[2]))
    ctx.cache[key] = rows
    return rows


def check_archive_hashes(ctx: Ctx, p: dict) -> tuple[str, str]:
    rows = _rows(ctx)
    if not rows:
        return FAIL, "docs/specs/SPEC_INDEX_DATA.tsv отсутствует или пуст"
    archive = ctx.path("career-intelligence-research-specs-v02")
    if not archive.is_dir():
        return FAIL, "нет каталога архива"
    actual = {f.name for f in archive.iterdir() if f.is_file()}
    listed = {name for name, _, _ in rows}
    missing = sorted(actual - listed)
    extra = sorted(listed - actual)
    stale = []
    for name, _, expected in rows:
        path = archive / name
        if path.exists():
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            if digest != expected:
                stale.append(name)
    problems = []
    if missing:
        problems.append(f"не в TSV: {', '.join(missing[:5])}")
    if extra:
        problems.append(f"лишние в TSV: {', '.join(extra[:5])}")
    if stale:
        problems.append(f"устарели хэши: {', '.join(stale[:5])}")
    if problems:
        return FAIL, "; ".join(problems)
    return PASS, f"хэши актуальны ({len(rows)} файлов)"


def check_spec_index_mentions_all(ctx: Ctx, p: dict) -> tuple[str, str]:
    rows = _rows(ctx)
    if not rows:
        return FAIL, "docs/specs/SPEC_INDEX_DATA.tsv отсутствует или пуст"
    doc = ctx.path(p.get("path", "docs/specs/SPEC_INDEX.md"))
    if not doc.exists():
        return FAIL, f"нет файла: {doc.relative_to(ctx.root)}"
    text = doc.read_text(encoding="utf-8")
    missing = sorted(name for name, _, _ in rows if name not in text)
    if missing:
        return (
            FAIL,
            f"SPEC_INDEX.md не упоминает {len(missing)} файлов: {', '.join(missing[:6])}",
        )
    return PASS, "SPEC_INDEX.md упоминает все файлы архива"


def check_terms_present(ctx: Ctx, p: dict) -> tuple[str, str]:
    rel = p["path"]
    path = ctx.path(rel)
    if not path.exists():
        return FAIL, f"нет файла: {rel}"
    text = path.read_text(encoding="utf-8")
    terms = p.get("terms", [])
    missing = [t for t in terms if t not in text]
    if missing:
        return FAIL, f"{rel}: нет терминов: {', '.join(missing[:8])}"
    return PASS, f"{rel}: все термины на месте ({len(terms)})"


def check_sections_present(ctx: Ctx, p: dict) -> tuple[str, str]:
    rel = p["path"]
    path = ctx.path(rel)
    if not path.exists():
        return FAIL, f"нет файла: {rel}"
    text = path.read_text(encoding="utf-8")
    missing = [s for s in p.get("headings", []) if s not in text]
    if missing:
        return FAIL, f"{rel}: нет разделов: {', '.join(missing)}"
    return PASS, f"{rel}: все разделы на месте"


def check_canonical_events(ctx: Ctx, p: dict) -> tuple[str, str]:
    rel = p["path"]
    path = ctx.path(rel)
    if not path.exists():
        return FAIL, f"нет файла: {rel}"
    text = path.read_text(encoding="utf-8")
    missing = [e for e in CANONICAL_EVENTS if e not in text]
    if missing:
        return FAIL, f"{rel}: нет канонических событий: {', '.join(missing)}"
    return PASS, f"{rel}: все {len(CANONICAL_EVENTS)} событий"


def check_human_signed(ctx: Ctx, p: dict) -> tuple[str, str]:
    rel = p["path"]
    path = ctx.path(rel)
    if not path.exists():
        return FAIL, f"нет файла: {rel}"
    text = path.read_text(encoding="utf-8")
    if not re.search(r"(?mi)^signed_by:\s*\S+", text):
        return WAIT, f"{rel}: нет подписи человека (signed_by)"
    who = re.search(r"(?mi)^signed_by:\s*(\S+)", text).group(1)  # type: ignore[union-attr]
    when = re.search(r"(?mi)^signed_at:\s*(\S+)", text)
    return PASS, f"{rel}: подписано {who}" + (f" {when.group(1)}" if when else "")


def check_gate_status(ctx: Ctx, p: dict) -> tuple[str, str]:
    rel = p["path"]
    path = ctx.path(rel)
    if not path.exists():
        return FAIL, f"нет файла: {rel}"
    match = re.search(
        r"(?m)^(?:P0_STATUS|STATUS):\s*(PASS|CONDITIONAL_PASS|FAIL)\s*$",
        path.read_text(encoding="utf-8"),
    )
    if not match:
        return FAIL, f"{rel}: нет строки STATUS (ожидалось «STATUS: PASS»)"
    verdict = match.group(1)
    if verdict == "PASS":
        return PASS, f"{rel}: {verdict}"
    if verdict == "CONDITIONAL_PASS":
        return WAIT, f"{rel}: CONDITIONAL_PASS требует решения человека"
    return FAIL, f"{rel}: FAIL"


def check_manual(ctx: Ctx, p: dict) -> tuple[str, str]:
    """Честно помечает то, что нельзя проверить механически."""
    return SKIP, p.get("note", "требует человека")


def _stage_rows(ctx: Ctx) -> list[dict]:
    """Реестр этапов из STAGE-INDEX.csv. Кэш по (mtime, size)."""
    path = ctx.path("docs/ops/STAGE-INDEX.csv")
    if not path.exists():
        return []
    stat = path.stat()
    key = ("stage_rows", stat.st_mtime_ns, stat.st_size)
    if key in ctx.cache:
        return ctx.cache[key]  # type: ignore[return-value]
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()]
    if not lines:
        return []
    header = [h.strip() for h in lines[0].split(",")]
    rows = []
    for line in lines[1:]:
        parts = [p.strip() for p in line.split(",")]
        if len(parts) == len(header):
            rows.append(dict(zip(header, parts, strict=False)))
    ctx.cache[key] = rows
    return rows


def check_stage_registry_consistent(ctx: Ctx, p: dict) -> tuple[str, str]:
    """Каждый этап реестра имеет карточку с обязательными разделами.

    Ловит дрейф при добавлении этапа: запись в реестре без карточки,
    карточка без записи, карточка без обязательных разделов.
    """
    rows = _stage_rows(ctx)
    if not rows:
        return FAIL, "docs/ops/STAGE-INDEX.csv отсутствует или пуст"
    stages_dir = ctx.path("docs/ops/stages")
    if not stages_dir.is_dir():
        return FAIL, "нет каталога docs/ops/stages"

    required = [
        "## Trigger",
        "## Inputs",
        "## Outputs",
        "## Definition of Done",
        "## HARD STOP",
        "## Rollback",
        "## Промпт для IDE",
    ]
    card_files = {f.name: f for f in stages_dir.glob("*.md")}
    problems = []
    seen = set()

    for row in rows:
        sid = row.get("stage_id", "")
        if not sid or sid == "stage_id":
            continue
        matches = [name for name in card_files if name.startswith(f"{sid}-")]
        if not matches:
            problems.append(f"нет карточки для {sid}")
            continue
        for name in matches:
            seen.add(name)
            text = card_files[name].read_text(encoding="utf-8")
            missing = [h for h in required if h not in text]
            if missing:
                problems.append(f"{name}: нет разделов {', '.join(missing)}")

    orphans = sorted(set(card_files) - seen)
    if orphans:
        problems.append(f"карточки вне реестра: {', '.join(orphans[:4])}")

    if problems:
        return FAIL, "; ".join(problems[:6])
    return PASS, f"{len(rows)} этапов, карточки и разделы на месте"


def check_skills_cover_stages(ctx: Ctx, p: dict) -> tuple[str, str]:
    """Каждый этап имеет скилл, и frontmatter `name` совпадает с именем папки."""
    rows = _stage_rows(ctx)
    if not rows:
        return FAIL, "docs/ops/STAGE-INDEX.csv отсутствует или пуст"
    skills_dir = ctx.path("skills")
    if not skills_dir.is_dir():
        return FAIL, "нет каталога skills"

    skill_dirs = [d for d in skills_dir.iterdir() if d.is_dir()]
    problems = []
    for row in rows:
        sid = row.get("stage_id", "")
        if not sid or sid == "stage_id":
            continue
        matches = [d for d in skill_dirs if d.name.startswith(f"ci-{sid.lower()}-")]
        if not matches:
            problems.append(f"нет скилла для {sid}")

    for d in skill_dirs:
        skill_md = d / "SKILL.md"
        if not skill_md.exists():
            problems.append(f"{d.name}: нет SKILL.md")
            continue
        head = skill_md.read_text(encoding="utf-8")[:400]
        if f"name: {d.name}" not in head:
            problems.append(f"{d.name}: frontmatter name не совпадает с папкой")

    if problems:
        return FAIL, "; ".join(problems[:6])
    return PASS, f"{len(rows)} этапов, {len(skill_dirs)} скиллов согласованы"


def check_assertions_cover_stages(ctx: Ctx, p: dict) -> tuple[str, str]:
    """Каждый этап реестра имеет декларацию проверок с совпадающим полем stage."""
    rows = _stage_rows(ctx)
    if not rows:
        return FAIL, "docs/ops/STAGE-INDEX.csv отсутствует или пуст"
    assertions = ctx.path("docs/ops/assertions")
    if not assertions.is_dir():
        return FAIL, "нет каталога docs/ops/assertions"

    problems = []
    declared = {}
    for path in assertions.glob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            problems.append(f"{path.name}: невалидный JSON ({exc})")
            continue
        stage = data.get("stage")
        if stage:
            declared[stage] = path.name

    for row in rows:
        sid = row.get("stage_id", "")
        if not sid or sid == "stage_id":
            continue
        if sid not in declared:
            problems.append(f"нет декларации для {sid}")

    if problems:
        return FAIL, "; ".join(problems[:6])
    return PASS, f"{len(declared)} деклараций покрывают реестр"


def check_markdown_links_resolve(ctx: Ctx, p: dict) -> tuple[str, str]:
    """Относительные ссылки в markdown должны указывать на существующие файлы.

    Проверяются только документы проекта (по умолчанию), не архив: архив —
    read-only источник и его внутренние ссылки не наша ответственность.
    """
    paths = p.get("paths") or [
        "README.md",
        "README.ru.md",
        "CONTRIBUTING.md",
        "AGENTS.md",
        "CHANGELOG.md",
        "SECURITY.md",
        "CODE_OF_CONDUCT.md",
        "docs",
    ]
    # Один уровень вложенности — чтобы ловить бейджи вида [![alt](img)](target).
    link_re = re.compile(r"\[(?:[^\[\]]|\[[^\]]*\])*\]\(([^)]+)\)")
    problems = []
    checked = 0

    files: list[Path] = []
    for rel in paths:
        candidate = ctx.path(rel)
        if candidate.is_dir():
            files.extend(sorted(candidate.rglob("*.md")))
        elif candidate.exists():
            files.append(candidate)

    # Ссылки внутри кода — не ссылки: вырезаем блоки и inline-код до разбора.
    fenced = re.compile(r"```.*?```", re.S)
    inline_code = re.compile(r"`[^`\n]*`")

    for path in files:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        text = fenced.sub("", text)
        text = inline_code.sub("", text)
        for raw in link_re.findall(text):
            target = raw.strip().split(" ")[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            checked += 1
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                rel_file = path.relative_to(ctx.root).as_posix()
                problems.append(f"{rel_file} → {raw}")

    if problems:
        head = "; ".join(problems[:5])
        more = f" (и ещё {len(problems) - 5})" if len(problems) > 5 else ""
        return FAIL, f"битые ссылки: {head}{more}"
    return PASS, f"проверено ссылок: {checked}"


def check_min_occurrences(ctx: Ctx, p: dict) -> tuple[str, str]:
    """Шаблон должен встречаться в файле не меньше N раз.

    Нужен для содержательных проверок: «в реестре рисков не меньше 16 строк»,
    «в карте контекстов — все 13 контекстов» и т. п.
    """
    rel, pattern, minimum = p["path"], p["pattern"], int(p.get("min", 1))
    path = ctx.path(rel)
    if not path.exists():
        return FAIL, f"нет файла: {rel}"
    try:
        regex = re.compile(pattern, re.M)
    except re.error as exc:
        return FAIL, f"{rel}: некорректный шаблон ({exc})"
    found = len(regex.findall(path.read_text(encoding="utf-8")))
    if found < minimum:
        return FAIL, f"{rel}: найдено {found}, ожидалось не меньше {minimum}"
    return PASS, f"{rel}: {found} совпадений (мин. {minimum})"


def check_frontmatter_equals(ctx: Ctx, p: dict) -> tuple[str, str]:
    """Поле в YAML-frontmatter должно иметь ожидаемое значение."""
    rel, field, expected = p["path"], p["field"], p["equals"]
    path = ctx.path(rel)
    if not path.exists():
        return FAIL, f"нет файла: {rel}"
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return FAIL, f"{rel}: нет frontmatter"
    head = text.split("---", 2)[1] if text.count("---") >= 2 else ""
    match = re.search(rf"(?m)^{re.escape(field)}:\s*(.+?)\s*$", head)
    if not match:
        return FAIL, f"{rel}: нет поля {field}"
    value = match.group(1).strip().strip('"').strip("'")
    if value != expected:
        return FAIL, f"{rel}: {field}={value}, ожидалось {expected}"
    return PASS, f"{rel}: {field}={value}"


def check_next_task_single(ctx: Ctx, p: dict) -> tuple[str, str]:
    rel = p.get("path", "docs/tasks/NEXT_TASK.md")
    path = ctx.path(rel)
    if not path.exists():
        return FAIL, f"нет файла: {rel}"
    ids = set(re.findall(r"TASK-[A-Z0-9]+-\d+", path.read_text(encoding="utf-8")))
    if len(ids) == 1:
        return PASS, f"{rel}: ровно одна задача ({next(iter(ids))})"
    return FAIL, f"{rel}: задач найдено {len(ids)}, ожидалась одна"


CHECKS = {
    "file_exists": check_file_exists,
    "dir_exists": check_dir_exists,
    "json_valid": check_json_valid,
    "tsv_rows_min": check_tsv_rows_min,
    "nonempty_field": check_nonempty_field,
    "deps_exist": check_deps_exist,
    "deps_acyclic": check_deps_acyclic,
    "archive_hashes": check_archive_hashes,
    "spec_index_mentions_all": check_spec_index_mentions_all,
    "terms_present": check_terms_present,
    "sections_present": check_sections_present,
    "canonical_events": check_canonical_events,
    "human_signed": check_human_signed,
    "gate_status": check_gate_status,
    "next_task_single": check_next_task_single,
    "stage_registry_consistent": check_stage_registry_consistent,
    "skills_cover_stages": check_skills_cover_stages,
    "assertions_cover_stages": check_assertions_cover_stages,
    "markdown_links_resolve": check_markdown_links_resolve,
    "min_occurrences": check_min_occurrences,
    "frontmatter_equals": check_frontmatter_equals,
    "manual": check_manual,
}


# --------------------------------------------------------------------------
# Загрузка деклараций
# --------------------------------------------------------------------------


def load_assertions() -> list[dict]:
    if not ASSERTIONS_DIR.is_dir():
        return []
    loaded = []
    for path in sorted(ASSERTIONS_DIR.glob("*.json")):
        try:
            loaded.append(json.loads(path.read_text(encoding="utf-8")))
        except Exception as exc:
            out(f"[FAIL] {path.name}: невалидный JSON ({exc})")
    return loaded


def stage_outputs(stage: dict) -> list[str]:
    outputs = stage.get("outputs", [])
    return [o["path"] if isinstance(o, dict) else o for o in outputs]


def transitive_deps(all_stages: list[dict], stage_id: str) -> list[str]:
    by_id = {s.get("stage"): s for s in all_stages if s.get("stage")}
    seen: list[str] = []
    stack = list(by_id.get(stage_id, {}).get("depends_on", []))
    while stack:
        dep = stack.pop()
        if dep in seen or dep not in by_id:
            continue
        seen.append(dep)
        stack.extend(by_id[dep].get("depends_on", []))
    return sorted(seen)


# --------------------------------------------------------------------------
# Режимы
# --------------------------------------------------------------------------


def cmd_list(all_stages: list[dict]) -> int:
    out("Этапы и число проверок:")
    for stage in all_stages:
        sid = stage.get("stage", "?")
        deps = ",".join(stage.get("depends_on", [])) or "-"
        out(
            f"  {sid:<12} deps={deps:<28} checks={len(stage.get('checks', []))} outputs={len(stage.get('outputs', []))}"
        )
    out(f"\nВсего этапов: {len(all_stages)}")
    out("Виды проверок: " + ", ".join(sorted(CHECKS)))
    return 0


def cmd_validate(all_stages: list[dict], only_stage: str | None, prereq: bool, strict: bool) -> int:
    ctx = Ctx(ROOT)
    results: list[tuple[str, str, str, str]] = []

    for stage in all_stages:
        sid = stage.get("stage", "?")
        if only_stage and sid != only_stage:
            continue

        if prereq:
            for rel in stage.get("inputs", []):
                results.append((sid, "input", *check_file_exists(ctx, {"path": rel})))
            if only_stage:
                for dep in transitive_deps(all_stages, sid):
                    dep_stage = next(s for s in all_stages if s.get("stage") == dep)
                    for rel in stage_outputs(dep_stage):
                        results.append((sid, f"dep:{dep}", *check_file_exists(ctx, {"path": rel})))
            continue

        for rel in stage.get("inputs", []):
            results.append((sid, "input", *check_file_exists(ctx, {"path": rel})))
        for rel in stage_outputs(stage):
            results.append((sid, "output", *check_file_exists(ctx, {"path": rel})))
        for item in stage.get("checks", []):
            kind = item.get("kind")
            fn = CHECKS.get(kind)
            if fn is None:
                results.append((sid, kind or "?", SKIP, "неизвестный вид проверки"))
                continue
            results.append((sid, kind, *fn(ctx, item)))

    marker = {PASS: "[PASS]", FAIL: "[FAIL]", WAIT: "[WAIT]", SKIP: "[SKIP]"}
    current = None
    for sid, kind, status, detail in results:
        if sid != current:
            out(f"\n{sid}")
            current = sid
        shown = FAIL if (strict and status == WAIT) else status
        out(f"  {marker[shown]:<7} {kind:<24} {detail}")

    fails = sum(1 for _, _, s, _ in results if s == FAIL)
    waits = sum(1 for _, _, s, _ in results if s == WAIT)
    passes = sum(1 for _, _, s, _ in results if s == PASS)
    out(f"\nИтого: PASS={passes} FAIL={fails} WAIT={waits}")
    if waits:
        out("WAIT — требуется решение или подпись человека. Не считается FAIL, но этап не закрыт.")
    return 1 if fails else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Валидатор runbook'а")
    parser.add_argument("--stage", help="проверить только этот этап, например STAGE-00")
    parser.add_argument("--prereq", action="store_true", help="только входы и зависимости")
    parser.add_argument("--list", action="store_true", help="список этапов и проверок")
    parser.add_argument("--strict", action="store_true", help="WAIT считать FAIL")
    args = parser.parse_args()

    all_stages = load_assertions()
    if not all_stages:
        out(f"[FAIL] нет файлов деклараций в {ASSERTIONS_DIR}")
        return 2
    if args.list:
        return cmd_list(all_stages)
    if args.stage and not any(s.get("stage") == args.stage for s in all_stages):
        out(f"[FAIL] неизвестный этап: {args.stage}")
        return 2
    return cmd_validate(all_stages, args.stage, args.prereq, args.strict)


if __name__ == "__main__":
    raise SystemExit(main())

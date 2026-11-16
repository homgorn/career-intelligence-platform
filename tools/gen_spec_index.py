#!/usr/bin/env python3
"""
Регенерация индекса спецификаций архива.

Пишет два файла:
  docs/specs/SPEC_INDEX_DATA.tsv — имя, размер, sha256 (machine-readable, без заголовка);
  docs/specs/SPEC_INDEX.md       — кураторская часть + сгенерированная таблица
                                   между маркерами GENERATED:BEGIN/END.

Кураторские статусы лежат в docs/specs/SPEC_STATUS.json и правятся человеком.
Всё остальное вычисляется из архива, поэтому индекс невозможно разойтись
с диском молча.

Запуск:
    python tools/gen_spec_index.py
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARCHIVE = ROOT / "career-intelligence-research-specs-v02"
STATUS_FILE = ROOT / "docs" / "specs" / "SPEC_STATUS.json"
INDEX_FILE = ROOT / "docs" / "specs" / "SPEC_INDEX.md"
TSV_FILE = ROOT / "docs" / "specs" / "SPEC_INDEX_DATA.tsv"

BEGIN = "<!-- GENERATED:BEGIN -->"
END = "<!-- GENERATED:END -->"


def out(text: str = "") -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    print(text)


def main() -> int:
    if not ARCHIVE.is_dir():
        out(f"[FAIL] нет каталога архива: {ARCHIVE}")
        return 1

    status_map = json.loads(STATUS_FILE.read_text(encoding="utf-8")).get("files", {})

    rows = []
    table = []
    counts: dict[str, int] = {}
    rel_counts: dict[str, int] = {}

    for path in sorted(p for p in ARCHIVE.iterdir() if p.is_file()):
        meta = status_map.get(path.name, {})
        status = meta.get("status", "reference")
        relevance = meta.get("relevance", "low")
        note = meta.get("note", "").replace("|", "/").replace("\n", " ")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        size = path.stat().st_size

        rows.append(f"{path.name}\t{size}\t{digest}")
        table.append(f"| `{path.name}` | {status} | {relevance} | `{digest[:12]}` | {note} |")
        counts[status] = counts.get(status, 0) + 1
        rel_counts[relevance] = rel_counts.get(relevance, 0) + 1

    # newline="\n" — вывод не должен зависеть от ОС, иначе CI на Linux
    # будет видеть дифф из-за CRLF на Windows.
    TSV_FILE.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")

    generated = [
        "## Полный индекс",
        "",
        f"Всего файлов: **{len(rows)}**. Полные sha256 — в `SPEC_INDEX_DATA.tsv`.",
        "",
        "| Файл | Статус | P0 | sha256 (12) | Примечание |",
        "| --- | --- | --- | --- | --- |",
        *table,
        "",
    ]

    narrative = INDEX_FILE.read_text(encoding="utf-8") if INDEX_FILE.exists() else ""
    if BEGIN in narrative and END in narrative:
        head = narrative.split(BEGIN)[0]
        tail = narrative.split(END)[1]
        updated = head + BEGIN + "\n" + "\n".join(generated) + END + tail
    elif narrative:
        updated = narrative.rstrip() + "\n\n" + BEGIN + "\n" + "\n".join(generated) + END + "\n"
    else:
        updated = BEGIN + "\n" + "\n".join(generated) + END + "\n"

    INDEX_FILE.write_text(updated, encoding="utf-8", newline="\n")

    out(f"Файлов: {len(rows)}")
    out("Статусы: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    out("P0-релевантность: " + ", ".join(f"{k}={v}" for k, v in sorted(rel_counts.items())))
    out(f"Записано: {TSV_FILE}, {INDEX_FILE}")
    unmapped = sorted(p.name for p in ARCHIVE.iterdir() if p.is_file() and p.name not in status_map)
    if unmapped:
        out(f"[WARN] без кураторской записи ({len(unmapped)}): {', '.join(unmapped)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

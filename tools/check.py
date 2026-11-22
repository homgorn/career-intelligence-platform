#!/usr/bin/env python3
"""
Однокомандная локальная проверка проекта — замена GitHub Actions на время
блокировки биллинга и единый источник истины о том, что значит «зелёный».

Запуск:
    python tools/check.py              # все проверки
    python tools/check.py --quick      # без перегенерации индекса и STAGE-00
    python tools/check.py --skip-info  # без информационного блока о будущих этапах
    python tools/check.py --json

Код возврата: 0 — все проверки пройдены, 1 — есть падения, 2 — ошибка запуска.
Никаких новых зависимостей: только stdlib + ruff/pytest из окружения.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Этапы, чьи артефакты ещё не созданы. Их провал ожидаем и не считается
# поломкой — он только показывает, что работа не начиналась.
INFO_STAGES = ("STAGE-00A", "STAGE-02", "STAGE-04", "STAGE-05", "STAGE-12")


@dataclass(frozen=True)
class Step:
    """Одна проверка. `allow_exit` перечисляет коды, которые не считаются падением."""

    name: str
    cmd: list[str]
    allow_exit: tuple[int, ...] = (0,)
    quick: bool = False


def run(step: Step, cwd: Path | None = None, timeout: int = 600) -> tuple[str, int, str]:
    """Выполнить шаг и вернуть (имя, код выхода, хвост вывода).

    Недоступная команда и таймаут возвращают синтетические коды 127 и 124,
    чтобы вызывающий код не отличал их от обычных падений.
    """
    try:
        proc = subprocess.run(
            step.cmd,
            cwd=cwd or ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
        )
    except FileNotFoundError:
        return step.name, 127, f"команда не найдена: {step.cmd[0]}"
    except subprocess.TimeoutExpired:
        return step.name, 124, "таймаут"
    except OSError as exc:
        return step.name, 126, f"не удалось запустить: {exc}"
    out = (proc.stdout + proc.stderr).strip()
    return step.name, proc.returncode, out


def build_steps(py: str) -> list[Step]:
    """Полный набор проверок. Порядок: сначала дешёвые, потом медленные."""
    return [
        Step(
            "json: бэклог",
            [
                py,
                "-c",
                "import json; json.load(open('docs/tasks/MASTER_BACKLOG.json', encoding='utf-8'))",
            ],
        ),
        Step(
            "json: SPEC_STATUS",
            [
                py,
                "-c",
                "import json; json.load(open('docs/specs/SPEC_STATUS.json', encoding='utf-8'))",
            ],
        ),
        Step(
            "csv: STAGE-INDEX",
            [py, "-c", "open('docs/ops/STAGE-INDEX.csv', encoding='utf-8').read()"],
        ),
        Step("ruff check", [py, "-m", "ruff", "check", "tools", "--output-format", "concise"]),
        Step("ruff format --check", [py, "-m", "ruff", "format", "--check", "tools"]),
        Step("pytest", [py, "-m", "pytest", "tools/tests", "-q"]),
        Step("gen_spec_index (перегенерация индекса)", [py, "tools/gen_spec_index.py"], quick=True),
        Step(
            "git diff (индекс соответствует архиву)",
            ["git", "diff", "--exit-code", "--", "docs/specs"],
            quick=True,
        ),
        Step("validator ALWAYS", [py, "tools/runbook_validate.py", "--stage", "ALWAYS"]),
        Step(
            "validator STAGE-00",
            [py, "tools/runbook_validate.py", "--stage", "STAGE-00"],
            quick=True,
        ),
        # Селектор либо блокирован до подписи пилота (2), либо ведёт на задачу,
        # которая сама создаёт пилот (0). Оба исхода валидны.
        Step("selector даёт валидный исход", [py, "tools/runbook_next.py"], allow_exit=(0, 2)),
    ]


def run_all(steps: list[Step], quick: bool = False, cwd: Path | None = None) -> list[dict]:
    results = []
    for step in steps:
        if quick and step.quick:
            results.append({"name": step.name, "status": "SKIP", "detail": ""})
            continue
        name, code, out = run(step, cwd=cwd)
        ok = code in step.allow_exit
        results.append(
            {
                "name": name,
                "status": "PASS" if ok else "FAIL",
                "exit": code,
                "detail": out[-800:],
            }
        )
    return results


def collect_info(py: str, cwd: Path | None = None) -> list[dict]:
    info = []
    for stage in INFO_STAGES:
        name, code, _ = run(
            Step(f"stage {stage}", [py, "tools/runbook_validate.py", "--stage", stage]),
            cwd=cwd,
        )
        info.append({"stage": stage, "exit": code, "status": "PASS" if code == 0 else "FAIL"})
    return info


def render_text(results: list[dict], info: list[dict]) -> str:
    lines = ["=== Career Intelligence — локальные проверки ===", ""]
    for r in results:
        mark = {"PASS": "[PASS]", "FAIL": "[FAIL]", "SKIP": "[SKIP]"}[r["status"]]
        lines.append(f"{mark} {r['name']}")
        if r["status"] == "FAIL":
            lines.append("       " + r["detail"].replace("\n", "\n       ")[:600])
    if info:
        lines.append("")
        lines.append("=== Информационно (ожидаются FAIL до выполнения этапов) ===")
        for i in info:
            lines.append(f"[{i['status']:>4}] {i['stage']} (exit {i['exit']})")
    fails = [r for r in results if r["status"] == "FAIL"]
    lines.append("")
    lines.append("Итого: " + ("всё зелёное" if not fails else f"{len(fails)} шаг(ов) упало"))
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Локальные проверки проекта")
    parser.add_argument("--quick", action="store_true", help="пропустить медленные шаги")
    parser.add_argument("--skip-info", action="store_true", help="не проверять будущие этапы")
    parser.add_argument("--json", action="store_true", help="вывод в JSON")
    args = parser.parse_args(argv)

    py = sys.executable
    results = run_all(build_steps(py), quick=args.quick)
    info = [] if args.skip_info else collect_info(py)
    fails = [r for r in results if r["status"] == "FAIL"]

    if args.json:
        print(
            json.dumps(
                {"results": results, "info": info, "passed": not fails},
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(render_text(results, info))
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())

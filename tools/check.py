#!/usr/bin/env python3
"""
Однокомандная локальная проверка проекта — замена GitHub Actions на время
блокировки биллинга.

Запуск:
    python tools/check.py            # все проверки
    python tools/check.py --quick    # без перегенерации индекса и без stage gates
    python tools/check.py --json

Код возврата: 0 — все проверки пройдены, 1 — есть падения.
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


@dataclass
class Step:
    name: str
    cmd: list[str]
    allow_exit: tuple[int, ...] = (0,)
    quick: bool = False


def run(step: Step) -> tuple[str, int, str]:
    try:
        proc = subprocess.run(
            step.cmd,
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=600,
        )
    except FileNotFoundError:
        return step.name, 127, f"команда не найдена: {step.cmd[0]}"
    except subprocess.TimeoutExpired:
        return step.name, 124, "таймаут"
    out = (proc.stdout + proc.stderr).strip()
    return step.name, proc.returncode, out


def main() -> int:
    parser = argparse.ArgumentParser(description="Локальные проверки проекта")
    parser.add_argument("--quick", action="store_true", help="пропустить медленные шаги")
    parser.add_argument("--json", action="store_true", help="вывод в JSON")
    args = parser.parse_args()

    py = sys.executable
    steps = [
        Step(
            "json: бэклог",
            [
                py,
                "-c",
                "import json,sys; json.load(open('docs/tasks/MASTER_BACKLOG.json', encoding='utf-8'))",
            ],
        ),
        Step(
            "json: SPEC_STATUS",
            [
                py,
                "-c",
                "import json,sys; json.load(open('docs/specs/SPEC_STATUS.json', encoding='utf-8'))",
            ],
        ),
        Step(
            "csv: STAGE-INDEX",
            [py, "-c", "open('docs/ops/STAGE-INDEX.csv', encoding='utf-8').read()"],
        ),
        Step("ruff check", [py, "-m", "ruff", "check", "tools", "--output-format", "concise"]),
        Step("ruff format --check", [py, "-m", "ruff", "format", "--check", "tools"]),
        Step("pytest", [py, "-m", "pytest", "tools/tests", "-q"]),
        Step(
            "gen_spec_index (автономная перегенерация)", [py, "tools/gen_spec_index.py"], quick=True
        ),
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
        Step("selector is blocked by design", [py, "tools/runbook_next.py"], allow_exit=(2,)),
    ]

    # Этапы, которые сегодня заведомо FAIL (артефакты ещё не созданы), включены
    # только как информационные — их неноль не роняет локальную проверку.
    results = []
    for step in steps:
        if args.quick and step.quick:
            results.append({"name": step.name, "status": "SKIP", "detail": ""})
            continue
        name, code, out = run(step)
        ok = code in step.allow_exit
        results.append(
            {
                "name": name,
                "status": "PASS" if ok else "FAIL",
                "exit": code,
                "detail": out[-800:],
            }
        )

    # Информационные этапы (артефакты ещё не существуют).
    info_stages = ["STAGE-00A", "STAGE-02", "STAGE-04", "STAGE-05", "STAGE-12"]
    info = []
    for stage in info_stages:
        name, code, out = run(
            Step(f"stage {stage}", [py, "tools/runbook_validate.py", "--stage", stage])
        )
        info.append({"stage": stage, "exit": code, "status": "PASS" if code == 0 else "FAIL"})

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
        print("=== Career Intelligence — локальные проверки ===\n")
        for r in results:
            mark = {"PASS": "[PASS]", "FAIL": "[FAIL]", "SKIP": "[SKIP]"}[r["status"]]
            print(f"{mark} {r['name']}")
            if r["status"] == "FAIL":
                print("       " + r["detail"].replace("\n", "\n       ")[:600])
        print("\n=== Информационно (ожидаются FAIL до выполнения этапов) ===")
        for i in info:
            print(f"[{i['status']:>4}] {i['stage']} (exit {i['exit']})")
        print("\nИтого: " + ("всё зелёное" if not fails else f"{len(fails)} шаг(ов) упало"))
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())

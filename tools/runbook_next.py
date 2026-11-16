#!/usr/bin/env python3
"""
Механический селектор следующей задачи (аналог STAGE-13).

Реализует правила выбора из runbook'а и ничего не выдумывает:
  1. не выбирать задачу потому, что она интересная;
  2. сначала dependencies;
  3. затем P0 blockers;
  4. затем customer value;
  5. затем architecture risk;
  6. затем implementation cost;
  7. P1 запрещён, пока P0 gate не разрешил переход;
  8. P2 запрещён до P1 gate.

Запуск:
    python tools/runbook_next.py            # текст
    python tools/runbook_next.py --json     # машиночитаемый вывод

Код возврата: 0 — задача выбрана, 2 — заблокировано, 1 — ошибка.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BACKLOG = ROOT / "docs" / "tasks" / "MASTER_BACKLOG.json"
PILOT = ROOT / "docs" / "architecture" / "PILOT_DECISION.md"

PRIORITY_RANK = {"P0": 0, "P1": 1, "P2": 2}


def out(text: str = "") -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    print(text)


def gate_status(path: Path) -> str | None:
    """Вердикт gate'а. Завершённая строка «STATUS: X»; шаблонный placeholder игнорируется."""
    if not path.exists():
        return None
    match = re.search(
        r"(?m)^(?:P0_STATUS|STATUS):\s*(PASS|CONDITIONAL_PASS|FAIL)\s*$",
        path.read_text(encoding="utf-8"),
    )
    return match.group(1) if match else None


def load_backlog() -> dict:
    return json.loads(BACKLOG.read_text(encoding="utf-8"))


def pilot_signed() -> tuple[bool, str]:
    if not PILOT.exists():
        return False, "нет docs/architecture/PILOT_DECISION.md"
    text = PILOT.read_text(encoding="utf-8")
    who = re.search(r"(?mi)^signed_by:\s*(\S+)", text)
    if not who:
        return False, f"{PILOT.relative_to(ROOT)} не подписан (signed_by)"
    when = re.search(r"(?mi)^signed_at:\s*(\S+)", text)
    return True, f"{who.group(1)}" + (f" {when.group(1)}" if when else "")


def main() -> int:
    parser = argparse.ArgumentParser(description="Селектор следующей задачи")
    parser.add_argument("--json", action="store_true", help="машиночитаемый вывод")
    args = parser.parse_args()

    if not BACKLOG.exists():
        out(f"[ERROR] нет бэклога: {BACKLOG}")
        return 1

    backlog = load_backlog()
    tasks = backlog.get("tasks", [])
    by_id = {t["id"]: t for t in tasks}

    signed, detail = pilot_signed()
    gates = {
        "P0": gate_status(ROOT / "docs" / "gates" / "RELEASE-GATE-P0.md"),
        "P1": gate_status(ROOT / "docs" / "gates" / "RELEASE-GATE-P1.md"),
        "P2": gate_status(ROOT / "docs" / "gates" / "RELEASE-GATE-P2.md"),
    }

    allowed = ["P0"]
    if gates["P0"] == "PASS":
        allowed.append("P1")
    if gates["P1"] == "PASS":
        allowed.append("P2")

    blocked_reason = None
    if not signed:
        blocked_reason = ("BLOCKED_ON_PILOT", detail)

    eligible = []
    reasons: dict[str, str] = {}
    if not blocked_reason:
        for task in tasks:
            tid = task["id"]
            if task.get("status") not in ("PENDING", None, ""):
                reasons[tid] = f"статус {task.get('status')}"
                continue
            if task.get("priority") not in allowed:
                reasons[tid] = f"priority {task.get('priority')} закрыт gate'ом"
                continue
            unfinished = [
                d for d in task.get("depends_on", []) if by_id.get(d, {}).get("status") != "DONE"
            ]
            if unfinished:
                reasons[tid] = f"не завершены зависимости: {', '.join(unfinished)}"
                continue
            value = float(task.get("value_score") or 0)
            risk = float(task.get("risk_score") or 0)
            cost = float(task.get("cost_score") or 0)
            score = value - risk - cost
            needs_priority = value == 0 and risk == 0 and cost == 0
            eligible.append((score, tid, needs_priority))

    eligible.sort(
        key=lambda item: (
            -item[0],
            PRIORITY_RANK.get(by_id[item[1]].get("priority"), 9),
            item[1],
        )
    )

    result = {
        "pilot_signed": signed,
        "pilot_detail": detail,
        "gates": gates,
        "allowed_priorities": allowed,
        "eligible_count": len(eligible),
        "selected": None,
        "blocked_reason": blocked_reason,
        "reasons": reasons,
    }

    if blocked_reason:
        result["selected"] = None
    elif eligible:
        score, tid, needs_priority = eligible[0]
        result["selected"] = {
            "task_id": tid,
            "score": score,
            "needs_human_priority": needs_priority,
            **{k: by_id[tid].get(k) for k in ("title", "priority", "depends_on", "stage")},
        }
    else:
        result["blocked_reason"] = (
            "NO_ELIGIBLE_TASK",
            "нет задач в статусе PENDING с закрытыми зависимостями",
        )

    if args.json:
        out(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        out("=== Селектор следующей задачи ===")
        out(f"Пилот подписан: {'да' if signed else 'НЕТ'} ({detail})")
        out(f"Gate: P0={gates['P0']} P1={gates['P1']} P2={gates['P2']}")
        out(f"Разрешённые приоритеты: {', '.join(allowed)}")
        out("")
        if blocked_reason:
            out(f"[BLOCKED] {blocked_reason[0]}: {blocked_reason[1]}")
            out("")
            out("Причины по отклонённым задачам:")
            for tid, why in sorted(reasons.items()):
                out(f"  {tid}: {why}")
            return 2
        if result["selected"]:
            sel = result["selected"]
            out(f"TASK: {sel['task_id']} — {sel['title']}")
            out(f"  priority: {sel['priority']}  stage: {sel['stage']}")
            out(f"  depends_on: {', '.join(sel['depends_on']) or 'нет'}")
            out(f"  score (value-risk-cost): {sel['score']}")
            if sel["needs_human_priority"]:
                out("  [!] value/risk/cost не оценены — приоритет требует человека")
            out("")
            out("WHY NOW: единственная задача с закрытыми зависимостями и разрешённым")
            out("приоритетом; правила 1–8 применены механически.")
        else:
            out("[BLOCKED] нет подходящей задачи")
            out("")
            out("Причины по отклонённым задачам:")
            for tid, why in sorted(reasons.items()):
                out(f"  {tid}: {why}")
            out("")
            out(f"Кандидатов: {len(eligible)}")
    return 0 if result["selected"] else 2


if __name__ == "__main__":
    raise SystemExit(main())

---
name: ci-stage-13-next-task
description: "Career Intelligence / AI Profession Intelligence, этап STAGE-13 — Next task selector. Постоянный: используется после каждой выполненной задачи. Механически выбирает ровно одну следующую задачу по правилам 1–8 (dependencies → P0 blockers → customer value → architecture risk → cost; P1 только после P0 gate, P2 только после P1 gate). Ничего не выдумывает."
---

# STAGE-13 — Next task selector

Полный источник шагов — `docs/ops/stages/STAGE-13-NEXT-TASK.md`.

## Инструмент

```bash
python tools/runbook_next.py
python tools/runbook_next.py --json
```

Скрипт читает бэклог, gate-отчёты и подпись PILOT_DECISION, применяет правила
механически и либо называет задачу, либо сообщает причину блокировки.

## Правила

1. Не выбирать задачу потому, что она интересная.
2. Сначала dependencies.
3. Затем P0 blockers.
4. Затем customer value.
5. Затем architecture risk.
6. Затем implementation cost.
7. P1 запрещён, пока P0 gate не разрешил переход.
8. P2 запрещён до P1 gate.

## Если приоритет неочевиден

`value_score`, `risk_score`, `cost_score` не заполнены — скрипт честно
сообщает, что приоритет требует человека. Не подставляй оценку сам.

## Выход

`docs/tasks/NEXT_TASK.md`: TASK, WHY NOW, DEPENDENCIES, CUSTOMER VALUE,
IMPLEMENTATION PLAN, RISKS, TESTS, DEFINITION OF DONE.

## Финиш

После выбора ждать команды на реализацию. Остановись.

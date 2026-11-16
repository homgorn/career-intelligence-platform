---
name: ci-stage-14-task-executor
description: "Career Intelligence / AI Profession Intelligence, этап STAGE-14 — Task executor. Постоянный универсальный исполнитель, запускается после STAGE-13 по одной задаче за сеанс. Порядок PLAN → IMPLEMENT → TEST → SECURITY CHECK → ANALYTICS CHECK → DOCS → DoD → REPORT. Не дублирует абстракции, не нарушает bounded contexts, не обходит gates, не меняет public contracts без ADR."
---

# STAGE-14 — Task executor

Полный источник шагов — `docs/ops/stages/STAGE-14-TASK-EXECUTOR.md`.

## Перед началом

1. Прочитай task.
2. Прочитай все указанные dependencies.
3. Прочитай соответствующие спеки.
4. Проверь существующий код.
5. Не дублируй существующие abstractions.
6. Не нарушай bounded contexts.
7. Не обходи gates.
8. Не меняй public contracts без ADR.

## Порядок

PLAN → IMPLEMENT → TEST → SECURITY CHECK → ANALYTICS CHECK → DOCS →
DEFINITION OF DONE → REPORT.

Архитектурная проблема — не скрытый workaround, а немедленная остановка
и ADR.

## Report

STATUS, CHANGES, TESTS, RISKS, OPEN QUESTIONS, NEXT TASK.

## Контроль

```bash
python tools/runbook_validate.py
```

## Финиш

Заполни `docs/ops/STAGE-STATUS.md`. Не запускай STAGE-13 в том же сеансе.
Остановись.

# STAGE-14 — Task executor (постоянный)

> Универсальный исполнитель из исходной цепочки. Запускается после STAGE-13,
> по одной задаче за сеанс.

## Назначение

Реализовать выбранную задачу строго в её рамках.

## Trigger

`NEXT_TASK.md` содержит задачу, человек дал команду на реализацию.

## Inputs

- Карточка задачи `docs/tasks/P0|TASK-XXXX.md`
- Все указанные dependencies
- Соответствующие спеки
- Существующий код
- `AGENTS.md`, `docs/contracts/*`

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
DEFINITION OF DONE → REPORT

Если обнаружена архитектурная проблема — остановись и создай ADR вместо
скрытого workaround.

## Outputs

Обновлённый код, тесты, документация, статус задачи в бэклоге.

## Report

```
STATUS
CHANGES
TESTS
RISKS
OPEN QUESTIONS
NEXT TASK
```

## Definition of Done

- [ ] Задача реализована в объявленных границах.
- [ ] Тесты проходят, включая security и analytics checks.
- [ ] Документация обновлена.
- [ ] Статус задачи в `MASTER_BACKLOG.json` изменён.
- [ ] `NEXT_TASK.md` ещё не трогаем — это STAGE-13.
- [ ] OPEN QUESTIONS зафиксированы.

## HARD STOP

После REPORT ждать человека. Не запускать STAGE-13 в том же сеансе.

## Rollback

Откат изменений задачи; статус задачи возвращается в `PENDING`. Если откат
невозможен без потери данных — фиксируется в `STAGE-STATUS.md` как риск.

## Промпт для IDE

```text
Реализуй TASK-XXXX.

Перед началом:
1. Прочитай task.
2. Прочитай все указанные dependencies.
3. Прочитай соответствующие спeки.
4. Проверь существующий код.
5. Не дублируй существующие abstractions.
6. Не нарушай bounded contexts.
7. Не обходи gates.
8. Не меняй public contracts без ADR.

Затем: PLAN → IMPLEMENT → TEST → SECURITY CHECK → ANALYTICS CHECK →
DOCS → DEFINITION OF DONE → REPORT.

Если обнаружена архитектурная проблема — остановись и создай ADR
вместо скрытого workaround.

В конце: STATUS, CHANGES, TESTS, RISKS, OPEN QUESTIONS, NEXT TASK.
Заполни docs/ops/STAGE-STATUS.md и остановись.
```

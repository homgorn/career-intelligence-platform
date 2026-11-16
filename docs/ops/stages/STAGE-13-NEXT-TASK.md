# STAGE-13 — Next task selector (постоянный)

> Бывший PROMPT 13. Используется постоянно, после каждой выполненной задачи,
> до следующего gate.

## Назначение

Выбрать ровно одну следующую задачу. Никогда не выбирать задачу только потому,
что она интересная.

## Trigger

После завершения любой задачи, или по явной команде человека.

## Inputs

- `docs/tasks/MASTER_BACKLOG.json`
- `docs/tasks/NEXT_TASK.md`
- Результаты P0/P1/P2 gate
- `docs/ops/STAGE-STATUS.md`

## Правила выбора

1. Никогда не выбирай задачу только потому, что она интересная.
2. Сначала dependencies.
3. Затем P0 blockers.
4. Затем customer value.
5. Затем architecture risk.
6. Затем implementation cost.
7. P1 запрещён, пока P0 gate не разрешил переход.
8. P2 запрещён до P1 gate.

## Outputs

`docs/tasks/NEXT_TASK.md` с ровно одной задачей.

## Формат

```
TASK
WHY NOW
DEPENDENCIES
CUSTOMER VALUE
IMPLEMENTATION PLAN
RISKS
TESTS
DEFINITION OF DONE
```

## Definition of Done

- [ ] Выбрана ровно одна задача.
- [ ] У неё нет незакрытых зависимостей.
- [ ] Она разрешена текущим gate.
- [ ] Есть WHY NOW и обоснование по правилам 1–8.
- [ ] `NEXT_TASK.md` содержит все восемь разделов.

## HARD STOP

После выбора ждать команды на реализацию.

## Rollback

Перевыбор задачи = новая версия `NEXT_TASK.md`, старая помечается `superseded`.

## Промпт для IDE

```text
Этап STAGE-13 — выбор следующей задачи.

Используй MASTER_BACKLOG и текущие результаты проекта.

Определи следующую задачу. Правила:
1. Никогда не выбирай задачу только потому, что она интересная.
2. Сначала dependencies.
3. Затем P0 blockers.
4. Затем customer value.
5. Затем architecture risk.
6. Затем implementation cost.
7. P1 запрещён, пока P0 gate не разрешил переход.
8. P2 запрещён до P1 gate.

Выбери РОВНО ОДНУ следующую задачу.
Выведи: TASK, WHY NOW, DEPENDENCIES, CUSTOMER VALUE,
IMPLEMENTATION PLAN, RISKS, TESTS, DEFINITION OF DONE.

После этого жди команды на реализацию.
Обнови docs/tasks/NEXT_TASK.md.
```

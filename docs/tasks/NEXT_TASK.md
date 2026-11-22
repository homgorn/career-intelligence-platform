# NEXT_TASK

Содержит ровно одну задачу, которую безопасно выполнять следующей.
Обновляется этапом `STAGE-13` после каждой выполненной задачи.

Выбор сделан механически: `python tools/runbook_next.py`.

---

## TASK

`TASK-P0-001` — Choose ICP + profession + measurable workflow
(STAGE-00A, priority P0, depends_on: нет).

## WHY NOW

Это единственная задача, которая не требует уже подписанного пилота: она сама
его создаёт (`produces_pilot_decision: true`). Все остальные 21 задача
бэклога заблокированы `BLOCKED_ON_PILOT`: без выбранного ICP, профессии,
workflow и страны нельзя ни заморозить контракты (STAGE-02), ни измерить
исход (STAGE-12).

## DEPENDENCIES

Нет. Входы: `docs/architecture/PILOT_OPTIONS.md`,
`docs/architecture/P0_SCOPE.md`, `docs/architecture/ARCHITECTURE_RISKS.md`,
`20_OPEN_QUESTIONS_AND_RESEARCH_BACKLOG.md`.

## CUSTOMER VALUE

Не создаёт ценности напрямую — снимает неопределённость, без которой нельзя
начать ни один этап реализации. Ценность измеряется косвенно: без этого
решения P0 gate не может быть пройден вообще.

## IMPLEMENTATION PLAN

1. Владелец читает `PILOT_OPTIONS.md` (три кандидата, явные неизвестные).
2. Проводит дешёвую проверку: 5–8 интервью по выбранному кандидату.
3. Заполняет `docs/templates/PILOT_DECISION.md` и копирует в
   `docs/architecture/PILOT_DECISION.md`: ICP, профессия, workflow, страна,
   baseline, целевой исход, пороги gate, бюджет, срок, таксономия.
4. Подписывает `signed_by` / `signed_at`.
5. IDE оформляет `docs/decisions/ADR-0002-stack-and-pilot.md` уже после
   решения (стек + таксономия), не подменяя решение.

## RISKS

- Ложная уверенность без интервью: числа рынка не проверены никем.
- Выбор «интересной» профессии вместо измеримой задачи.
- Растянутый исход (как в варианте B) ломает 14-дневное окно измерения.
- Пилот выбран, но канал привлечения отсутствует — P0 gate не на ком проверять.

## TESTS

```bash
python tools/runbook_validate.py --stage STAGE-00A   # ожидается WAIT до подписи, PASS после
python tools/runbook_next.py                          # после подписи выберет TASK-P0-002
```

## DEFINITION OF DONE

- [ ] `PILOT_DECISION.md` заполнен по всем разделам шаблона.
- [ ] Есть `signed_by` и `signed_at`.
- [ ] Заданы числовые пороги P0 gate.
- [ ] Зафиксированы таксономия и стек (или явно переданы в ADR).
- [ ] `STAGE-00A` валидатор: `PASS`, не `WAIT`.

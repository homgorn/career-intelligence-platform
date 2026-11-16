# STAGE-STATUS — журнал этапов и задач

Заполняется после каждого этапа и после каждой задачи. Без этой записи этап
считается не завершённым.

## Журнал

| Дата | Этап / задача | Статус | Артефакты | Тесты | Комментарий |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | STAGE-00 Audit | AWAITING_HUMAN | `SPEC_INDEX.md`, `SPEC_INDEX_DATA.tsv`, `MASTER_ARCHITECTURE_MAP.md`, `DEPENDENCY_MAP.md`, `P0_SCOPE.md`, `ARCHITECTURE_RISKS.md`, `ADR-0001` | `python tools/runbook_validate.py --stage STAGE-00` → PASS | Инвентаризировано 109 файлов; 8 конфликтов зафиксировано; ждёт подтверждения человека |
| 2026-11-16 | Лицензирование | ACCEPTED | `LICENSE-MAP.md`, `LICENSES/`, ADR-0002 (ACCEPTED), CONTRIBUTING DCO | docs-only change; legal review TRIGGERED, not performed | Владелец подтвердил «делай ок»; Change License → GPL-3.0-or-later (BUSL covenant); legal review обязателен до первого BUSL-файла |

## Статусы

- `PENDING` — не начат.
- `IN_PROGRESS` — выполняется.
- `BLOCKED_ON_PILOT` — нужны решения по пилоту (STAGE-00A).
- `BLOCKED_ON_QUESTION` — есть OPEN QUESTION, влияющий на контракт.
- `AWAITING_HUMAN` — артефакты готовы, ждём подтверждения человека.
- `DONE` — завершён, gate пройден.
- `FAILED` — gate не пройден, есть список исправлений.
- `DEFERRED` — отложен в более позднюю фазу.

## Текущее состояние

- Активный этап: `STAGE-00` завершён, ждёт подтверждения человека.
- Следующий этап: `STAGE-00A` (пилот, решает человек).
- Последний gate: нет.
- Открытых blocking questions: 8 архивных конфликтов (C-001…C-008) +
  вопросы пилота из `20_OPEN_QUESTIONS_AND_RESEARCH_BACKLOG.md`.

## Быстрый аудит журнала

После каждой записи проверь:

1. Есть ли артефакт на каждый пункт Outputs карточки этапа?
2. Есть ли вывод тестов или команда, которой его можно повторить?
3. Есть ли HARD STOP и ждёт ли этап человека?
4. Есть ли OPEN QUESTIONS и у каждой есть владелец?

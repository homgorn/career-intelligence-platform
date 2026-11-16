# STAGE-02 — Contract freeze + executable backlog

> Бывший PROMPT 02, усиленный. Добавлены: заморозка контрактов и единая система
> ID задач. Именно здесь спеки-оглавления превращаются в типизированные
> контракты, которые утверждает человек.

## Назначение

1. Заморозить контракты, по которым будет писаться код: каталог событий,
   API foundation, целевая схема данных P0.
2. Превратить архитектуру в исполнимый бэклог с задачами по IDE_TASK_TEMPLATE.

## Trigger

Подписан `PILOT_DECISION.md`. Завершён STAGE-01.

## Inputs

- `IDE_TASK_TEMPLATE.json` из архива.
- `MASTER_DEPENDENCY_GRAPH.json` — базовые ID задач.
- `03_EVENT_CONTRACTS_SPEC.md` — 17 канонических событий и envelope.
- `37_API_CONTRACTS_SPEC.md`, `09_DATABASE_ARCHITECTURE_SPEC.md`,
  `02_DOMAIN_MODEL_SPEC.md`, `49_AI_DATA_MODEL_ADDENDUM.md`.
- `45_IDE_EXECUTION_BACKLOG_SCHEMA.md`, `49_DEFINITION_OF_DONE_GLOBAL.md`.

## Шаги

### А. Заморозка контрактов

1. Составить каталог событий на базе `03_EVENT_CONTRACTS_SPEC.md`: envelope,
   17 типов, payload-контракты, privacy_class, правила идемпотентности.
2. Спроектировать target schema данных P0: список таблиц, ключи, индексы,
   ограничения, tenant scope, versioning, provenance-поля, lifecycle.
3. Спроектировать API foundation P0: аутентификация, tenant isolation,
   ошибки, пагинация, версионирование, идемпотентность.
4. Оформить всё как документы-контракты и вынести на утверждение человеку
   через ADR. **До утверждения код не пишется.**

### Б. Бэклог

5. Сформировать задачи P0/P1/P2 по шаблону `docs/templates/TASK_CARD.md`.
6. Каждой задаче присвоить ID из архива. Новые задачи — продолжением нумерации.
7. В каждой задаче указать `spec_refs` — файл спеки и раздел.
8. Построить `docs/tasks/MASTER_BACKLOG.json` с метаданными и статусами.
9. Сформировать `docs/tasks/NEXT_TASK.md` — ровно одна безопасная следующая
   задача, с указанием, почему именно она.

## Outputs

- `docs/contracts/events/EVENT-CATALOG.md` (+ machine-readable `.json`)
- `docs/contracts/domain/DATA-MODEL-P0.md` (DDL-проект)
- `docs/contracts/api/API-FOUNDATION.md`
- `docs/decisions/ADR-0003-data-model-canonical.md`
- `docs/decisions/ADR-0004-event-catalog.md`
- `docs/tasks/P0/`, `docs/tasks/P1/`, `docs/tasks/P2/` — карточки задач
- `docs/tasks/MASTER_BACKLOG.json`
- `docs/tasks/NEXT_TASK.md`

## Definition of Done

- [ ] Каталог событий включает envelope и все 17 типов, каждый с payload-схемой.
- [ ] Target schema покрывает все сущности P0 из STAGE-04 со scope, versioning
      и provenance.
- [ ] Ни один контракт не написан «на глаз» — у каждого есть версия и владелец.
- [ ] У каждой задачи есть: objective, customer_value, priority, dependencies,
      inputs, outputs, acceptance_criteria, security, legal_trigger, analytics,
      tests, rollback, definition_of_done.
- [ ] Нет задач без customer value, измеримого acceptance criterion,
      зависимостей и DoD.
- [ ] `NEXT_TASK.md` содержит ровно одну задачу и обоснование выбора.
- [ ] Контракты утверждены человеком.

## HARD STOP

Показать: число контрактов, число задач P0/P1/P2, выбранную следующую задачу,
открытые вопросы. Ждать человека.

## Rollback

Удалить созданные контракты и карточки, каталог событий откатить к версии
из `03_EVENT_CONTRACTS_SPEC.md`. Бэклог — к состоянию `PENDING`.

## Промпт для IDE

```text
Этап STAGE-02 — contract freeze + executable backlog.

Прочитай:
- career-intelligence-research-specs-v02/IDE_TASK_TEMPLATE.json
- career-intelligence-research-specs-v02/MASTER_DEPENDENCY_GRAPH.json
- career-intelligence-research-specs-v02/03_EVENT_CONTRACTS_SPEC.md
- career-intelligence-research-specs-v02/37_API_CONTRACTS_SPEC.md
- career-intelligence-research-specs-v02/09_DATABASE_ARCHITECTURE_SPEC.md
- career-intelligence-research-specs-v02/02_DOMAIN_MODEL_SPEC.md
- career-intelligence-research-specs-v02/45_IDE_EXECUTION_BACKLOG_SCHEMA.md
- career-intelligence-research-specs-v02/49_DEFINITION_OF_DONE_GLOBAL.md
- docs/architecture/PILOT_DECISION.md

Часть А — заморозка контрактов.
1. Каталог событий: envelope, 17 канонических событий, payload-схемы,
   privacy_class, идемпотентность, правила replay.
2. Target schema данных P0: таблицы, ключи, индексы, ограничения, tenant scope,
   versioning, provenance, lifecycle.
3. API foundation: auth, tenant isolation, ошибки, пагинация, версионирование,
   идемпотентность.
Оформи как документы-контракты и вынеси на утверждение человеку через ADR.

Часть Б — бэклог.
4. Задачи P0/P1/P2 по docs/templates/TASK_CARD.md.
5. ID задач — из MASTER_DEPENDENCY_GRAPH.json; новые задачи продолжают
   нумерацию, не перезапуская её.
6. У каждой задачи обязательны spec_refs — файл и раздел спеки.
7. docs/tasks/MASTER_BACKLOG.json — единственный живой бэклог.
8. docs/tasks/NEXT_TASK.md — ровно одна следующая задача и почему она.

Не реализуй задачи. Не создавай второй dependency graph.
В конце заполни docs/ops/STAGE-STATUS.md и остановись.
```

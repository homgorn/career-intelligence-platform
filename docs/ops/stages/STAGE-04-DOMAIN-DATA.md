# STAGE-04 — Domain + data

> Бывший PROMPT 04, исправленный. В исходном списке P0-сущностей не хватало
> `Consent`, `PolicyDecision`, `AuditEvent`, `Source` — без них гейты STAGE-09
> и требования STAGE-05 к provenance и version политики нереализуемы.

## Назначение

Реализовать domain/data foundation P0 строго по замороженным контрактам.

## Trigger

Завершён STAGE-03.

## Inputs

- `docs/contracts/domain/DATA-MODEL-P0.md` (заморожен в STAGE-02, утверждён ADR-0003)
- `docs/contracts/events/EVENT-CATALOG.md`
- `02_DOMAIN_MODEL_SPEC.md` — канон предметной модели для P0
- `49_AI_DATA_MODEL_ADDENDUM.md` — AI-слой, только если нужен по STAGE-05A
- `09_DATABASE_ARCHITECTURE_SPEC.md`, `10_DATA_GOVERNANCE_PROVENANCE_SPEC.md`,
  `03_EVENT_CONTRACTS_SPEC.md`

## Сущности P0

Обязательны:

- Person
- Tenant
- CareerProfile
- AIProfile
- Goal
- Occupation
- Skill
- Task
- Workflow
- WorkRecipe
- Tool
- Recommendation
- Evidence
- Outcome

Добавлены к исходному списку (необходимы для гейтов):

- Source — источник evidence
- Consent — согласие (юридический gate)
- PolicyDecision — результат политики с версией
- AuditEvent — след действий (security gate)

## По каждой сущности

- ID;
- ownership;
- tenant scope;
- timestamps;
- versioning где необходимо;
- provenance где необходимо;
- lifecycle;
- indexes;
- constraints.

## Обязательные разделения

- `CareerProfile != AIProfile`.
- `WorkRecipe` — самостоятельная сущность, а не поле профиля.
- `Evidence` связана с claims / recommendations.
- `Outcome` связана с implementation / recommendation.
- `PolicyDecision` связана с recommendation и хранит policy version.
- `Consent` связана с Person и содержит purpose, granted_at, revoked_at, legal_basis.
- `AuditEvent` неизменяем, пишется на каждое consequential действие.

## Порядок

1. Migration / schema.
2. Repositories / services.
3. API.
4. Tests.

## Outputs

- Schema/migrations
- Repository/service layer
- API endpoints по замороженному контракту
- Tests (unit + integration + tenant isolation)
- Updated `DATA-MODEL-P0.md` с фактической схемой

## Definition of Done

- [ ] Все 18 сущностей P0 имеют таблицы, scope, timestamps, indexes, constraints.
- [ ] Versioning там, где указано в спеке; provenance там, где указано.
- [ ] Tenant isolation проверен тестом на каждой таблице с tenant scope.
- [ ] `CareerProfile` и `AIProfile` — разные таблицы с разным lifecycle.
- [ ] `WorkRecipe` ссылается на Task + Context + Tool + Implementation.
- [ ] `Evidence → Recommendation` и `Outcome → Implementation` связаны.
- [ ] Нет giant `users` table.
- [ ] Сущности, не нужные P0, не добавляются без ADR.
- [ ] Миграции применяются и откатываются.

## HARD STOP

Показать: число таблиц, число тестов, статус tenant isolation, открытые вопросы.
Ждать человека.

## Rollback

Откат миграций, удаление созданных модулей, возврат `DATA-MODEL-P0.md` к версии
из STAGE-02. Данные пилота не удаляются без явной команды человека.

## Промпт для IDE

```text
Этап STAGE-04 — domain + data foundation P0.

Строго основывайся на:
- docs/contracts/domain/DATA-MODEL-P0.md
- docs/contracts/events/EVENT-CATALOG.md
- career-intelligence-research-specs-v02/02_DOMAIN_MODEL_SPEC.md
- career-intelligence-research-specs-v02/09_DATABASE_ARCHITECTURE_SPEC.md
- career-intelligence-research-specs-v02/10_DATA_GOVERNANCE_PROVENANCE_SPEC.md
- career-intelligence-research-specs-v02/03_EVENT_CONTRACTS_SPEC.md

Реализуй минимальный набор сущностей:
Person, Tenant, CareerProfile, AIProfile, Goal, Occupation, Skill, Task,
Workflow, WorkRecipe, Tool, Recommendation, Evidence, Outcome,
Source, Consent, PolicyDecision, AuditEvent.

По каждой: ID, ownership, tenant scope, timestamps, versioning где нужно,
provenance где нужно, lifecycle, indexes, constraints.

Не превращай всё в одну giant users table.

Особенно:
- CareerProfile != AIProfile;
- WorkRecipe — самостоятельная сущность;
- Evidence связана с claims/recommendations;
- Outcome связана с implementation/recommendation;
- PolicyDecision хранит policy version;
- Consent: purpose, granted_at, revoked_at, legal_basis;
- AuditEvent неизменяем.

Порядок: migration/schema → repositories/services → API → tests.
Не добавляй сущности, не нужные P0, без ADR.

В конце заполни docs/ops/STAGE-STATUS.md и остановись.
```

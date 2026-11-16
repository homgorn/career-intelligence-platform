---
name: ci-stage-04-domain-data
description: "Career Intelligence / AI Profession Intelligence, этап STAGE-04 — Domain + data. Применять только после STAGE-03. Реализует 18 сущностей P0 (включая Consent, PolicyDecision, AuditEvent, Source) по замороженной схеме. Порядок: migration → repositories/services → API → tests. CareerProfile != AIProfile, WorkRecipe — самостоятельная сущность."
---

# STAGE-04 — Domain + data

Полный источник шагов — `docs/ops/stages/STAGE-04-DOMAIN-DATA.md`.

## Перед стартом

- [ ] Завершён STAGE-03.
- [ ] Схема `DATA-MODEL-P0.md` заморожена и утверждена ADR-0003.

## Сущности P0

Person, Tenant, CareerProfile, AIProfile, Goal, Occupation, Skill, Task,
Workflow, WorkRecipe, Tool, Recommendation, Evidence, Outcome,
Source, Consent, PolicyDecision, AuditEvent.

По каждой: ID, ownership, tenant scope, timestamps, versioning где нужно,
provenance где нужно, lifecycle, indexes, constraints.

## Обязательные разделения

- `CareerProfile != AIProfile`.
- `WorkRecipe` — самостоятельная сущность.
- `Evidence → Recommendation`, `Outcome → Implementation`.
- `PolicyDecision` хранит policy version.
- `Consent`: purpose, granted_at, revoked_at, legal_basis.
- `AuditEvent` неизменяем.

Не превращать всё в одну giant `users` table. Сущности, не нужные P0,
не добавлять без ADR.

## Порядок

1. Migration / schema.
2. Repositories / services.
3. API.
4. Tests.

## Контроль

```bash
python tools/runbook_validate.py --stage STAGE-04
```

Валидатор проверяет, что все 18 сущностей описаны в `DATA-MODEL-P0.md`.

## Финиш

Число таблиц, число тестов, статус tenant isolation, открытые вопросы.
Остановись.

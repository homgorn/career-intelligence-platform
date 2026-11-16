# STAGE-16 — B2B layer

> Бывший PROMPT 15. Запускается после release gate P1, не раньше.

## Назначение

Подготовить B2B-слой, не сломав B2C архитектуру.

## Trigger

Release gate P1 пройден.

## Inputs

- `15_B2B_VALUE_SPEC.md`
- `16_B2B2C_AND_PARTNER_VALUE_SPEC.md`
- `38_TENANCY_IDENTITY_RBAC_SPEC.md`
- `11_SECURITY_ARCHITECTURE_SPEC.md`, `12_LEGAL_COMPLIANCE_SPEC.md`
- `22_BILLING_MONETIZATION_SPEC.md`, `39_BILLING_ENTITLEMENT_SPEC.md`
- `31_OUTCOME_ROI_ENGINE_SPEC.md`

## B2B value chain

diagnostic → transformation backlog → implementation → enablement →
measurement → optimization.

## Нужны

Organization, Tenant, Teams, Members, Roles, Goals, Workflows,
Transformation initiatives, Outcomes, ROI.

## Переиспользовать

WorkRecipe, Task, Workflow, Skill, Tool, Outcome, Evidence.

B2B не должен превращаться в отдельный независимый продукт.

## Enterprise gates

security, privacy, procurement, audit, data export, retention, SSO/RBAC,
support, billing.

## Outputs

- Architecture document
- Contracts for B2B entities
- Enterprise gate plan

## Definition of Done

- [ ] B2B сущности переиспользуют B2C domain, а не дублируют её.
- [ ] Tenant и RBAC покрывают Organization / Team / Member.
- [ ] Enterprise gates описаны и привязаны к существующим gate'ам.
- [ ] Нет enterprise features без P0/P1 обоснования.

## HARD STOP

Сначала архитектура и контракты. Enterprise features без обоснования
не реализуются. Ждать человека.

## Rollback

B2B-слой отключается флагами; B2C домен не меняется.

## Промпт для IDE

```text
Этап STAGE-16 — B2B layer (только после release gate P1).

Основывайся на:
- career-intelligence-research-specs-v02/15_B2B_VALUE_SPEC.md
- career-intelligence-research-specs-v02/16_B2B2C_AND_PARTNER_VALUE_SPEC.md
- career-intelligence-research-specs-v02/38_TENANCY_IDENTITY_RBAC_SPEC.md
- career-intelligence-research-specs-v02/11_SECURITY_ARCHITECTURE_SPEC.md
- career-intelligence-research-specs-v02/12_LEGAL_COMPLIANCE_SPEC.md
- career-intelligence-research-specs-v02/22_BILLING_MONETIZATION_SPEC.md
- career-intelligence-research-specs-v02/31_OUTCOME_ROI_ENGINE_SPEC.md

B2B value: diagnostic → transformation backlog → implementation →
enablement → measurement → optimization.

Нужны: Organization, Tenant, Teams, Members, Roles, Goals, Workflows,
Transformation initiatives, Outcomes, ROI.

Переиспользуй: WorkRecipe, Task, Workflow, Skill, Tool, Outcome, Evidence.
B2B не должен превращаться в отдельный независимый продукт.

Enterprise gates: security, privacy, procurement, audit, data export,
retention, SSO/RBAC, support, billing.

Сначала создай architecture + contracts.
Не реализуй enterprise features без P0/P1 обоснования.
```

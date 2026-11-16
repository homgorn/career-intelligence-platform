---
name: ci-stage-16-b2b
description: "Career Intelligence / AI Profession Intelligence, этап STAGE-16 — B2B layer. Только после release gate P1. Сначала архитектура и контракты, enterprise gates, переиспользование WorkRecipe/Task/Workflow/Skill/Tool/Outcome/Evidence. B2B не должен превращаться в отдельный продукт. Enterprise features без P0/P1 обоснования не реализуются."
---

# STAGE-16 — B2B layer

Полный источник шагов — `docs/ops/stages/STAGE-16-B2B.md`.

## Условие

Release gate P1 пройден. В P0 не запускается.

## Value chain

diagnostic → transformation backlog → implementation → enablement →
measurement → optimization.

## Сущности

Organization, Tenant, Teams, Members, Roles, Goals, Workflows,
Transformation initiatives, Outcomes, ROI.

## Переиспользовать

WorkRecipe, Task, Workflow, Skill, Tool, Outcome, Evidence.

## Enterprise gates

security, privacy, procurement, audit, data export, retention, SSO/RBAC,
support, billing.

## Порядок

Сначала архитектура и контракты. Реализация — после обоснования.

## Контроль

```bash
python tools/runbook_validate.py --stage STAGE-16
```

## Финиш

Покажи архитектуру и контракты, ничего не реализуя без обоснования.
Остановись.

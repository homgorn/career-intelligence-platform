# STAGE-18 — Tool / plugin / MCP registry

> Бывший PROMPT 17. Запускается после release gate P1.

## Назначение

Реализовать Registry инструментов с lifecycle и fallback.

## Trigger

Release gate P1 пройден.

## Inputs

- `26_MCP_TOOL_PLUGIN_SPEC.md`
- `27_SKILLS_PLUGIN_MAPPING_SPEC.md`
- `47_ADAPTER_CATALOG.md`
- `05_GATES_AND_ADAPTERS_SPEC.md`
- `34_TOOL_PLUGIN_INTEGRATION_CATALOG_SPEC.md`
- `26_AI_TOOL_RECOMMENDATION_SPEC.md`

## Каждый tool

identity, provider, capability, input schema, output schema, auth scope,
risk, data class, region, pricing, version, verification date, health, owner.

## Lifecycle

DISCOVERED → REVIEW → VERIFIED → AVAILABLE → DEPRECATED → RETIRED.

## Обязательные правила

- Никакой plugin не становится hard dependency domain layer.
- Если tool unavailable — fallback должен существовать.
- Tool recommendation учитывает: user, task, goal, region, budget, skill,
  risk, privacy, existing stack, expected outcome.
- Region availability — versioned property, а не предположение.

## Outputs

- Registry service
- Adapter contracts
- Lifecycle management
- Fallback matrix
- Verification schedule

## Definition of Done

- [ ] У каждого инструмента есть owner и lifecycle status.
- [ ] У каждого инструмента есть fallback.
- [ ] Auth scope и data class обязательны.
- [ ] Region availability версионирована.
- [ ] Рекомендация не ломается при недоступности провайдера.

## HARD STOP

Показать registry и первую матрицу fallback. Ждать человека.

## Rollback

Инструмент переводится в `DEPRECATED`, рекомендация откатывается к fallback.

## Промпт для IDE

```text
Этап STAGE-18 — tool/plugin/skill/MCP registry.

Основывайся на:
- career-intelligence-research-specs-v02/26_MCP_TOOL_PLUGIN_SPEC.md
- career-intelligence-research-specs-v02/27_SKILLS_PLUGIN_MAPPING_SPEC.md
- career-intelligence-research-specs-v02/47_ADAPTER_CATALOG.md
- career-intelligence-research-specs-v02/05_GATES_AND_ADAPTERS_SPEC.md
- career-intelligence-research-specs-v02/34_TOOL_PLUGIN_INTEGRATION_CATALOG_SPEC.md
- career-intelligence-research-specs-v02/26_AI_TOOL_RECOMMENDATION_SPEC.md

Каждый tool: identity, provider, capability, input schema, output schema,
auth scope, risk, data class, region, pricing, version, verification date,
health, owner.

Lifecycle: DISCOVERED → REVIEW → VERIFIED → AVAILABLE → DEPRECATED → RETIRED.

Никакой plugin не становится hard dependency domain layer.
Если tool unavailable — fallback должен существовать.
Tool recommendation учитывает: user, task, goal, region, budget, skill,
risk, privacy, existing stack, expected outcome.
Region availability — versioned property.
```

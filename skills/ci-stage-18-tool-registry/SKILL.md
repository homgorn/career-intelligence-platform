---
name: ci-stage-18-tool-registry
description: "Career Intelligence / AI Profession Intelligence, этап STAGE-18 — Tool / plugin / MCP registry. Только после release gate P1. Registry с lifecycle DISCOVERED→REVIEW→VERIFIED→AVAILABLE→DEPRECATED→RETIRED, fallback для каждого инструмента, versioned region availability, запрет hard dependency на domain layer. Tool recommendation учитывает user, task, goal, region, budget, skill, risk, privacy, stack, outcome."
---

# STAGE-18 — Tool / plugin / MCP registry

Полный источник шагов — `docs/ops/stages/STAGE-18-TOOL-REGISTRY.md`.

## Условие

Release gate P1 пройден.

## У каждого tool

identity, provider, capability, input schema, output schema, auth scope,
risk, data class, region, pricing, version, verification date, health, owner.

## Lifecycle

DISCOVERED → REVIEW → VERIFIED → AVAILABLE → DEPRECATED → RETIRED.

## Обязательные правила

- Никакой plugin не становится hard dependency domain layer.
- Если tool unavailable — fallback должен существовать.
- Region availability — versioned property, а не предположение.
- Рекомендация учитывает: user, task, goal, region, budget, skill, risk,
  privacy, existing stack, expected outcome.

## Выходы

Registry service, adapter contracts, lifecycle management, fallback matrix,
verification schedule.

## Контроль

```bash
python tools/runbook_validate.py --stage STAGE-18
```

## Финиш

Registry и первая матрица fallback. Остановись.

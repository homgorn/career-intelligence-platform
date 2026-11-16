---
name: ci-stage-07-knowledge-graph
description: "Career Intelligence / AI Profession Intelligence, этап STAGE-07 — Knowledge Graph. Отложен в P2: запускать только после release gate P1 и стабилизации data model. Derived projection из authoritative данных, asserted vs inferred edges, graph schema, projection, traversal, consistency tests. Не создавать graph DB ради технологии."
---

# STAGE-07 — Knowledge Graph (DEFERRED_P2)

Полный источник шагов — `docs/ops/stages/STAGE-07-KNOWLEDGE-GRAPH.md`.

## Не запускать раньше

- Release gate P1 пройден.
- P0 data model стабилен.
- Есть обоснование, что traversal material improves product decisions.

## Graph

```
Occupation → Task → Workflow → Skill → Tool → WorkRecipe → Learning → Outcome
```

Inferred relationship отличается от asserted. У каждой связи: source,
confidence, effective date, verification status.

Graph — derived projection из authoritative data, если нет отдельного
архитектурного решения.

## Порядок

1. Graph schema.
2. Projection.
3. Traversal queries.
4. Consistency tests.
5. Оценка необходимости отдельной graph DB.

## Контроль

```bash
python tools/runbook_validate.py --stage STAGE-07
```

## Финиш

Обоснование выбора хранилища и результат оценки. Остановись.

# STAGE-07 — Knowledge Graph

> Бывший PROMPT 07. **Отложен в P2.** В исходной цепочке он присутствовал в верхней
> схеме последовательности и отсутствовал в нижней — теперь статус зафиксирован
> явно: `DEFERRED_P2`.

## Назначение

Реализовать Knowledge Graph как derived projection из authoritative data,
после того как P0 data model стабилизирован и доказал себя.

## Trigger

Release gate P1 пройден. Подтверждено, что traversal material improves
product decisions. В P0 не запускается.

## Inputs

- `08_KNOWLEDGE_GRAPH_SPEC.md`
- `02_DOMAIN_MODEL_SPEC.md`
- `10_DATA_GOVERNANCE_PROVENANCE_SPEC.md`

## Graph

```
Occupation → Task → Workflow → Skill → Tool → WorkRecipe → Learning → Outcome
```

Inferred relationship отличается от asserted relationship. Каждая связь имеет:
source, confidence, effective date, verification status.

Graph — derived projection из authoritative data, если нет отдельного
архитектурного решения.

## Порядок

1. Graph schema.
2. Projection.
3. Traversal queries.
4. Consistency tests.
5. Оценить, нужен ли отдельный graph DB.

## Definition of Done

- [ ] Asserted и inferred связи различимы в схеме.
- [ ] У каждой связи есть source, confidence, effective dates, verification status.
- [ ] Projection воспроизводима из authoritative данных.
- [ ] Consistency tests проходят.
- [ ] Есть обоснование выбора между PostgreSQL graph tables и отдельной graph DB.

## HARD STOP

Показать обоснование выбора хранилища и результат оценки. Ждать человека.

## Rollback

Graph — производная проекция. Откат = удаление projection и traversal, authoritative
данные не затрагиваются.

## Промпт для IDE

```text
Этап STAGE-07 — knowledge graph (только после release gate P1).

Не запускай его раньше стабилизации P0 data model.

Основывайся на:
- career-intelligence-research-specs-v02/08_KNOWLEDGE_GRAPH_SPEC.md
- career-intelligence-research-specs-v02/02_DOMAIN_MODEL_SPEC.md
- career-intelligence-research-specs-v02/10_DATA_GOVERNANCE_PROVENANCE_SPEC.md

Graph: Occupation → Task → Workflow → Skill → Tool → WorkRecipe → Learning → Outcome.

Inferred relationship отличается от asserted. Каждая связь имеет:
source, confidence, effective date, verification status.

Graph — derived projection из authoritative data, если нет отдельного
архитектурного решения.

Сначала: graph schema, projection, traversal queries, consistency tests.
После этого оцени, нужен ли отдельный graph DB.

Не создавай graph database только ради технологии.
```

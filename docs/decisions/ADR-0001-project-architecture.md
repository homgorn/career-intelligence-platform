---
doc_type: adr
status: ACCEPTED
id: ADR-0001
title: Project architecture and operating model
date: 2026-11-15
supersedes:
---

# ADR-0001 — Project architecture and operating model

## Контекст

Архив из 109 файлов задаёт продуктовые контракты, но не финальную техническую
архитектуру (`00_INDEX.md`). Нужно зафиксировать, какие решения уже приняты
архивом, что отложено на пилот и как проект будет исполняться, чтобы
последующие этапы не переизобретали одно и то же.

## Решения

### D1. Канон предметной модели

`02_DOMAIN_MODEL_SPEC.md` — канон для P0. `19_DATA_MODEL_CONCEPTUAL.md` —
`superseded`. `49_AI_DATA_MODEL_ADDENDUM.md` — применяется как addendum,
только если STAGE-05A обосновал LLM.

### D2. Bounded contexts и владение

Контексты и владельцы сущностей — из `MASTER_ARCHITECTURE_MAP.md`. Один
владелец на сущность; кросс-контекстные ссылки через стабильные ID и event
contracts. Giant mutable `user profile` object запрещён.

### D3. System of record и производные индексы

Реляционная БД (PostgreSQL) — authoritative. Search/vector/graph — производные
и перестраиваемые. LLM, векторный индекс и память модели не являются
источником истины.

### D4. Детерминизм и policy

Бизнес-правила, gates, entitlement, pricing, permissions и safety — typed и
детерминированные. LLM предлагает, typed services решают. Бизнес-логика
не хранится в промптах.

### D5. Единица ценности

`WorkRecipe` — центральная сущность. Каждая рекомендация имеет evidence,
confidence, engine version, policy results, alternatives, expected outcome
и verification method.

### D6. Стек отложен

Язык, фреймворк, фронтенд и хостинг выбираются после пилота в `ADR-0002`.
Хранение уже задано: PostgreSQL + pgvector + OpenSearch/Elasticsearch;
Neo4j — только если traversal material improves decisions
(`09_DATABASE_ARCHITECTURE_SPEC.md`).

### D7. Порядок исполнения и gates

P0 → release gate → P1 → release gate → P2. Один этап за сеанс; human gates
останавливают прогресс. Release gate проходит по доказательству ценности,
а не по готовности бэклога.

### D8. Воспроизводимая проверка

Definition of Done частично машиночитаем: `docs/ops/assertions/*.json`,
`tools/runbook_validate.py`, `tools/runbook_next.py`, скиллы этапов.
Проверка артефактов отделяется от проверки кода.

### D9. Инструменты процесса

Валидатор, селектор, скиллы, при необходимости schedule — часть архитектуры
процесса, а не разовые скрипты. Их исходники версионируются в репозитории.

## Затрагиваемые контракты

- `docs/specs/SPEC_INDEX.md` — статусы спек.
- `docs/tasks/MASTER_BACKLOG.json` — единый бэклог.
- `docs/ops/RUNBOOK.md` — порядок и запреты.
- `AGENTS.md` — правила IDE.

## Последствия

Проще: единый источник правды по сущностям; проверяемые DoD; предсказуемый
процесс. Сложнее: нужно держать SPEC_STATUS и assertions в актуальном
состоянии; contract freeze требует паузы перед кодом. Влияние на security /
privacy / legal: проверяется на STAGE-09; юридический вывод остаётся
за counsel.

## Юридическая проверка

`NOT_REQUIRED` на уровне архитектуры. `TRIGGERED` на уровне конкретных
юрисдикций и use cases — через `LEGAL_GATE.md`.

## Откат

ADR-0001 можно пересмотреть новой версией. Уже созданные артефакты
(`MASTER_ARCHITECTURE_MAP`, `DEPENDENCY_MAP`, `P0_SCOPE`) перегенерируются
или помечаются `superseded`.

## Связанное

- `docs/architecture/P0_SCOPE.md`
- `docs/architecture/ARCHITECTURE_RISKS.md`
- `docs/ops/RUNBOOK.md`

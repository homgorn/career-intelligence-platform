---
name: ci-stage-02-contracts-backlog
description: "Career Intelligence / AI Profession Intelligence, этап STAGE-02 — Contract freeze + executable backlog. Применять только после подписанного PILOT_DECISION. Замораживает каталог событий, target-схему P0 и API foundation, затем строит единый бэклог с ID из MASTER_DEPENDENCY_GRAPH.json и ровно одну задачу в NEXT_TASK.md. Задачи не реализуются."
---

# STAGE-02 — Contracts + backlog

Полный источник шагов — `docs/ops/stages/STAGE-02-CONTRACTS-BACKLOG.md`.

## Перед стартом

- [ ] Подписан `docs/architecture/PILOT_DECISION.md`.
- [ ] Завершён STAGE-01.

## Часть А — заморозка контрактов

1. Каталог событий из `03_EVENT_CONTRACTS_SPEC.md`: envelope, 17 типов,
   payload, privacy_class, идемпотентность, replay.
2. Target schema данных P0: таблицы, ключи, индексы, tenant scope,
   versioning, provenance, lifecycle.
3. API foundation: auth, tenant isolation, ошибки, пагинация, версионирование.

Оформи как документы-контракты и вынеси на утверждение через ADR.
**До утверждения код не пишется.**

## Часть Б — бэклог

- ID задач — только из `MASTER_DEPENDENCY_GRAPH.json`. Нумерация продолжается,
  не перезапускается.
- У каждой задачи обязательны `spec_refs` — файл и раздел спеки.
- `docs/tasks/MASTER_BACKLOG.json` — единственный живой бэклог. Второй
  dependency graph не создаётся.
- `docs/tasks/NEXT_TASK.md` — ровно одна задача и почему она.

## Выходы

- `docs/contracts/events/EVENT-CATALOG.md`
- `docs/contracts/domain/DATA-MODEL-P0.md`
- `docs/contracts/api/API-FOUNDATION.md`
- `docs/decisions/ADR-0003-data-model-canonical.md`
- `docs/decisions/ADR-0004-event-catalog.md`
- `docs/tasks/MASTER_BACKLOG.json` (заполненный)
- `docs/tasks/NEXT_TASK.md`

## Контроль

```bash
python tools/runbook_validate.py --stage STAGE-02
```

Валидатор проверяет, что все 17 канонических событий на месте, у каждой
задачи заполнены `customer_value`, `acceptance_criteria` и `spec_refs`,
и что в NEXT_TASK ровно одна задача.

## Финиш

Покажи: число контрактов, число задач P0/P1/P2, выбранную следующую задачу.
Остановись.

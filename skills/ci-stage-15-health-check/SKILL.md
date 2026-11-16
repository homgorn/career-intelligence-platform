---
name: ci-stage-15-health-check
description: "Career Intelligence / AI Profession Intelligence, этап STAGE-15 — Architectural health check. Постоянный: каждые 5 выполненных задач, или >30 изменённых файлов, или на каждом release gate, или по команде человека. Ищет architecture drift, vendor lock-in, LLM coupling, hidden business logic in prompts, missing provenance, security/legal debt. Refactor автоматически не делать."
---

# STAGE-15 — Health check

Полный источник шагов — `docs/ops/stages/STAGE-15-HEALTH-CHECK.md`.

## Триггер (любое событие)

- Каждые 5 выполненных задач.
- Более 30 изменённых файлов с прошлой проверки.
- На каждом release gate.
- По явной команде человека.

Что наступит раньше.

## Сравнивать

IMPLEMENTED CODE vs MASTER SPECS vs MASTER BACKLOG vs CURRENT ADRs.

## Искать

architecture drift, duplicated logic, vendor lock-in, oversized modules,
missing tests, missing telemetry, security debt, legal debt, data-model drift,
API inconsistencies, undocumented behavior, LLM coupling, hidden business
logic inside prompts, missing provenance, missing rollback, dead code,
premature complexity.

## Классификация

CRITICAL / HIGH / MEDIUM / LOW. У каждого finding — владелец.

## Выход

`docs/architecture/HEALTH-CHECK.md` + remediation backlog, интегрированный
в `MASTER_BACKLOG.json`.

## Контроль

```bash
python tools/runbook_validate.py
```

## Финиш

Не делай refactor автоматически. Сначала findings и priority. Остановись.

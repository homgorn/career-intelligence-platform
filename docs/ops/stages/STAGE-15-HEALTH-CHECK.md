# STAGE-15 — Architectural health check (постоянный)

> Бывший PROMPT 14. Триггер сделан объективным вместо «примерно после 5–10
> задач».

## Назначение

Найти дрейф между реализованным кодом и спеками, бэклогом и ADR.

## Trigger (любое событие)

- Каждые 5 выполненных задач.
- Более 30 изменённых файлов с прошлой проверки.
- На каждом release gate.
- По явной команде человека.

Что наступит раньше.

## Inputs

- Реализованный код
- Мастер-спеки и `SPEC_INDEX.md`
- `MASTER_BACKLOG.json`
- Текущие ADR
- `STAGE-STATUS.md`

## Искать

Architecture drift, duplicated logic, vendor lock-in, oversized modules,
missing tests, missing telemetry, security debt, legal debt, data-model drift,
API inconsistencies, undocumented behavior, LLM coupling, hidden business
logic inside prompts, missing provenance, missing rollback, dead code,
premature complexity.

## Классификация

CRITICAL / HIGH / MEDIUM / LOW.

## Outputs

- `docs/architecture/HEALTH-CHECK.md`
- Remediation backlog

## Definition of Done

- [ ] Каждый finding имеет классификацию и владельца.
- [ ] Findings сравнены со спеками и ADR, а не с ощущениями.
- [ ] Remediation backlog интегрирован в `MASTER_BACKLOG.json`.
- [ ] Ни один CRITICAL не оставлен без плана.

## HARD STOP

Не делай refactor автоматически. Сначала покажи findings и priority.

## Rollback

Health check ничего не меняет в коде. Откат не требуется; удаление отчёта
возможно в любой момент.

## Промпт для IDE

```text
Этап STAGE-15 — architectural health check.

Сравни: IMPLEMENTED CODE vs MASTER SPECS vs MASTER BACKLOG vs CURRENT ADRs.

Найди: architecture drift, duplicated logic, vendor lock-in, oversized modules,
missing tests, missing telemetry, security debt, legal debt, data-model drift,
API inconsistencies, undocumented behavior, LLM coupling, hidden business
logic inside prompts, missing provenance, missing rollback, dead code,
premature complexity.

Классифицируй: CRITICAL, HIGH, MEDIUM, LOW.

Создай remediation backlog.
Не делай refactor автоматически. Сначала покажи findings и priority.
В конце заполни docs/ops/STAGE-STATUS.md и остановись.
```

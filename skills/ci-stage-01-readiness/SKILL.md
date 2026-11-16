---
name: ci-stage-01-readiness
description: "Career Intelligence / AI Profession Intelligence, этап STAGE-01 — Architecture readiness review. Применять только по явной команде человека и после STAGE-00/00A. Проверяет 25 областей, включая самосогласованность архива, отделяет blocking от non-blocking. Production-код не пишется."
---

# STAGE-01 — Architecture readiness review

Полный источник шагов — `docs/ops/stages/STAGE-01-READINESS-REVIEW.md`.

## Перед стартом

- [ ] Завершён STAGE-00.
- [ ] Идеально — подписан `PILOT_DECISION.md`. Без него проблемы, зависящие
      от пилота, помечаются `BLOCKED_ON_PILOT` и не закрываются молча.

## Обязательные проверки

Кроме 24 областей, проверь **самосогласованность архива**: конфликтующие
спеки, три модели данных, дублирующиеся новичковые и evaluation-спеки.

Ключевые утверждения, которые должны держаться:

- LLM не source of truth и не решает security/legal/billing.
- Vendor SDK не проникают в domain layer.
- Indexes производны от authoritative data.
- Provenance и policy version обязательны.
- Tenant isolation проверяется автоматически.
- Необратимые agent actions требуют approval.
- Customer value измерима.

## Выходы

- `docs/architecture/ARCHITECTURE_READINESS_REVIEW.md`
- Список blocking issues
- Список non-blocking issues

## Правило

Ни один blocking issue не «принимается» молча. Архитектурная проблема
правится через спеку или ADR, а не кодом.

## Контроль

```bash
python tools/runbook_validate.py --stage STAGE-01
```

## Финиш

Число blocking / non-blocking, три самые опасные проблемы, следующий шаг.
Остановись.

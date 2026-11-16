---
name: ci-stage-10-analytics-outcome
description: "Career Intelligence / AI Profession Intelligence, этап STAGE-10 — Analytics + outcome. Применять только после STAGE-02 и STAGE-08. Инструментирует по замороженному каталогу событий, считает cost per verified outcome и time-to-first-value. Не оптимизировать под messages, prompts, AI calls, time in app, number of recommendations."
---

# STAGE-10 — Analytics + outcome

Полный источник шагов — `docs/ops/stages/STAGE-10-ANALYTICS-OUTCOME.md`.

## Перед стартом

- [ ] Заморожен `EVENT-CATALOG.md`.
- [ ] Завершён STAGE-08.

## Что измерять

acquisition, activation, time_to_first_value, recommendation acceptance,
implementation start, implementation completion, verification, outcome,
retention, paid conversion, referral.

Отдельно: recommendation quality, unsupported claims, policy blocks,
tool failures, LLM cost, LLM latency, RAG quality, human escalation.

## Запрещено оптимизировать под

messages, prompts, AI calls, time in app, number of recommendations.

## Главное

North-star метрика привязана к customer outcome, а не к активности.
События — только из замороженного каталога, ничего не переопределять.

## Выходы

Event instrumentation, dashboard-ready analytics, outcome funnel,
cost per verified outcome, unit economics snapshot.

## Контроль

```bash
python tools/runbook_validate.py --stage STAGE-10
```

## Финиш

Дашборд и первые числа. Остановись.

# STAGE-10 — Analytics + outcome

> Бывший PROMPT 10. Инструментирует по каталогу событий, замороженному в
> STAGE-02, а не определяет события заново после того, как код уже написан.

## Назначение

Реализовать measurement layer, где главная метрика связана с customer outcome.

## Trigger

Завершены STAGE-02 и STAGE-08.

## Inputs

- `23_ANALYTICS_PRODUCT_METRICS_SPEC.md`
- `31_OUTCOME_ROI_ENGINE_SPEC.md`
- `24_EVALUATION_AND_BENCHMARKS_SPEC.md`
- `18_ANALYTICS_EVALS_SPEC.md`
- `docs/contracts/events/EVENT-CATALOG.md`

## Что измеряем

acquisition, activation, time_to_first_value, recommendation acceptance,
implementation start, implementation completion, verification, outcome,
retention, paid conversion, referral.

Отдельно: recommendation quality, unsupported claims, policy blocks,
tool failures, LLM cost, LLM latency, RAG quality, human escalation.

## Не оптимизировать под

messages, prompts, AI calls, time in app, number of recommendations.

## Outputs

- Event instrumentation
- Dashboard-ready analytics
- Outcome funnel
- Cost per verified outcome
- Unit economics snapshot

## Definition of Done

- [ ] Все метрики считаются из событий замороженного каталога.
- [ ] North-star метрика привязана к outcome, а не к активности.
- [ ] Есть возможность разрезать метрики по ICP, стране, языку, seniority.
- [ ] Recommendation quality измеряется отдельно от бизнес-метрик.
- [ ] Cost per verified outcome считается.
- [ ] Human escalation rate виден.
- [ ] Нет метрик, которые поощряют ненужные AI-вызовы.

## HARD STOP

Показать дашборд и первые числа. Ждать человека.

## Rollback

Telemetry отключается флагом; данные аналитики не удаляются без команды.

## Промпт для IDE

```text
Этап STAGE-10 — analytics + outcome measurement.

Основывайся на:
- career-intelligence-research-specs-v02/23_ANALYTICS_PRODUCT_METRICS_SPEC.md
- career-intelligence-research-specs-v02/31_OUTCOME_ROI_ENGINE_SPEC.md
- career-intelligence-research-specs-v02/24_EVALUATION_AND_BENCHMARKS_SPEC.md
- career-intelligence-research-specs-v02/18_ANALYTICS_EVALS_SPEC.md
- docs/contracts/events/EVENT-CATALOG.md

Измеряй: acquisition, activation, time_to_first_value, recommendation acceptance,
implementation start, implementation completion, verification, outcome,
retention, paid conversion, referral.

Отдельно: recommendation quality, unsupported claims, policy blocks,
tool failures, LLM cost, LLM latency, RAG quality, human escalation.

Главная метрика связана с customer outcome.
Не оптимизируй под messages, prompts, AI calls, time in app,
number of recommendations.

События бери только из замороженного каталога, ничего не переопределяй.
Добавь event contracts и dashboard-ready analytics.

В конце заполни docs/ops/STAGE-STATUS.md и остановись.
```

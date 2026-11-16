# STAGE-17 — SEO + growth

> Бывший PROMPT 16. Масштабирование SEO — после P0. Минимальная дистрибуция
> (10–30 страниц) уже сделана в STAGE-08A.

## Назначение

Превратить контент в систему роста, связанную с реальными WorkRecipes.

## Trigger

Release gate P1 пройден.

## Inputs

- `19_SEO_PROGRAMMATIC_SPEC.md`
- `20_CONTENT_ENGINE_SPEC.md`
- `18_GROWTH_MARKETING_SPEC.md`
- `23_ANALYTICS_PRODUCT_METRICS_SPEC.md`
- `PILOT_DECISION.md` — страна и язык

## SEO graph

profession → task → problem → solution → tool → workflow → learning →
implementation → case → outcome.

## Правила

- Не создавать thin programmatic pages.
- Каждая generated page имеет unique value, structured data, evidence,
  clear intent, internal links, freshness, canonicalization, conversion path.
- Не создавать SEO-контент, который продукт не может подтвердить.
- Связать SEO-страницы с реальными WorkRecipes.

## Outputs

- SEO information architecture
- Keyword/entity map
- Programmatic page schema
- Content pipeline
- Internal linking rules
- Analytics
- Indexation monitoring

## Definition of Done

- [ ] Каталог генерируемых страниц имеет чёткий intent и шаблон.
- [ ] Каждая страница связана с WorkRecipe.
- [ ] Structured data и canonical URL на месте.
- [ ] Индексация и трафик мониторятся.
- [ ] Thin-контент отсутствует.

## HARD STOP

Показать информационную архитектуру, первые страницы, метрики индексации. Ждать человека.

## Rollback

`noindex` на тирах, остановка pipeline. Контент не удаляется.

## Промпт для IDE

```text
Этап STAGE-17 — SEO и marketing (после core product).

Основывайся на:
- career-intelligence-research-specs-v02/19_SEO_PROGRAMMATIC_SPEC.md
- career-intelligence-research-specs-v02/20_CONTENT_ENGINE_SPEC.md
- career-intelligence-research-specs-v02/18_GROWTH_MARKETING_SPEC.md
- career-intelligence-research-specs-v02/23_ANALYTICS_PRODUCT_METRICS_SPEC.md

SEO graph: profession → task → problem → solution → tool → workflow →
learning → implementation → case → outcome.

Не создавать thin programmatic pages.
Каждая generated page: unique value, structured data, evidence, clear intent,
internal links, freshness, canonicalization, conversion path.

Создай: SEO information architecture, keyword/entity map, programmatic page
schema, content pipeline, internal linking rules, analytics,
indexation monitoring.

Свяжи SEO pages с реальными WorkRecipes.
Не создавать SEO-контент, который продукт не может подтвердить.
```

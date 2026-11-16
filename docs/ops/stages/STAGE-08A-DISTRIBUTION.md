# STAGE-08A — Distribution MVP

> Новый этап, вынесенный из PROMPT 16 в P0. Причина: `44_MASTER_ROADMAP_P0_P2.md`
> пункты 6–7 и `TASK-P0-008` требуют публикации страниц и запуска
> acquisition-эксперимента внутри P0. Без дистрибуции P0 gate не на ком
> проверять — вертикальный срез собран, а пользователей нет.

## Назначение

Дать P0 минимальную дистрибуцию: лендинг, 10–30 качественных страниц
профессия/задача и один acquisition-канал.

## Trigger

Завершён STAGE-08.

## Inputs

- `19_SEO_PROGRAMMATIC_SPEC.md`
- `20_CONTENT_ENGINE_SPEC.md`
- `18_GROWTH_MARKETING_SPEC.md`
- `23_ANALYTICS_PRODUCT_METRICS_SPEC.md`
- `PILOT_DECISION.md` — страна и язык
- `docs/contracts/events/EVENT-CATALOG.md`

## Шаги

1. Лендинг пилота с ясным offer и CTA.
2. Информационная архитектура SEO: 10–30 страниц по схеме
   профессия → задача → проблема → решение → инструмент → workflow → learning →
   implementation → case → outcome.
3. Каждая страница связана с реальной WorkRecipe в продукте.
4. Один acquisition-канал: органика, сообщества или точечный outreach —
   выбрать по `PILOT_DECISION.md`.
5. Аналитика канала по каноническим событиям.

## Правила

- Не создавать thin programmatic pages.
- Каждая страница имеет unique value, structured data, evidence, clear intent,
  internal links, freshness, canonicalization, conversion path.
- Не создавать SEO-контент, который продукт не может подтвердить.
- Не обещать то, чего WorkRecipe не покрывает.

## Outputs

- Лендинг
- 10–30 страниц
- Keyword/entity map
- Programmatic page schema
- Internal linking rules
- Analytics по каналу

## Definition of Done

- [ ] Хотя бы 10 страниц опубликованы и связаны с WorkRecipe.
- [ ] У каждой страницы есть structured data и canonical URL.
- [ ] Есть выбранный канал и первые запущенные эксперименты.
- [ ] Источники трафика измеряются.
- [ ] Ни одной thin-страницы без уникальной ценности.

## HARD STOP

Показать: число страниц, канал, первые метрики трафика, конверсия в регистрацию.
Ждать человека.

## Rollback

Снять страницы с индексации (`noindex`), отключить канал. Контент не удалять
без команды — он может быть переиспользован.

## Промпт для IDE

```text
Этап STAGE-08A — distribution MVP.

Без дистрибуции P0 gate не на ком проверять.

Основывайся на:
- career-intelligence-research-specs-v02/19_SEO_PROGRAMMATIC_SPEC.md
- career-intelligence-research-specs-v02/20_CONTENT_ENGINE_SPEC.md
- career-intelligence-research-specs-v02/18_GROWTH_MARKETING_SPEC.md
- career-intelligence-research-specs-v02/23_ANALYTICS_PRODUCT_METRICS_SPEC.md
- docs/architecture/PILOT_DECISION.md

Задача:
1. Лендинг пилота с ясным offer и CTA.
2. 10–30 качественных страниц по схеме: профессия → задача → проблема →
   решение → инструмент → workflow → learning → implementation → case → outcome.
3. Каждая страница связана с реальной WorkRecipe.
4. Один acquisition-канал по выбору owner'а.
5. Аналитика канала по каноническим событиям.

Не создавать thin programmatic pages.
У каждой страницы: unique value, structured data, evidence, clear intent,
internal links, freshness, canonicalization, conversion path.
Не создавать SEO-контент, который продукт не может подтвердить.

В конце заполни docs/ops/STAGE-STATUS.md и остановись.
```

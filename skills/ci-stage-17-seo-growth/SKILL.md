---
name: ci-stage-17-seo-growth
description: "Career Intelligence / AI Profession Intelligence, этап STAGE-17 — SEO + growth. Только после release gate P1. SEO graph profession→task→problem→solution→tool→workflow→learning→implementation→case→outcome, programmatic page schema, content pipeline, internal linking, indexation monitoring. Thin pages и неподтверждённый контент запрещены."
---

# STAGE-17 — SEO + growth

Полный источник шагов — `docs/ops/stages/STAGE-17-SEO-GROWTH.md`.

## Условие

Release gate P1 пройден. Минимальная дистрибуция уже сделана в STAGE-08A.

## SEO graph

```
profession → task → problem → solution → tool → workflow
→ learning → implementation → case → outcome
```

## Правила

- Не создавать thin programmatic pages.
- У каждой страницы: unique value, structured data, evidence, clear intent,
  internal links, freshness, canonicalization, conversion path.
- Не создавать SEO-контент, который продукт не может подтвердить.
- Связать страницы с реальными WorkRecipes.

## Выходы

SEO information architecture, keyword/entity map, programmatic page schema,
content pipeline, internal linking rules, analytics, indexation monitoring.

## Контроль

```bash
python tools/runbook_validate.py --stage STAGE-17
```

## Финиш

Информационная архитектура, первые страницы, метрики индексации. Остановись.

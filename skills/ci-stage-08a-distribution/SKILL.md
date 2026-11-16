---
name: ci-stage-08a-distribution
description: "Career Intelligence / AI Profession Intelligence, этап STAGE-08A — Distribution MVP. Применять только после STAGE-08. Лендинг, 10–30 качественных страниц по схеме профессия→задача→проблема→решение→инструмент→workflow, один acquisition-канал. Без дистрибуции P0 gate не на ком проверять. Thin programmatic pages запрещены."
---

# STAGE-08A — Distribution MVP

Полный источник шагов — `docs/ops/stages/STAGE-08A-DISTRIBUTION.md`.

## Зачем

`TASK-P0-008` требует acquisition-эксперимента внутри P0. Без него
P0 gate невозможно пройти: вертикальный срез собран, а проверять не на ком.

## Состав

1. Лендинг пилота с ясным offer и CTA.
2. 10–30 страниц по схеме: профессия → задача → проблема → решение →
   инструмент → workflow → learning → implementation → case → outcome.
3. Каждая страница связана с реальной WorkRecipe.
4. Один acquisition-канал по выбору owner'а.
5. Аналитика канала по каноническим событиям.

## Запрещено

Thin programmatic pages. SEO-контент, который продукт не может подтвердить.
Обещания, не покрытые WorkRecipe.

## У каждой страницы

unique value, structured data, evidence, clear intent, internal links,
freshness, canonicalization, conversion path.

## Контроль

```bash
python tools/runbook_validate.py --stage STAGE-08A
```

## Финиш

Число страниц, канал, первые метрики трафика, конверсия в регистрацию.
Остановись.

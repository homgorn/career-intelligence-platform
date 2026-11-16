---
doc_type: strategy
status: PROPOSED (license split REJECTED 2026-11-16 per ADR-0002)
author: architecture
date: 2026-11-16
decision_required_by: owner (pricing, API tiers, operator)
---

# Monetization strategy — PROPOSAL

Статус: **PROPOSAL, не решение.** Требуется выбор владельца и, по
необходимости, ADR. Часть позиций юридически значима и не принимается
внутри IDE.

## Принцип

Репозиторий содержит **исполняемую спецификацию и систему исполнения**
(runbook, валидаторы, скиллы). Продукт (Career Intelligence /
AI Profession Intelligence) — это приложение и данные, которые ещё не
выпущены. Монетизация строится вокруг разницы между ними:

```
open repo (этот репозиторий)          proprietary SaaS / API
─────────────────────────────        ──────────────────────────────
specs, process, tooling, data model   recipes, outcomes, verification
validator, selector, skills           engine, ranking, policy packs
architecture, roadmap                 execution telemetry, live ROI
```

## Варианты «ограничения» репозитория

### Вар-1 (отменён): License split (open core)

Владелец отменил BUSL (2026-11-16, `ADR-0002` REJECTED). Разделение по путям
отменено: репозиторий остаётся единой MIT, включая гипотетический `engine/`.
Ограничение лицензии как инструмент монетизации вычеркнуто из роадмапа.

### Вар-2. Thin open repo, deep proprietary control plane

- Репозиторий оставить полным и MIT, но продукт реализовать как закрытое
  отдельное приложение; репо = форр + документация + пайплайн.
- Эффект: бренд и экспертность, ноль защиты кода.
- Цена: любой может скопировать и развернуть.

### Вар-3. Open core + premium API (платные ключи, metering)

- Открытый монослой в репозитории, платный доступ к **исполнению**:
  вызов рекомендательного движка, RAG-прогоны, верификация исхода,
  metered через API-ключи.
- Модель: free tier (100 вызовов/мес), Growth, Team, Enterprise.
- Биллинг: entitlements как policy objects — уже зафиксировано в архиве
  (`39_BILLING_ENTITLEMENT_SPEC.md`, `22_BILLING_MONETIZATION_SPEC.md`).
- Цена: нужна инфраструктура, поддержка, SLA, metering, reconciliation.

### Вар-4. Community edition + hosted Premium/Enterprise

- Community: on-prem, ничего кроме runbook'а и демо-данных.
- Hosted: recipes, outcomes, jobs, guaranteed ROI verification, BI.
- Enterprise: SSO, SCIM, DPA, audit, private model routing.

### Вар-5. API-as-a-product + docs bot

- В API: `/recommend`, `/recipes`, `/verify` на базе WorkRecipe; платно
  по вызову + сниженные тарифы на объём; бесплатный rate limit для бота.
- Подходит стеку Cloudflare/DeepSeek/каталог open models.

## Рекомендуемая связка

1. **License**: не ограничивается. Единая MIT. Любая монетизация строится
   на ценности исполнения (data, verified outcomes, поддержка), а не на
   запретах. Лицензионный инструмент в роадмапе вычеркнут.
2. **Open gates**: оставить валидатор и skill-карточки открытыми; закрытыми
   могут стать отдельные коммерческие артефакты (например, каталог
   проверенных рецептов или outcome-верификация как сервис).
3. **Монетизация API**: metered доступ к API `/recommend`, `/recipes`,
   `/verify`; бесплатный уровень — docs-бот + ограниченный trial. Пересматривается
   на каждом gate.
4. **Продажи**: B2C-пример в этом репо, B2B outcome-report через partner program.

## Не делать

- Не начинать монетизацию до P0 gate.
- Не делать paywall на документации и процессе — это уничтожает главный актив.
- Не продавать результат, который не измеряем: без verified outcome нет продукта.

## Следующее решение владельца

- [ ] Стоимость API tiers (сколько и за что)
- [ ] SLA/поддержка первого платного уровня
- [ ] Фискальный оператор (payments): Stripe / Cloudflare / локальный

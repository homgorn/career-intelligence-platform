---
doc_type: strategy
status: PROPOSED
author: architecture
date: 2026-11-16
decision_required_by: owner
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

### Вар-1. License split (open core) — рекомендация

Разделение по путям, а не по файлам задним числом:

| Артефакт | Лицензия | Когда |
| --- | --- | --- |
| Pre-BUSL (этот коммит и раньше) | MIT / CC BY для docs | неизменяемо |
| Engine major versions (после принятия ADR-0002) | BUSL 1.1 | 4 года → Apache-2.0 |
| Docs / skills / tools / CI | MIT / CC BY | бессрочно |

- Сейчас: MIT на всё.
- Предложение: перенести на BUSL 1.1 / BSL со сроком конвертации в Apache/MIT,
  и опубликовать **ядро решения** закрыто в продукт.
- Эффект: репозиторий показывает экспертизу, но запрещает конкурирующий
  hosted-SaaS без коммерческой лицензии.
- Цена юридическая: смена лицензии публичного репозитория = новый «лист»
  для новых контрибьюторов; нужны согласия или CLA; старые коммиты остаются MIT.

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

1. **License**: BUSL на код движка (не на документы — они остаются открытыми).
   Готовлю `ADR-0002-license-busl.md` (PROPOSED): двойная лицензия MIT для
   docs/skills/tools/CI и BUSL 1.1 для будущего `engine/`. Принятие требует
   legal review и подписи владельца.
2. **Open gates**: оставить валидатор и skill-карточки; закрыть
   `engine/`, `policy-packs/`, `recipes/live/` и live-API.
3. **Монетизация API**: metered доступ к engine; бесплатный уровень —
   1 прогон WorkRecipe в месяц + docs бот. Пересмотрена на каждом gate.
4. **Продажи**: B2C-пример в этом репо, B2B outcome-report через partner program.

## Не делать

- Не начинать монетизацию до P0 gate.
- Не делать paywall на документации и процессе — это уничтожает главный актив.
- Не продавать результат, который не измеряем: без verified outcome нет продукта.

## Следующее решение владельца

- [ ] Лицензионная модель (MIT остаётся / BUSL на engine / закрытый core)
- [ ] Стоимость API tiers (сколько и за что)
- [ ] SLA/поддержка первого платного уровня
- [ ] Фискальный оператор (payments): Stripe / Cloudflare / локальный

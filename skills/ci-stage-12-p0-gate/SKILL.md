---
name: ci-stage-12-p0-gate
description: "Career Intelligence / AI Profession Intelligence, этап STAGE-12 — P0 value gate. Применять только после STAGE-11 и implementation review STAGE-09. Сравнивает измеренное с порогами из PILOT_DECISION.md по областям CUSTOMER VALUE, PRODUCT, ENGINEERING, AI, SECURITY, LEGAL, ECONOMICS. Вердикты PASS / CONDITIONAL_PASS / FAIL. Если P0 не доказан — P1 не предлагается."
---

# STAGE-12 — P0 value gate

Полный источник шагов — `docs/ops/stages/STAGE-12-P0-GATE.md`.

## Суть

Проверяй не наличие функций, а доказательство customer value.

## Пороги

Берутся из `PILOT_DECISION.md`, заданные человеком до старта P0.
Рекомендуемый минимум:

| Показатель | Порог |
| --- | --- |
| Реальные пользователи | ≥ 20, не сотрудники |
| Time-to-first-value | ≤ 15 мин медианно |
| Завершили действие из WorkRecipe | ≥ 30% |
| Записали outcome за 14 дней | ≥ 10% |
| Blocker security/privacy | 0 |
| Provenance и policy version | 100% |
| Cost per verified outcome | по цели из PILOT_DECISION |

## Вердикты

- **PASS** — все пороги выполнены.
- **CONDITIONAL_PASS** — один порог не выполнен, есть план и срок.
- **FAIL** — outcome не доказан или есть нерешённый legal/security blocker.

Обязательно ответь: «Может ли реальный пользователь получить измеримую пользу
без участия разработчика?» Нет → FAIL независимо от остального.

## Выход

`docs/gates/RELEASE-GATE-P0.md` + список исправлений с владельцами.

## Контроль

```bash
python tools/runbook_validate.py --stage STAGE-12
```

## Финиш

Не предлагай строить P1, если P0 не доказан. Остановись.

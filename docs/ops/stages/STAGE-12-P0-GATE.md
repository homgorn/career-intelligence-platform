# STAGE-12 — P0 value gate

> Бывший PROMPT 12, количественно определённый. PASS / CONDITIONAL_PASS / FAIL
> без порогов непроверяемы, поэтому пороги берутся из `PILOT_DECISION.md`,
> заданные человеком ещё до старта P0.

## Назначение

Проверить не наличие функций, а доказательство customer value.

## Trigger

Завершён STAGE-11 и implementation review STAGE-09.

## Inputs

- `PILOT_DECISION.md` — целевые пороги.
- `44_MASTER_ROADMAP_P0_P2.md`, `46_GATES_CHECKLIST.md`.
- Результаты STAGE-11, STAGE-09, STAGE-10.
- `49_DEFINITION_OF_DONE_GLOBAL.md`.

## Проверяемые области

CUSTOMER VALUE, PRODUCT, ENGINEERING, AI, SECURITY, LEGAL, ECONOMICS.

По каждой: STATUS, EVIDENCE, BLOCKERS, RISK, OWNER, NEXT ACTION.

### CUSTOMER VALUE

- Какая конкретная проблема решена?
- Для какого ICP?
- Какой baseline?
- Какой ожидаемый outcome?
- Каким способом outcome проверяется?

### PRODUCT

- Может ли пользователь пройти путь целиком?
- Time-to-first-value?
- Friction?
- Trust?

### ENGINEERING

Архитектурные границы, тесты, миграции, rollback, observability.

### AI

Evidence, model traceability, hallucination controls, evaluation, human review.

### SECURITY

Tenant isolation, PII, tool permissions, prompt injection.

### LEGAL

Нерешённые вопросы юрисдикции, consent, deletion, AI disclosure.

### ECONOMICS

Expected cost per outcome, expected support burden.

## Пороги PASS

Конкретные числа задаёт owner в `PILOT_DECISION.md`. Рекомендуемый минимум
для первого пилота:

| Показатель | Порог |
| --- | --- |
| Реальные пользователи, прошедшие цикл | ≥ 20, не сотрудники и не друзья |
| Time-to-first-value | ≤ 15 минут медианно |
| Завершили хотя бы одно действие из WorkRecipe | ≥ 30% |
| Вернулись записать outcome в течение 14 дней | ≥ 10% |
| Blocker security / privacy findings | 0 нерешённых |
| Provenance и policy version | 100% рекомендаций |
| Cost per verified outcome | не выше цели из PILOT_DECISION |

## Вердикты

- **PASS** — все пороги выполнены.
- **CONDITIONAL_PASS** — один порог не выполнен, но есть план и срок.
- **FAIL** — outcome не доказан или есть нерешённый legal/security blocker.

Отдельно обязательно ответить: «Может ли реальный пользователь получить
измеримую пользу без участия разработчика?» Если нет — FAIL независимо
от остального.

## Outputs

- `docs/gates/RELEASE-GATE-P0.md`
- Список исправлений с владельцами, если gate не PASS

## Definition of Done

- [ ] Есть вердикт по каждой из семи областей.
- [ ] Числа сравнены с порогами из `PILOT_DECISION.md`.
- [ ] Нет ни одного «принято молча».
- [ ] Если P0 не доказан — есть конкретный список исправлений и P1 не предлагается.

## HARD STOP

Если P0 не доказан — не предлагать строить P1. Ждать решения человека.

## Rollback

Gate пересматривается новой версией отчёта. Предыдущая версия помечается
`superseded`, но не удаляется.

## Промпт для IDE

```text
Этап STAGE-12 — P0 value gate.

Остановись и проведи gate. Проверяй не наличие функций,
а доказательство customer value.

Прочитай:
- docs/architecture/PILOT_DECISION.md
- career-intelligence-research-specs-v02/44_MASTER_ROADMAP_P0_P2.md
- career-intelligence-research-specs-v02/46_GATES_CHECKLIST.md
- docs/gates/SECURITY_GATE.md
- docs/gates/PRIVACY_GATE.md
- docs/gates/LEGAL_GATE.md
- результаты STAGE-11

Проверь: CUSTOMER VALUE, PRODUCT, ENGINEERING, AI, SECURITY, LEGAL, ECONOMICS.
По каждой: STATUS, EVIDENCE, BLOCKERS, RISK, OWNER, NEXT ACTION.

Сравни измеренные значения с порогами из PILOT_DECISION.md.
Ответь письменно: "Может ли реальный пользователь получить измеримую пользу
без участия разработчика?" Если нет — FAIL независимо от остального.

OUTPUT:
P0_STATUS: PASS / CONDITIONAL_PASS / FAIL
BLOCKERS: ...
EVIDENCE: ...
UNKNOWN: ...
NEXT DECISION: ...

Если P0 не доказан — НЕ предлагай строить P1.
Сформируй конкретный список исправлений.

Создай docs/gates/RELEASE-GATE-P0.md.
В конце заполни docs/ops/STAGE-STATUS.md и остановись.
```

# GATE REPORT — <название gate>

Универсальный шаблон для stage gate, release gate и production gate.

## Метаданные

- Gate: `STAGE-GATE-XX` | `RELEASE-GATE-P0|P1|P2` | `PRODUCTION-GATE`
- Дата:
- Проводит: IDE готовит, человек решает
- Предыдущий gate:
- Пороги из `PILOT_DECISION.md`:

## Результат

```
STATUS: PASS | CONDITIONAL_PASS | FAIL
```

## Области

### CUSTOMER VALUE

STATUS / EVIDENCE / BASELINE / EXPECTED OUTCOME / HOW VERIFIED /
BLOCKERS / RISK / OWNER / NEXT ACTION

### PRODUCT

STATUS / EVIDENCE / CAN_USER_COMPLETE_JOURNEY / TIME_TO_FIRST_VALUE /
FRICTION / TRUST / BLOCKERS / RISK / OWNER / NEXT ACTION

### ENGINEERING

STATUS / EVIDENCE / ARCHITECTURE_BOUNDARIES / TESTS / MIGRATIONS /
ROLLBACK / OBSERVABILITY / BLOCKERS / RISK / OWNER / NEXT ACTION

### AI

STATUS / EVIDENCE / MODEL_TRACEABILITY / HALLUCINATION_CONTROLS /
EVALUATION / HUMAN_REVIEW / BLOCKERS / RISK / OWNER / NEXT ACTION

### SECURITY

STATUS / EVIDENCE / TENANT_ISOLATION / PII / TOOL_PERMISSIONS /
PROMPT_INJECTION / BLOCKERS / RISK / OWNER / NEXT ACTION

### LEGAL

STATUS / EVIDENCE / JURISDICTION_ISSUES / CONSENT / DELETION /
AI_DISCLOSURE / BLOCKERS / RISK / OWNER / NEXT ACTION

### ECONOMICS

STATUS / EVIDENCE / COST_PER_OUTCOME / SUPPORT_BURDEN /
BLOCKERS / RISK / OWNER / NEXT ACTION

## Сводка по порогам

| Показатель | Порог | Факт | Вердикт |
| --- | --- | --- | --- |
| Реальные пользователи | ≥ 20 | | |
| Time-to-first-value | ≤ 15 мин | | |
| Завершили действие | ≥ 30% | | |
| Записали outcome за 14 дней | ≥ 10% | | |
| Blocker security/privacy | 0 | | |
| Provenance и policy version | 100% | | |
| Cost per verified outcome | по цели | | |

## Главный вопрос

«Может ли реальный пользователь получить измеримую пользу без участия
разработчика?» — Да / Нет.

Если нет — FAIL независимо от остального.

## BLOCKERS

| # | Finding | Severity | Owner | Due | Status |
| --- | --- | --- | --- | --- | --- |

## UNKNOWN

Что не удалось проверить и почему.

## NEXT DECISION

Что решает человек после этого gate.

## Список исправлений

Конкретные пункты с owner и сроком. Без общих рекомендаций.

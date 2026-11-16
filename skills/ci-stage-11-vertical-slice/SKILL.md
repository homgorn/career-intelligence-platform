---
name: ci-stage-11-vertical-slice
description: "Career Intelligence / AI Profession Intelligence, этап STAGE-11 — Vertical slice E2E. Применять только после STAGE-05, STAGE-08, STAGE-10. Собирает один полный сквозной сценарий USER→AUTH→PROFILE→GOAL→TASK→WORKFLOW→DIAGNOSIS→OPTIONS→POLICY GATES→RECOMMENDATION→WORK RECIPE→IMPLEMENTATION→VERIFICATION→OUTCOME→ANALYTICS. 13 обязательных доказательств E2E. Mock, обходящий домен, запрещён."
---

# STAGE-11 — Vertical slice E2E

Полный источник шагов — `docs/ops/stages/STAGE-11-VERTICAL-SLICE.md`.

## Путь

```
USER → AUTH → PROFILE → GOAL → TASK → WORKFLOW → DIAGNOSIS → CANDIDATE OPTIONS
→ POLICY GATES → RECOMMENDATION → WORK RECIPE → IMPLEMENTATION → VERIFICATION
→ OUTCOME → ANALYTICS
```

Реальные production-like контракты. Stub external provider — только
через adapter. Mock, обходящий доменную архитектуру, запрещён.

## E2E должен доказать

1. Пользователь создаётся.
2. Профиль сохраняется.
3. Goal создаётся.
4. Task определяется.
5. Recommendation формируется.
6. Recommendation имеет evidence.
7. Policy gate срабатывает.
8. `consent.granted` фиксируется.
9. WorkRecipe создаётся.
10. Implementation фиксируется.
11. Outcome записывается.
12. Analytics event создаётся.
13. Audit trail существует.

Проверь также цепочку `recommendation.generated → recommendation.accepted`
и `tool.verified`.

## Контроль

```bash
python tools/runbook_validate.py --stage STAGE-11
```

## Финиш

Прогон E2E, цепочка событий, найденные разрывы. Остановись.

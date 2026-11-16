# STAGE-19 — Production readiness

> Бывший PROMPT 18. Финальный аудит перед выпуском. Не выпускать продукт,
> пока этот gate не пройден.

## Назначение

Проверить весь проект по слоям и ответить на главный вопрос: может ли
реальный пользователь получить измеримую пользу без участия разработчика.

## Trigger

Release gate P2 пройден или человек дал команду на финальный аудит.

## Inputs

- Все артефакты предыдущих этапов
- `49_DEFINITION_OF_DONE_GLOBAL.md`
- `46_GATES_CHECKLIST.md`
- `41_TESTING_QA_SPEC.md`, `40_DEVOPS_SRE_SPEC.md`, `42_OBSERVABILITY_SPEC.md`
- `11_SECURITY_ARCHITECTURE_SPEC.md`, `12_LEGAL_COMPLIANCE_SPEC.md`,
  `13_PRIVACY_DATA_SUBJECT_SPEC.md`

## Слои

1. CUSTOMER VALUE
2. PRODUCT
3. UX
4. DOMAIN
5. DATABASE
6. API
7. EVENTS
8. SDD ENGINE
9. RULE ENGINE
10. GATES
11. ADAPTERS
12. LLM
13. RAG
14. WIKI
15. KNOWLEDGE GRAPH
16. SECURITY
17. PRIVACY
18. LEGAL
19. BILLING
20. ANALYTICS
21. EVALUATION
22. OBSERVABILITY
23. TESTING
24. DEVOPS
25. SEO
26. CONTENT
27. GROWTH
28. B2C
29. B2B
30. SUPPORT
31. OPERATIONS

По каждому: STATUS, EVIDENCE, BLOCKERS, RISK, OWNER, NEXT ACTION.

## Главный вопрос

«Может ли реальный пользователь получить измеримую пользу без участия
разработчика?» Если нет — production readiness FAIL.

## Outputs

- `docs/gates/PRODUCTION-GATE.md`
- P0/P1/P2 STATUS
- RELEASE DECISION
- BLOCKERS
- POST-RELEASE PLAN

## Definition of Done

- [ ] Все 31 слой имеют вердикт.
- [ ] У каждого blocker есть owner и срок.
- [ ] Юридические вопросы либо закрыты, либо вынесены на counsel.
- [ ] Backup/recovery и rollback проверены.
- [ ] Мониторинг и алерты настроены.
- [ ] Support/runbook существует.
- [ ] Есть post-release plan.

## HARD STOP

Не выпускать продукт. Ждать решения человека.

## Rollback

Отзыв релиза, откат к предыдущей версии, отключение фич флагами.

## Промпт для IDE

```text
Этап STAGE-19 — production readiness gate.

Не выпускай продукт. Проведи Production Readiness Gate.

Проверь весь проект по слоям: CUSTOMER VALUE, PRODUCT, UX, DOMAIN, DATABASE,
API, EVENTS, SDD ENGINE, RULE ENGINE, GATES, ADAPTERS, LLM, RAG, WIKI,
KNOWLEDGE GRAPH, SECURITY, PRIVACY, LEGAL, BILLING, ANALYTICS, EVALUATION,
OBSERVABILITY, TESTING, DEVOPS, SEO, CONTENT, GROWTH, B2C, B2B, SUPPORT,
OPERATIONS.

Для каждого: STATUS, EVIDENCE, BLOCKERS, RISK, OWNER, NEXT ACTION.

Особенно ответь: "Может ли реальный пользователь получить измеримую пользу
без участия разработчика?" Если нет — production readiness FAIL.

Затем: P0/P1/P2 STATUS, RELEASE DECISION, BLOCKERS, POST-RELEASE PLAN.

Создай docs/gates/PRODUCTION-GATE.md.
В конце заполни docs/ops/STAGE-STATUS.md и остановись.
```

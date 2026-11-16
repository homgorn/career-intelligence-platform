# STAGE-01 — Architecture readiness review

> Бывший PROMPT 01. Добавлена проверка самосогласованности архива, которой
> не было среди исходных 24 пунктов.

## Назначение

Проверить готовность архитектуры к реализации и дать список blocking и
non-blocking проблем. Код не пишется.

## Trigger

Завершён STAGE-00. Желательно — подписан `PILOT_DECISION.md`; без него часть
проблем помечается `BLOCKED_ON_PILOT`.

## Inputs

- Артефакты STAGE-00.
- Спеки по списку ниже — только соответствующие разделы.

## Проверяемые области

1. Domain model
2. Data model
3. API contracts
4. Event contracts
5. Policy engine
6. Gates
7. Adapter boundaries
8. LLM boundaries
9. RAG
10. Knowledge Graph
11. Security
12. Privacy
13. Legal
14. Billing
15. Analytics
16. Multi-tenancy
17. Observability
18. Testing
19. DevOps
20. Website
21. B2C
22. B2B
23. WorkRecipe
24. Outcome measurement
25. **Самосогласованность архива** (новый пункт): конфликтующие спеки,
   три модели данных, дублирующиеся новичковые и evaluation-спеки.

## Обязательные проверки

- LLM не является source of truth.
- LLM не принимает security / legal / billing решения.
- Vendor SDK не проникают в domain layer.
- Индексы — производные от authoritative data.
- У recommendation есть provenance.
- У policy decision есть version.
- Tenant isolation проверяется автоматически.
- Sensitive data не попадает без необходимости в logs / events / model context.
- Необратимые agent actions требуют approval.
- Customer value может быть измерена.
- Конфликтующие спеки разрешены или явно помечены `BLOCKED_ON_QUESTION`.

## Outputs

- `docs/architecture/ARCHITECTURE_READINESS_REVIEW.md`
- Список blocking issues
- Список non-blocking issues

## Definition of Done

- [ ] Каждая из 25 областей имеет вердикт: `READY` / `GAP` / `N/A_P0`.
- [ ] У каждого gap есть: описание, влияние, предлагаемое исправление, владелец.
- [ ] Blocking issues отделены от non-blocking.
- [ ] Ни один blocking issue не «принят» молча.
- [ ] Если проблема архитектурная — предлагается правка спеки или ADR, а не обходной код.

## HARD STOP

Вывести сводку: количество blocking / non-blocking, самые опасные три,
следующий шаг. Заполнить `STAGE-STATUS.md`. Ждать человека.

## Rollback

Правки документов. Удаление отчёта + статус `PENDING`.

## Промпт для IDE

```text
Этап STAGE-01 — architecture readiness review.

Production code не пишется.

Прочитай артефакты STAGE-00 и docs/specs/SPEC_INDEX.md.
Проверь 25 областей по чек-листу в docs/ops/stages/STAGE-01-READINESS-REVIEW.md.

Особенно проверь:
- LLM не source of truth;
- LLM не принимает security/legal/billing решения;
- vendor SDK не проникают в domain layer;
- indexes производны от authoritative data;
- у recommendation есть provenance;
- у policy decision есть version;
- tenant isolation проверяется автоматически;
- sensitive data не попадает без необходимости в logs/events/model context;
- необратимые agent actions требуют approval;
- customer value измерима;
- конфликтующие спеки разрешены или помечены BLOCKED_ON_QUESTION.

Если обнаружена архитектурная проблема — сначала предложи правку спеки или ADR,
а не код.

Создай:
docs/architecture/ARCHITECTURE_READINESS_REVIEW.md
со списком blocking issues и списком non-blocking issues.

Ни один blocking issue нельзя просто "принять" молча.
В конце заполни docs/ops/STAGE-STATUS.md и остановись.
```

# STAGE-11 — Vertical slice E2E

> Бывший PROMPT 11. E2E-чеклист приведён к каноническим событиям из
> `03_EVENT_CONTRACTS_SPEC.md`: в исходном списке не было `policy.blocked`,
> `consent.granted`, `recommendation.accepted`, `tool.verified`.

## Назначение

Собрать первый полный P0 vertical slice: один конкретный customer journey
проходит через всю систему.

## Trigger

Завершены STAGE-05, STAGE-08, STAGE-10.

## Inputs

- Все контракты из STAGE-02.
- `44_MASTER_ROADMAP_P0_P2.md`.
- `49_DEFINITION_OF_DONE_GLOBAL.md`.

## Путь

```
USER → AUTH → PROFILE → GOAL → TASK → WORKFLOW → DIAGNOSIS → CANDIDATE OPTIONS
→ POLICY GATES → RECOMMENDATION → WORK RECIPE → IMPLEMENTATION → VERIFICATION
→ OUTCOME → ANALYTICS
```

Используй реальные production-like контракты. Не делай mock, который обходит
доменную архитектуру. Допускается stub external provider через adapter.

## E2E-тест должен доказать

1. Пользователь создаётся.
2. Профиль сохраняется.
3. Goal создаётся.
4. Task определяется.
5. Recommendation формируется.
6. Recommendation имеет evidence.
7. Policy gate срабатывает (`policy.blocked` или guardrails).
8. `consent.granted` фиксируется до внешних действий.
9. WorkRecipe создаётся.
10. Implementation фиксируется (`implementation.started` / `completed`).
11. Outcome записывается (`outcome.recorded`).
12. Analytics event создаётся.
13. Audit trail существует.

Дополнительно проверить: `recommendation.accepted` → `recommendation.generated`
корректная цепочка; `tool.verified` при использовании инструмента.

## Outputs

- E2E test suite
- Полный сквозной сценарий
- P0 Gate Report (черновик для STAGE-12)

## Definition of Done

- [ ] Все 13 пунктов E2E-теста зелёные.
- [ ] События соответствуют замороженному каталогу.
- [ ] Есть доказательство provenance у каждой recommendation в сценарии.
- [ ] Есть доказательство работы policy gate.
- [ ] Есть audit trail.
- [ ] Stub providers только через adapters.
- [ ] Mock, обходящий доменную архитектуру, отсутствует.

## HARD STOP

Показать прогон E2E, цепочку событий, найденные разрывы. Ждать человека.

## Rollback

Откат к предыдущей версии через feature flags. Данные сценария не удаляются —
они нужны для STAGE-12.

## Промпт для IDE

```text
Этап STAGE-11 — первый настоящий P0 vertical slice.

Собери один complete P0 vertical slice. Один конкретный customer journey
проходит через всю систему:

USER → AUTH → PROFILE → GOAL → TASK → WORKFLOW → DIAGNOSIS → CANDIDATE OPTIONS
→ POLICY GATES → RECOMMENDATION → WORK RECIPE → IMPLEMENTATION → VERIFICATION
→ OUTCOME → ANALYTICS

Используй реальные production-like контракты.
Не делай mock, который обходит domain architecture.
Допускается stub external provider через adapter.

E2E-тест должен доказать:
1. пользователь создаётся;
2. профиль сохраняется;
3. goal создаётся;
4. task определяется;
5. recommendation формируется;
6. recommendation имеет evidence;
7. policy gate срабатывает;
8. consent.granted фиксируется;
9. WorkRecipe создаётся;
10. implementation фиксируется;
11. outcome записывается;
12. analytics event создаётся;
13. audit trail существует.

После реализации выполни E2E test.
В конце заполни docs/ops/STAGE-STATUS.md и остановись.
```

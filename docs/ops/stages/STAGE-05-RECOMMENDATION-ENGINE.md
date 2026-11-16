# STAGE-05 — Recommendation engine

> Бывший PROMPT 05. Формула ранжирования приведена к канону из
> `29_WORK_RECIPE_SPEC.md`, чтобы не было двух разных формул.

## Назначение

Реализовать deterministic Recommendation Engine P0. LLM здесь не решает —
он может помогать с extraction / reasoning / proposal, но не является
единственным decision-maker.

## Trigger

Завершён STAGE-04.

## Inputs

- `01_SDD_ENGINE_SPEC.md` — pipeline и decision record
- `04_RULE_POLICY_ENGINE_SPEC.md` — ALLOW / DENY / ALLOW_WITH_GUARDRAILS /
  REQUIRE_HUMAN_REVIEW
- `05_GATES_AND_ADAPTERS_SPEC.md` — обязательные gates
- `29_WORK_RECIPE_SPEC.md` — solution types и формула ранжирования
- `31_OUTCOME_ROI_ENGINE_SPEC.md` — outcome и ROI
- `docs/contracts/domain/DATA-MODEL-P0.md`

## Pipeline

```
Context → Goal → Task → Workflow → Candidate interventions → Scoring
→ Policy gates → Recommendation → WorkRecipe → Verification
```

Типы вмешательства: `NON_AI`, `HUMAN`, `AI_AUGMENT`, `AI_AUTOMATION`, `AGENT`, `HYBRID`.

## Обязательно

AI не считается лучшим вариантом по умолчанию.

Scoring учитывает минимум: expected value, evidence confidence, feasibility,
implementation effort, risk, maintenance, user readiness.

Формула ранжирования — из `29_WORK_RECIPE_SPEC.md`:

```
score = expected_outcome × evidence_confidence × feasibility ÷ (cost × risk × friction)
```

Каждая recommendation хранит: reason, evidence, confidence, engine version,
policy results, alternatives, expected outcome, verification method.

Бизнес-правила — deterministic / typed. В промптах нет бизнес-логики.

## Outputs

- Scoring service
- Policy gate integration
- Recommendation → WorkRecipe generation
- Decision record (decision_id, engine_version, inputs_hash, candidate_set,
  scores, gate_results, selected_option, evidence_refs, timestamp, reviewer,
  outcome_status)
- Tests

## Обязательные тесты

- High-value AI решение.
- Low-value AI решение.
- Non-AI рекомендация выигрывает у AI.
- High-risk рекомендация блокируется или требует human review.
- Insufficient evidence.
- Low user readiness.

## Definition of Done

- [ ] Pipeline реализован полностью, все шаги логируются.
- [ ] Каждое решение сохраняет decision record с полным provenance.
- [ ] Policy gates — типизированные, с версией и reason codes.
- [ ] LLM не участвует в scoring и selection без явного обоснования.
- [ ] Все шесть обязательных тестов проходят.
- [ ] Есть тест «non-AI побеждает AI» — это ключевая проверка принципа.
- [ ] WorkRecipe создаётся только для выбранной recommended option.

## HARD STOP

Показать: покрытие тестами, пример decision record, число policy blocks,
примеры non-AI побед. Ждать человека.

## Rollback

Откат сервиса recommendation, возврат к предыдущей версии engine, отключение
фичи через feature flag. Никаких тихих изменений в scoring без ADR.

## Промпт для IDE

```text
Этап STAGE-05 — recommendation engine P0.

Основывайся строго на:
- career-intelligence-research-specs-v02/01_SDD_ENGINE_SPEC.md
- career-intelligence-research-specs-v02/04_RULE_POLICY_ENGINE_SPEC.md
- career-intelligence-research-specs-v02/05_GATES_AND_ADAPTERS_SPEC.md
- career-intelligence-research-specs-v02/29_WORK_RECIPE_SPEC.md
- career-intelligence-research-specs-v02/31_OUTCOME_ROI_ENGINE_SPEC.md
- docs/contracts/domain/DATA-MODEL-P0.md

Pipeline: Context → Goal → Task → Workflow → Candidate interventions →
Scoring → Policy gates → Recommendation → WorkRecipe → Verification.

Candidate intervention: NON_AI, HUMAN, AI_AUGMENT, AI_AUTOMATION, AGENT, HYBRID.

AI не должен автоматически считаться лучшим вариантом.

Scoring учитывает минимум: expected value, evidence confidence, feasibility,
implementation effort, risk, maintenance, user readiness.
Формула — из 29_WORK_RECIPE_SPEC: expected_outcome × evidence_confidence ×
feasibility ÷ (cost × risk × friction).

Каждая recommendation хранит: reason, evidence, confidence, engine version,
policy results, alternatives, expected outcome, verification method.

LLM не использовать как единственного decision-maker.
Бизнес-правила — deterministic/typed. Policy engine независим от LLM.

Напиши тесты для:
- high-value AI;
- low-value AI;
- non-AI recommendation выигрывает у AI;
- high-risk recommendation;
- insufficient evidence;
- low user readiness.

В конце заполни docs/ops/STAGE-STATUS.md и остановись.
```

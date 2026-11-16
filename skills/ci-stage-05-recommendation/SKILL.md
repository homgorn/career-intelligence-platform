---
name: ci-stage-05-recommendation
description: "Career Intelligence / AI Profession Intelligence, этап STAGE-05 — Recommendation engine. Применять только после STAGE-04. Deterministic scoring и policy gates, WorkRecipe generation, decision record с provenance. AI не считается лучшим вариантом по умолчанию, LLM не единственный decision-maker. Шесть обязательных тестов, включая non-AI побеждает AI."
---

# STAGE-05 — Recommendation engine

Полный источник шагов — `docs/ops/stages/STAGE-05-RECOMMENDATION-ENGINE.md`.

## Перед стартом

- [ ] Завершён STAGE-04.

## Pipeline

```
Context → Goal → Task → Workflow → Candidate interventions → Scoring
→ Policy gates → Recommendation → WorkRecipe → Verification
```

Типы: `NON_AI`, `HUMAN`, `AI_AUGMENT`, `AI_AUTOMATION`, `AGENT`, `HYBRID`.

## Формула ранжирования — из 29_WORK_RECIPE_SPEC.md

```
score = expected_outcome × evidence_confidence × feasibility ÷ (cost × risk × friction)
```

Scoring учитывает минимум: expected value, evidence confidence, feasibility,
implementation effort, risk, maintenance, user readiness.

## Decision record

decision_id, engine_version, inputs_hash, candidate_set, scores, gate_results,
selected_option, evidence_refs, timestamp, reviewer, outcome_status.

Policy gates — типизированные, с версией и reason codes:
ALLOW / DENY / ALLOW_WITH_GUARDRAILS / REQUIRE_HUMAN_REVIEW.

## Обязательные тесты

1. High-value AI.
2. Low-value AI.
3. Non-AI рекомендация выигрывает у AI.
4. High-risk recommendation.
5. Insufficient evidence.
6. Low user readiness.

## Контроль

```bash
python tools/runbook_validate.py --stage STAGE-05
```

## Финиш

Покройка тестами, пример decision record, число policy blocks, примеры
non-AI побед. Остановись.

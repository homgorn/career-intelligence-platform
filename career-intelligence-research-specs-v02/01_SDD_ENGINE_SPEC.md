# SDD engine specification

Software Design Description for the product's decision and execution engine. The engine turns evidence about a person, organization, task, and available capabilities into bounded recommendations and implementation plans.

## Inputs

User/tenant context; goal; occupation and task taxonomy; current workflow; constraints; tools; skills; evidence; market signals; policies; risk classification; budget; geography; language; historical outcomes.

## Pipeline

1. Normalize context.
2. Resolve entities.
3. Identify goal and success metric.
4. Map task/workflow.
5. Generate candidate interventions.
6. Score value, feasibility, risk, confidence.
7. Apply policy gates.
8. Select or rank options.
9. Generate implementation recipe.
10. Execute or hand off.
11. Verify result.
12. Record outcome and update evidence.

## Design contracts

Every engine component must expose: input schema, output schema, confidence, provenance, policy decisions, failure modes, latency/cost budget, and version.

## Determinism

Business rules, policy gates, entitlement, pricing, permissions, and safety decisions must not depend on unconstrained LLM prose. LLMs can propose; typed services decide.

## Decision record

Persist decision_id, engine_version, inputs_hash, candidate_set, scores, gate_results, selected_option, evidence_refs, model metadata, timestamp, reviewer, and outcome status.

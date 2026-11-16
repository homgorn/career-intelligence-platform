# AI Layer — Data Model Addendum

## Core entities
ProfessionTask, Workflow, WorkflowStep, AICapability, Tool, Connector, ToolPlan, LearningModule, SkillEvidence, ReadinessAssessment, AdoptionBarrier, ImplementationPackage, Provider, RiskAssessment, TestCase, EvaluationRun, OutcomeMeasurement, UserApproval, IntegrationCredentialReference.

## Key relationships
Profession → Task; Task → Workflow; Workflow → Step; Step → Capability; Capability → Tool; Tool → Connector; Workflow → Risk; Workflow → TestCase; Workflow → Outcome; Person → SkillEvidence; Person → ReadinessAssessment; Person → LearningPath; Person → ImplementationPackage.

## Provenance fields
source_uri, source_type, observed_at, checked_at, geography, language, author, reviewer, confidence, evidence_level, version, valid_from, valid_to.

## State fields
draft / reviewed / verified / pilot / production / deprecated / blocked.

## User-specific versus global
Keep personal task frequency and outcomes separate from generalized profession benchmarks. Aggregate only with appropriate consent and privacy controls.

## Avoid
- storing raw secrets in records;
- treating generated recommendations as verified facts;
- overwriting historical tool pricing;
- using one opaque "AI score" as the source of truth.

## Acceptance criteria
All recommendations can be traced to task, evidence, version, constraints and user context.

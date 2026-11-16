# Conceptual Domain Model

## Core entities
User, Profile, CareerGoal, Constraint, Preference, Experience, Education, Skill, SkillEvidence, Credential, Language, Location, Occupation, OccupationSpecialization, CareerPath, PathStep, MarketSnapshot, Job, JobMatch, LearningResource, Assessment, QuizResponse, Recommendation, RecommendationReason, Outcome, Source, TaxonomyVersion.

## Relationships
User → Profile
Profile → Experience / Skills / Credentials / Preferences / Constraints / Goals / Evidence
Occupation → Skills / Tasks / WorkContext / Credentials / Seniority / Market
Profile ↔ Occupation = CareerMatch
Occupation ↔ Occupation = CareerTransition
Occupation ↔ Skill = SkillRequirement
Profile ↔ Job = JobMatch
Profile → CareerPlan → Learning → Evidence → Recompute

## Evidence
User capability claims trace to evidence.
Occupation facts trace to sources.
Market claims trace to dated snapshots.

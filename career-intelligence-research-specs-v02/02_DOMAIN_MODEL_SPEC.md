# Domain model and bounded contexts

Canonical entities and ownership boundaries for a multi-tenant career/work/AI intelligence platform.

## Core entities

Person, Organization, Tenant, Goal, CareerProfile, AIProfile, Occupation, Skill, Task, Workflow, WorkRecipe, Tool, Plugin, Connector, Agent, LearningAsset, ImplementationPackage, Outcome, Evidence, Source, Recommendation, Experiment, Partner, Job, MarketSignal, Policy, Consent, AuditEvent, Subscription, Invoice.

## Relationships

Person performs Task; Task belongs to Workflow; Workflow belongs to Occupation or JobFunction; Tool enables Task/Workflow; Skill enables Task; WorkRecipe binds Task+Context+Tool+Implementation; Recommendation points to WorkRecipe/Skill/Job/Tool; Outcome measures Recommendation/Implementation; Evidence supports claims.

## Ownership

Each entity has one authoritative owner/context. Cross-context references use stable IDs and immutable event contracts rather than direct table coupling where possible.

## Identity

Separate account identity, person identity, organization membership, and professional profile. Never use email as the durable domain key.

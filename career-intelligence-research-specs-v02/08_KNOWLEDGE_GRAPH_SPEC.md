# Knowledge graph

Graph model connecting occupations, tasks, skills, tools, workflows, evidence, jobs, learning and outcomes.

## Node types

Person, Occupation, JobFunction, Skill, Task, Workflow, Tool, Plugin, Agent, LearningAsset, Job, Organization, Evidence, Source, Policy, Outcome.

## Edge types

PERFORMS, REQUIRES, ENABLES, AUTOMATES, AUGMENTS, DEPENDS_ON, LEARNS, MATCHES, SUPPORTED_BY, MEASURED_BY, RECOMMENDED_FOR, REPLACED_BY, COMPLEMENTS, VALIDATED_BY.

## Provenance

Every non-trivial edge has source/evidence, confidence, effective dates and maintainer. Separate asserted facts from inferred edges.

## Reasoning uses

Skill gap inference; adjacent occupation discovery; task-to-tool recommendation; learning path generation; AI transformation analysis; explainable matching; SEO entity relationships.

## Graph safety

Do not infer sensitive personal attributes from weak correlations. Person-specific graph edges require explicit evidence or user-provided data.

# AI Task Mapping Specification

## Objective
Build a normalized task map for each profession. The occupation title alone is too coarse: two people with the same title may perform different tasks.

## Task schema
- task_id and canonical task name;
- plain-language description and examples;
- trigger / input / output;
- frequency and typical duration (range, source and confidence);
- variability, ambiguity and exception rate;
- required knowledge, skills, tools and credentials;
- physical / digital / interpersonal / judgment components;
- consequence of error and reversibility;
- data sensitivity and regulatory constraints;
- seniority and context variants;
- evidence source, date, geography and confidence.

## Task decomposition
Represent work as:
`workflow → stage → task → subtask → decision → handoff`.
Do not split work so finely that the map becomes unusable. A subtask is separate when it has a distinct input/output, tool, risk, owner or measurable result.

## AI capability labels
- understand / explain;
- retrieve / search;
- extract / structure;
- classify / route;
- generate / draft;
- transform / translate;
- calculate / estimate;
- compare / recommend;
- inspect / review;
- simulate / train;
- monitor / alert;
- execute action;
- coordinate multiple steps.

## Applicability scoring
Use a transparent rubric, not a black-box single score:
1. task digitizability;
2. input availability and quality;
3. model capability on representative cases;
4. workflow repeatability;
5. exception rate;
6. error consequence;
7. human verification cost;
8. integration feasibility;
9. privacy / legal constraints;
10. economic value.

Store dimension-level scores and evidence. Do not average away a critical safety blocker.

## Evidence hierarchy
1. direct task observation / time study;
2. employer or practitioner validated workflow;
3. occupational databases and official standards;
4. representative job postings;
5. credible field research;
6. vendor case study;
7. expert hypothesis.
Mark inferred tasks separately from observed tasks.

## Coverage and confidence
Each profession module must report:
- task coverage estimate;
- unverified task share;
- country and date coverage;
- conflicting sources;
- known omissions;
- confidence by task family.

## User correction loop
Allow user to mark a task as: does not apply / missing / different frequency / different tool / unsafe / already automated. Preserve provenance and distinguish personal profile data from general profession knowledge.

## Acceptance criteria
A profession module is not publishable if it contains only generic skills without task-level workflows, or if task frequency and AI applicability are presented as facts without sources or confidence.

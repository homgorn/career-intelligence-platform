# AI Tool Recommendation Specification

## Goal
Recommend a tool stack that solves a specific work problem with minimum friction, not a trendy list of AI products.

## Tool categories
- general AI assistants and model interfaces;
- profession-specific software with AI features;
- document, image, audio and video tools;
- search / research / knowledge retrieval;
- automation and orchestration;
- CRM, ERP, scheduling, accounting and field-service software;
- agents and agent platforms;
- RPA and computer-use systems;
- learning and simulation platforms;
- privacy, security, evaluation and observability tools.

## Recommendation dimensions
Task fit, quality on representative examples, ease of use, language support, mobile support, integrations, offline/low-connectivity behavior, data residency, privacy, permissions, exportability, reliability, support, pricing model, regional availability, accessibility, vendor lock-in and exit cost.

## User-facing tool card
- what it does in plain language;
- exact task it helps with;
- who should use it / who should not;
- difficulty: beginner / intermediate / technical;
- supported platforms and languages;
- setup time range;
- free / paid / usage-based / quote-based, with checked date;
- required accounts and subscriptions;
- data sent to vendor;
- integration path;
- known limitations;
- official documentation and learning resource;
- alternative tool;
- confidence and last verification date.

## Ranking
Apply hard constraints first (region, language, privacy, budget, device, required integration). Then rank by task fit and total cost of ownership. Do not let popularity compensate for a critical incompatibility.

## Tool stack recommendation
Prefer the smallest viable stack:
- one primary assistant;
- one automation platform only if a repeatable multi-app workflow exists;
- profession system of record;
- approved knowledge source;
- optional specialist tool.
Avoid recommending multiple overlapping subscriptions.

## Currentness
Tool catalogue records require periodic revalidation. Pricing, plan features, connector access and regional availability must never be hardcoded as timeless facts.

## Acceptance criteria
Every tool recommendation must be tied to a task, have an alternative, explain setup burden and disclose relevant data/privacy considerations.

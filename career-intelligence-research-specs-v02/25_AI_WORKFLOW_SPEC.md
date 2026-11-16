# AI Workflow Specification

## Purpose
Convert an AI opportunity into a repeatable, testable work procedure.

## Workflow contract
Every workflow includes:
- user and profession segment;
- problem statement and baseline process;
- trigger;
- inputs and data sources;
- ordered steps;
- AI steps and deterministic steps;
- human approval points;
- outputs and destination;
- exception routes;
- failure handling and recovery;
- quality checks;
- data retention and access rules;
- setup instructions;
- maintenance owner;
- expected cost and benefit;
- test cases and success metrics.

## Workflow patterns
1. Copilot: user performs work, AI advises or drafts.
2. Human-in-the-loop: AI prepares, human approves.
3. Human-on-the-loop: AI executes bounded tasks, human monitors.
4. Deterministic automation: rules and APIs, no model needed.
5. Agentic workflow: model selects tools or next steps within a restricted scope.
6. RPA/UI automation: interacts with legacy interfaces; fragile and needs monitoring.
7. Hybrid: AI for unstructured judgment + code/rules for exact operations.

## Design rules
- Use deterministic code for exact arithmetic, IDs, permissions and state transitions.
- Keep AI output separate from verified facts.
- Require approval before sending messages, spending money, changing records, booking, publishing or deleting.
- Define timeout, retry, idempotency, duplicate prevention and rollback.
- Make provenance visible: source document, extracted field, generated suggestion.
- Provide a manual fallback.
- Start with low-risk, high-frequency tasks.

## Workflow maturity
Draft → simulated → pilot → supervised production → monitored production → optimized → retired.
Each transition requires test evidence and owner approval.

## Example: service request to estimate
1. Receive text, voice note or form.
2. Transcribe and extract customer, location, issue and constraints.
3. Ask for missing information; do not invent it.
4. Retrieve approved price list and standards.
5. Generate a draft estimate with assumptions marked.
6. Human checks technical scope, quantities and price.
7. Send only after approval.
8. Record actual labor, material and final price.
9. Compare estimate with actuals to improve future estimates.

## Acceptance criteria
Workflow is ready only when it has a named owner, known failure modes, test set, approval rules, rollback/manual fallback and a measurable baseline.

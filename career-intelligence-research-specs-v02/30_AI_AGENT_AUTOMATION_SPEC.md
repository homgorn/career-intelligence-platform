# AI Agent & Automation Specification

## Purpose
Choose between a simple assistant, deterministic automation, RPA and an agent. An agent is not the default answer.

## Decision ladder
1. Can a checklist or template solve it?
2. Can existing software feature solve it?
3. Can deterministic rule/API automation solve it?
4. Does an AI assistant add value to an individual step?
5. Is bounded orchestration needed?
6. Is an agent justified after testing and controls?

## Agent contract
- narrow purpose and allowed tasks;
- identity and least-privilege permissions;
- approved tools and data sources;
- explicit prohibited actions;
- input/output schema;
- approval policy;
- budget and rate limits;
- timeouts and retry policy;
- audit log and trace;
- escalation path;
- evaluation set;
- kill switch and rollback.

## Autonomy levels
A0: explain only.
A1: draft; user executes.
A2: execute after each approval.
A3: execute bounded low-risk actions; notify and log.
A4: multi-step execution under policy with human escalation.
A5: unrestricted autonomy is not a product target.

## Human approval required
External communication, financial commitments, safety-critical decisions, legal/medical decisions, access changes, deletion, publication and irreversible operations.

## Failure modes
Prompt injection, data exfiltration, wrong tool call, duplicate action, stale data, hallucinated facts, runaway loops, privilege escalation, silent partial failure and vendor outage.

## Acceptance criteria
No production agent without threat model, test suite, least privilege, monitoring, owner, escalation, rollback and documented limits.

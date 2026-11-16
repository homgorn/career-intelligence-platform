# AI Governance, Privacy & Safety Specification

## Purpose
Make AI adoption safe for individuals and small businesses, not just enterprises.

## Data classification
Public / internal / confidential / personal / sensitive / regulated / safety-critical. Provide profession-specific examples and default prohibitions.

## Core controls
- data minimization and purpose limitation;
- explicit consent for uploads and connections;
- least privilege and role separation;
- retention and deletion policy;
- encryption in transit/at rest where applicable;
- vendor data-use and training policy review;
- audit trail and access review;
- incident reporting and response;
- human approval for consequential actions;
- secure secrets handling;
- backup and recovery.

## High-consequence domains
Electrical work, construction, healthcare, legal, finance, transport and other safety-critical or regulated professions require stricter rules. AI may assist with documentation or retrieval but must not replace licensed judgment, onsite inspection or required standards.

## User-facing warnings
Explain specific risk and mitigation, not generic "AI can be wrong". Label unverified output and show sources where possible.

## Acceptance criteria
No workflow can be published without data classification, permission review, human control design and a documented incident path.

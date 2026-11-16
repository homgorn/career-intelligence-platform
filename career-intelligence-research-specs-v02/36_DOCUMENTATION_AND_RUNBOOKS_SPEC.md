# Documentation & Runbooks Specification

## Purpose
Make each recommended workflow reproducible by a novice and supportable by another person.

## Required documentation artifacts
- quick start (one page);
- prerequisites and account checklist;
- step-by-step setup guide;
- screenshots or short clips with version labels;
- sample input/output;
- prompt/template and configuration export;
- verification checklist;
- troubleshooting decision tree;
- rollback and manual fallback;
- privacy and permissions explanation;
- maintenance schedule;
- change log and owner.

## Runbook structure
Symptom → likely causes → safe checks → resolution → escalation → recovery → prevention.

## Documentation quality
Use plain language, numbered steps, one action per step, visible expected result, screenshots that match current UI, no hidden prerequisites, accessible formatting and localization.

## Versioning
Docs are versioned with workflow configuration. Breaking changes require migration instructions and a tested rollback.

## Supportability
A workflow without an owner, support path and runbook cannot be marked production-ready.

## Acceptance criteria
A user outside the build team can install, test, troubleshoot and safely disable the workflow using only the documentation.

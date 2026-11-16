# Security policy

## Reporting a vulnerability

Please **do not** open public issues for security problems.

Report privately to the maintainers via GitHub Security Advisories
("Report a vulnerability" on the Security tab of this repository).

Include:

- what is affected (file, stage, tool, output);
- a minimal reproduction;
- expected vs actual behaviour;
- impact and suggested fix, if known.

We aim to acknowledge within 48 hours and agree a fix timeline within
7 days. Credits: reporters who wish to be acknowledged will be listed
in `CHANGELOG.md`.

## Scope

In scope: `tools/`, `skills/`, `docs/ops/`, CI configuration, and the
integrity of the specification index (`docs/specs/`, `SPEC_INDEX_DATA.tsv`).

Out of scope: the frozen legacy archive (`old specs не трогать пока.7z`)
and the application product, which is pre-release and has no hosted service yet.

## Secrets

This repository must never contain secrets or API keys. If you find one,
report it the same way and treat the secret as compromised.

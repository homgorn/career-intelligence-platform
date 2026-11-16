# Security architecture

Security baseline for a multi-tenant SaaS handling resumes, work data, tool credentials and AI workflows.

## Baseline

Threat model against account takeover, tenant isolation failure, prompt injection, tool abuse, secret leakage, supply-chain compromise, insecure file handling, SSRF, data exfiltration and excessive agent agency.

## Controls

Strong authentication; MFA for privileged roles; least privilege; short-lived tokens; secret vault; encryption in transit/at rest; signed URLs; malware scanning; sandboxing; egress controls; rate limits; audit logs; anomaly detection; dependency scanning; backups.

## AI-specific

Treat retrieved content and tool output as untrusted input. Tool permissions are explicit. High-impact tools require approval and constrained parameters. Never expose secrets to model context.

## Security testing

SAST, DAST, dependency/SBOM scanning, authorization tests, tenant-isolation tests, prompt-injection tests, tool-abuse tests, file parser fuzzing and incident drills.

## Reference baseline

Align controls with OWASP Top 10:2025 and OWASP LLM guidance; adapt controls to actual threat model rather than checklist compliance alone.

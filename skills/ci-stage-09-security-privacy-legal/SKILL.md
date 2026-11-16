---
name: ci-stage-09-security-privacy-legal
description: "Career Intelligence / AI Profession Intelligence, этап STAGE-09 — Security + privacy + legal gate. Design review после STAGE-02, implementation review после STAGE-11. AUTH, RBAC, tenant isolation, PII, resume data, document storage, LLM context, RAG, tools, MCP, agents, logging, audit, consent, delete, export, retention, third-party providers. Плюс prompt injection, tool abuse, secret leakage, cross-tenant, SSRF. Юридический вывод не принимается в IDE."
---

# STAGE-09 — Security + privacy + legal

Полный источник шагов — `docs/ops/stages/STAGE-09-SECURITY-PRIVACY-LEGAL.md`.

## Два прохода, не смешивать

- **Design review** — после STAGE-02: оцениваются контракты и план.
- **Implementation review** — после STAGE-11: оценивается фактическая система.

## Что проверить

AUTH, RBAC, TENANT ISOLATION, PII, RESUME DATA, DOCUMENT STORAGE,
LLM CONTEXT, RAG, TOOLS, MCP, AGENTS, LOGGING, AUDIT, CONSENT, DELETE,
EXPORT, RETENTION, THIRD-PARTY PROVIDERS.

Отдельно: prompt injection, tool abuse, secret leakage, cross-tenant access,
SSRF, malicious documents, unsafe automation, excessive agent agency.

## Формат finding

severity, evidence, risk, fix, test, status.

## Юридическая граница

Если вывод зависит от юрисдикции — не придумывай. Создай legal review trigger.

## Выходы

- `docs/gates/SECURITY_GATE.md`
- `docs/gates/PRIVACY_GATE.md`
- `docs/gates/LEGAL_GATE.md`

## Контроль

```bash
python tools/runbook_validate.py --stage STAGE-09
```

## Финиш

Число findings по severity, blocking count, что мешает выпуску, что отдано
на legal review. Остановись.

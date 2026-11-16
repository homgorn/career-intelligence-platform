# STAGE-09 — Security + privacy + legal

> Бывший PROMPT 09, разделённый на два прохода. Design review — до кода,
> implementation review — после STAGE-11. Смешивать их нельзя: первый
> оценивает контракты, второй — фактическую систему.

## Назначение

Провести security / privacy / legal gate. Ничего не выпускать, пока он не
пройден. Юридические выводы зависят от юрисдикции и не выдумываются —
создаётся legal review trigger.

## Trigger

Design review — после STAGE-02. Implementation review — после STAGE-11.

## Inputs

- `11_SECURITY_ARCHITECTURE_SPEC.md`
- `12_LEGAL_COMPLIANCE_SPEC.md`
- `13_PRIVACY_DATA_SUBJECT_SPEC.md`
- `04_RULE_POLICY_ENGINE_SPEC.md`
- `PILOT_DECISION.md` — юрисдикция
- `docs/contracts/*`

## Проверяем

AUTH, RBAC, TENANT ISOLATION, PII, RESUME DATA, DOCUMENT STORAGE, LLM CONTEXT,
RAG, TOOLS, MCP, AGENTS, LOGGING, AUDIT, CONSENT, DELETE, EXPORT, RETENTION,
THIRD-PARTY PROVIDERS.

Отдельно: prompt injection, tool abuse, secret leakage, cross-tenant access,
SSRF, malicious documents, unsafe automation, excessive agent agency.

## Для каждого finding

severity, evidence, risk, fix, test, status.

## Outputs

- `docs/gates/SECURITY_GATE.md`
- `docs/gates/PRIVACY_GATE.md`
- `docs/gates/LEGAL_GATE.md`

## Definition of Done

- [ ] Каждый finding имеет severity, evidence, risk, fix, test, status.
- [ ] Blocking findings не закрыты молча.
- [ ] Tenant isolation проверен тестом на уровне данных и API.
- [ ] Согласие (`Consent`) запрашивается до внешних интеграций.
- [ ] Удаление пользователя распространяется на производные индексы.
- [ ] Prompt injection и tool abuse проверены тестами.
- [ ] Legal conclusion, зависящая от юрисдикции, вынесена на legal review trigger,
      а не принята внутри IDE.

## HARD STOP

Показать: число findings по severity, blocking count, что мешает выпуску,
что отдано на legal review. Ждать человека.

## Rollback

Исправления security findings — вне обычного rollback: ротация секретов,
отзыв токенов, patch уязвимостей. Никаких «откатим потом».

## Промпт для IDE

```text
Этап STAGE-09 — security / privacy / legal gate.

Проход 1 — design review (после STAGE-02).
Проход 2 — implementation review (после STAGE-11).

Основывайся на:
- career-intelligence-research-specs-v02/11_SECURITY_ARCHITECTURE_SPEC.md
- career-intelligence-research-specs-v02/12_LEGAL_COMPLIANCE_SPEC.md
- career-intelligence-research-specs-v02/13_PRIVACY_DATA_SUBJECT_SPEC.md
- career-intelligence-research-specs-v02/04_RULE_POLICY_ENGINE_SPEC.md
- docs/architecture/PILOT_DECISION.md

Проверь: AUTH, RBAC, TENANT ISOLATION, PII, RESUME DATA, DOCUMENT STORAGE,
LLM CONTEXT, RAG, TOOLS, MCP, AGENTS, LOGGING, AUDIT, CONSENT, DELETE, EXPORT,
RETENTION, THIRD-PARTY PROVIDERS.

Отдельно: prompt injection, tool abuse, secret leakage, cross-tenant access,
SSRF, malicious documents, unsafe automation, excessive agent agency.

Для каждого finding: severity, evidence, risk, fix, test, status.

Создай:
docs/gates/SECURITY_GATE.md
docs/gates/PRIVACY_GATE.md
docs/gates/LEGAL_GATE.md

Если legal conclusion зависит от jurisdiction — не придумывай. Создай
legal review trigger.

В конце заполни docs/ops/STAGE-STATUS.md и остановись.
```

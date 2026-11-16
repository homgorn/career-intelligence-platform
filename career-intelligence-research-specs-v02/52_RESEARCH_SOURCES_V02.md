# V02 Research Sources & Verification Notes

Проверены 2026-11-14. Используются как примеры продуктовых возможностей и методологических ограничений; перед публикацией каталога конкретные тарифы и доступность нужно перепроверять по стране и плану.

## Official documentation
- OpenAI — Apps in ChatGPT: https://help.openai.com/en/articles/11487775-connectors-in-chatgpt
  Connected apps can search/reference services and, depending on app capabilities and permissions, perform write actions. Availability depends on plan, region, workspace, role, model and interface.
- OpenAI — Configuring actions in GPTs: https://help.openai.com/en/articles/9442513
  Actions require API details and an OpenAPI schema; authentication may use none, API key or OAuth; workspace domain restrictions can block actions.
- Microsoft — Copilot Studio overview: https://learn.microsoft.com/microsoft-copilot-studio/overview
  Describes low-code agent/workflow creation, connected data and systems, analytics, evaluations, administration and cost management.
- Microsoft — Copilot Studio documentation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/
  Covers agents, workflows, tools, MCP servers, testing, evaluation, publishing, monitoring, governance and billing.
- Google — Integrations with Gemini in Workspace: https://support.google.com/docs/answer/16796422
  Third-party integrations are available in supported Workspace surfaces; eligibility depends on account/edition, subscription and administrator settings.
- Zapier — AI automation tools (vendor-authored overview): https://zapier.com/blog/ai-automation-tools/
  Useful for market discovery, not independent proof of comparative performance.
- Zapier — Workflow orchestration tools (vendor-authored overview): https://zapier.com/blog/workflow-orchestration-tools/
  Summarizes tool categories and trade-offs; prices/features need rechecking.

## Product design implications
1. "Plugin" is not a stable universal category. Use a capability catalog with separate fields for app, connector, API, agent, workflow template and service.
2. Tool availability is conditional: country, plan, workspace policy, admin permission, interface and authentication can all affect it.
3. Integration is not equivalent to safe automation. Read/write scope, approvals, audit, failure handling and revocation must be evaluated separately.
4. A demo is not production readiness. Test representative cases, monitor errors and establish rollback.
5. Vendor comparison pages are useful for discovery but must be labeled as vendor-authored evidence.

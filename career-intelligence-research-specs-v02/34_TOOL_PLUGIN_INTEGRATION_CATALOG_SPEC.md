# Tool, Plugin & Integration Catalog Specification

## Purpose
Maintain a verified directory of tools, plugins, connectors, templates and profession-specific software that can support workflows.

## Terminology
- Tool: standalone software or feature.
- Plugin/app/connector: bridge between a host and an external service.
- Template: reusable configuration or workflow blueprint.
- Agent: model-driven component that can use tools.
- Integration: technical connection between systems.
- Service package: human or vendor implementation delivered to the user.

Do not use "plugin" as a universal label. Product ecosystems change their terminology and packaging.

## Catalog record
Canonical vendor/product, category, task coverage, capabilities, supported countries/languages, platforms, plans, pricing model, free tier, data processing terms, security certifications (verified only), connector scope, auth method, permissions, limits, uptime/support, official docs, changelog, last checked, reviewer and confidence.

## Discovery sources
Official vendor documentation and marketplace first; independent evaluations and user feedback second. Vendor claims must be labeled as claims, not independent validation.

## Integration capability levels
0: no integration;
1: export/import;
2: one-way sync;
3: two-way sync;
4: API/webhook;
5: governed agent/tool access with scoped permissions and audit.

## Selection rules
Check regional access, payment availability, language quality, mobile support, account requirements, data residency, plan restrictions and required admin permissions.

## Starter catalog categories
- general assistants;
- office suites;
- search/research;
- transcription and voice;
- OCR/document extraction;
- image/video/audio;
- automation (Zapier, Make, n8n, Power Automate and comparable tools);
- CRM/field-service/accounting;
- knowledge bases and RAG;
- agent platforms;
- evaluation/monitoring;
- profession-specific systems.

## Freshness
Recheck availability and pricing before displaying a purchase recommendation. If not checked, say "price/availability not verified". Never imply an integration is available just because an API exists.

## Acceptance criteria
Every listing has a specific use case, official source, region/plan constraints, date checked and a clear status: verified / beta / waitlist / unavailable / unknown.

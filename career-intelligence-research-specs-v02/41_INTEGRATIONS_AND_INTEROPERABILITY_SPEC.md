# Integrations & Interoperability Specification

## Purpose
Prevent the product from recommending disconnected tools that create more manual work than they remove.

## Integration map
User identity → profession software → files/knowledge → communications → CRM/ERP → calendar/scheduling → billing/payments → automation/orchestration → analytics.

## Integration methods
Native connector, marketplace app, OAuth, API key, webhook, MCP/tool server, CSV import/export, email forwarding, browser/RPA automation. Each method has different reliability and security properties.

## Required metadata
Read/write scope, OAuth scopes, token storage, refresh behavior, rate limits, data direction, sync frequency, duplicate behavior, error handling, audit logs, admin approval, data residency and revocation steps.

## Design rules
- Prefer official native connectors and scoped OAuth.
- Never ask users to paste secrets into chat or documents.
- Do not store credentials in prompt templates.
- Minimize data transferred.
- Use idempotency keys and reconciliation for writes.
- Provide export and manual fallback.
- Revalidate connector permissions after vendor changes.

## Acceptance criteria
An integration is supported only after end-to-end tests for authentication, permissions, normal flow, failure flow, revocation and data deletion.

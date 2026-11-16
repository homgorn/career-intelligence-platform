# Gates and adapters architecture

Gates stop unsafe or invalid transitions; adapters translate between stable domain contracts and volatile external providers.

## Mandatory gates

Identity/authorization; consent; input quality; evidence/provenance; policy; safety; tool capability; budget; human review; execution verification; outcome validity.

## Adapter categories

LLM provider; embedding provider; search; vector DB; graph DB; SQL DB; file storage; email; CRM; payments; analytics; job feeds; taxonomy providers; learning providers; tool/MCP servers; identity provider.

## Adapter contract

Capability discovery, typed request/response, timeout, retry policy, rate limits, auth scope, data handling class, health status, provider version, fallback behavior.

## Anti-lock-in

Domain logic never imports vendor SDKs directly. Provider-specific code lives behind adapters. Maintain a conformance test suite for every production adapter.

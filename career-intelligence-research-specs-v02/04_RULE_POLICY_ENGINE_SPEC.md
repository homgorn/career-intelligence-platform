# Rules, policy and eligibility engine

Typed policy layer for recommendations, tool access, automation, billing, geography, risk, and compliance.

## Policy classes

Eligibility; safety; privacy; data residency; tool permissions; age/region; subscription entitlements; enterprise controls; human-review requirements; regulated-domain restrictions.

## Evaluation

Policies evaluate structured facts and return ALLOW, DENY, ALLOW_WITH_GUARDRAILS, or REQUIRE_HUMAN_REVIEW plus reason codes and policy version.

## Priority

Security/privacy/legal hard stops override product optimization. Organization policy overrides user defaults. Explicit user consent is required where law or product policy requires it.

## Auditability

Every non-trivial decision stores policy IDs, input facts used, result, and version. No hidden policy in prompts.

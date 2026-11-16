# Event model and event contracts

Event-driven integration contract for the product. Events describe facts that happened; commands request actions.

## Canonical events

profile.created; profile.updated; resume.ingested; occupation.matched; task.identified; workflow.created; recommendation.generated; recommendation.accepted; implementation.started; implementation.completed; outcome.recorded; tool.verified; policy.blocked; consent.granted; consent.revoked; subscription.changed; partner.attributed.

## Event envelope

event_id, event_type, schema_version, occurred_at, actor_type, actor_id, tenant_id, correlation_id, causation_id, data, provenance, privacy_class.

## Rules

Events are immutable. Consumers must be idempotent. PII minimization applies to event payloads. Sensitive data should be referenced by secure object ID rather than copied into every event.

## Replay

Consumers must tolerate replay. Critical projections must be rebuildable from durable events or authoritative data.

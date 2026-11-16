# Billing and entitlement engine

Separates payments from feature/data entitlements.

## Entitlement

plan; feature; quota; seat; expiration; tenant; override; source.

## Metering

Measure billable events through immutable usage records. Billing provider reconciliation is required.

## Failure handling

Provider outage must not corrupt entitlements or delete data. Graceful degradation and reconciliation jobs are required.

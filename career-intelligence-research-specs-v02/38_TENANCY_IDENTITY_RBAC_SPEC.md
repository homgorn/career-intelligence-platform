# Tenancy, identity and RBAC

Authorization model for B2C, teams, enterprises and partners.

## Roles

Person; member; manager; HR; admin; implementation partner; support; security reviewer; system service.

## Scopes

Tenant; team; user; resource; action; data class.

## ABAC extension

Use attributes for context-sensitive policies; never rely only on role names for high-risk actions.

## Isolation tests

Automated negative tests must prove one tenant cannot access another tenant's profile, documents, recipes, outcomes or billing data.

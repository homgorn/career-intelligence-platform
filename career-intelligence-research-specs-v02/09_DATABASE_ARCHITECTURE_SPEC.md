# Database architecture

Polyglot persistence strategy. Keep the relational system of record authoritative; use search/vector/graph as derived indexes unless a workload clearly requires otherwise.

## Relational

PostgreSQL for tenants, identities, profiles, taxonomy mappings, recipes, recommendations, outcomes, subscriptions, policies, audit metadata and workflow state.

## Object storage

Encrypted object storage for resumes, documents, exports and artifacts with short-lived signed URLs and lifecycle policies.

## Search

OpenSearch/Elasticsearch or equivalent for text/entity retrieval and faceting. Indexes are rebuildable from authoritative records.

## Vector

pgvector or dedicated vector DB for embeddings. Store embedding model/version and source hash.

## Graph

Neo4j or equivalent only if graph traversal materially improves product decisions; otherwise PostgreSQL graph tables can be the initial implementation.

## Multi-tenancy

Tenant ID on every tenant-scoped record; database-level row security where practical; explicit authorization service; tests for cross-tenant leakage.

## Retention

Data classes have retention periods and deletion semantics. User deletion must propagate to derived indexes and cached representations subject to legally required retention.

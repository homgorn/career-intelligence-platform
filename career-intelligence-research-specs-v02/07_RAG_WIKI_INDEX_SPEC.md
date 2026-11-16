# LLM Wiki, RAG and indexes

Knowledge architecture for a continuously updated internal and user-facing knowledge base.

## Knowledge layers

Source documents; normalized claims; entities; relationships; retrieval chunks; procedural runbooks; policy documents; product documentation; profession modules; tool records; research notes; outcome evidence.

## Index strategy

Keyword/BM25 index for exact terms; vector index for semantic retrieval; graph index for entity relationships; metadata filters for tenant, locale, freshness, trust, source type and access level.

## Chunk contract

chunk_id, document_id, version, section_path, text, token_count, embedding_version, ACL, locale, source_ref, valid_from, valid_to.

## RAG pipeline

Query normalization → intent/entity resolution → hybrid retrieval → reranking → evidence selection → answer synthesis → citation/provenance → confidence → feedback.

## Freshness

Tool prices, capabilities, policies, integrations and market data require TTL/verification dates. Stale records must be marked rather than presented as current facts.

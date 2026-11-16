# wiki — продуктовая база знаний

Создаётся в `STAGE-06` (только если `LLM_DECISION.md` = `LLM_REQUIRED`/`LLM_PARTIAL`).

## Модель

```
document → version → chunk → embedding → source → ACL → freshness
```

## Правила

- Wiki — не источник истины. Authoritative data всегда в реляционной БД.
- Chunk содержит: chunk_id, document_id, version, section_path, text,
  token_count, embedding_version, ACL, locale, source_ref, valid_from, valid_to.
- Tool prices, capabilities, policies, integrations, market data имеют TTL
  и verification dates.
- Tenant-aware retrieval обязателен.
- Stale documents помечаются, а не удаляются молча.

## Связанное

- `career-intelligence-research-specs-v02/07_RAG_WIKI_INDEX_SPEC.md`
- `career-intelligence-research-specs-v02/36_SEARCH_WIKI_CONTENT_INDEX_MANIFEST.md`

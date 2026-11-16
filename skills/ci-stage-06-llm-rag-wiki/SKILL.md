---
name: ci-stage-06-llm-rag-wiki
description: "Career Intelligence / AI Profession Intelligence, этап STAGE-06 — LLM + RAG + Wiki. Применять только если LLM_DECISION.md = LLM_REQUIRED или LLM_PARTIAL и человек подтвердил. Controlled LLM layer с model/provider/version tracking, cost и latency, fallback, prompt registry, tenant-aware retrieval. Семь обязательных тестов, включая prompt injection и tenant leakage. Autonomous agent не создаётся."
---

# STAGE-06 — LLM + RAG + wiki

Полный источник шагов — `docs/ops/stages/STAGE-06-LLM-RAG-WIKI.md`.

## Условие запуска

`docs/gates/LLM_DECISION.md` = `LLM_REQUIRED` / `LLM_PARTIAL`.
Иначе этап не запускается.

## Архитектура

```
Application → LLM Orchestrator → Provider Adapter → Model
Application → Retrieval → Hybrid Search → Reranker → Evidence → LLM
```

## Требования

structured outputs; model/provider/version tracking; cost tracking;
latency tracking; retries; fallback; prompt/version registry; evaluation hooks;
provenance; citation support; sensitive-data filtering; tenant-aware retrieval.

LLM не является authoritative database.

Wiki: document → version → chunk → embedding → source → ACL → freshness.

## Обязательные тесты

Irrelevant retrieval; stale document; tenant leakage; unsupported claim;
malformed structured output; prompt injection; missing evidence.

## Контроль

```bash
python tools/runbook_validate.py --stage STAGE-06
```

## Финиш

Число тестов, пример run с provenance, стоимость одного пользователя,
известные отказы. Остановись.

# STAGE-06 — LLM + RAG + Wiki

> Бывший PROMPT 06. Условный этап: запускается только если `LLM_DECISION.md`
> даёт `LLM_REQUIRED` или `LLM_PARTIAL`.

## Назначение

Реализовать контролируемый LLM-слой и минимальный рабочий RAG. LLM не
authoritative database.

## Trigger

`LLM_DECISION.md` = `LLM_REQUIRED` / `LLM_PARTIAL`, подтверждён человеком.
Получены доступы к провайдеру и бюджет.

## Inputs

- `06_LLM_PLATFORM_SPEC.md`
- `07_RAG_WIKI_INDEX_SPEC.md`
- `10_DATA_GOVERNANCE_PROVENANCE_SPEC.md`
- `11_SECURITY_ARCHITECTURE_SPEC.md`
- `05_GATES_AND_ADAPTERS_SPEC.md`
- `docs/gates/LLM_DECISION.md`

## Архитектура

```
Application → LLM Orchestrator → Provider Adapter → Model

Application → Retrieval → Hybrid Search → Reranker → Evidence → LLM
```

## Требования

- structured outputs; invalid output отклоняется, а не молча коэрцится;
- model/provider/version tracking;
- cost tracking;
- latency tracking;
- retries;
- fallback;
- prompt/version registry;
- evaluation hooks;
- provenance;
- citation support;
- sensitive-data filtering;
- tenant-aware retrieval.

Knowledge Wiki: document → version → chunk → embedding → source → ACL → freshness.

## Outputs

- LLM orchestrator + provider adapters
- Prompt registry
- Retrieval pipeline (минимум один рабочий RAG)
- Wiki document/chunk model
- Cost/latency telemetry
- Tests

## Обязательные тесты

- Irrelevant retrieval.
- Stale document.
- Tenant leakage.
- Unsupported claim.
- Malformed structured output.
- Prompt injection.
- Missing evidence.

## Definition of Done

- [ ] Каждый consequential run записывает model/provider/version.
- [ ] Стоимость и latency измеряются и видны в телеметрии.
- [ ] Есть fallback при недоступности провайдера.
- [ ] RAG воспроизводит источник и цитирование для каждого утверждения.
- [ ] Tenant-aware retrieval проверен тестом на cross-tenant leakage.
- [ ] Sensitive data не попадает в контекст модели.
- [ ] Все семь обязательных тестов проходят.
- [ ] Сложный autonomous agent не создаётся.

## HARD STOP

Показать: число тестов, примерrun с provenance, стоимость одного пользователя,
известные отказы. Ждать человека.

## Rollback

Feature flag на LLM-фичу; возврат к deterministic-пути; откат prompt к предыдущей
версии реестра. Провайдер отключается через adapter, без изменения домена.

## Промпт для IDE

```text
Этап STAGE-06 — LLM + RAG + wiki.

Запускается только если docs/gates/LLM_DECISION.md = LLM_REQUIRED / LLM_PARTIAL.

Основывайся строго на:
- career-intelligence-research-specs-v02/06_LLM_PLATFORM_SPEC.md
- career-intelligence-research-specs-v02/07_RAG_WIKI_INDEX_SPEC.md
- career-intelligence-research-specs-v02/10_DATA_GOVERNANCE_PROVENANCE_SPEC.md
- career-intelligence-research-specs-v02/11_SECURITY_ARCHITECTURE_SPEC.md
- career-intelligence-research-specs-v02/05_GATES_AND_ADAPTERS_SPEC.md

Архитектура:
Application → LLM Orchestrator → Provider Adapter → Model
и отдельно:
Application → Retrieval → Hybrid Search → Reranker → Evidence → LLM

Требования: structured outputs, model/provider/version tracking, cost tracking,
latency tracking, retries, fallback, prompt/version registry, evaluation hooks,
provenance, citation support, sensitive-data filtering, tenant-aware retrieval.

LLM не является authoritative database.

Knowledge Wiki: document → version → chunk → embedding → source → ACL → freshness.

Сделай минимум один working RAG pipeline.

Тесты: irrelevant retrieval, stale document, tenant leakage, unsupported claim,
malformed structured output, prompt injection, missing evidence.

Не создавай сложного autonomous agent.
В конце заполни docs/ops/STAGE-STATUS.md и остановись.
```

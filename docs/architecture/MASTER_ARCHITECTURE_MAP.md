# MASTER_ARCHITECTURE_MAP

Карта архитектуры по архиву `career-intelligence-research-specs-v02/`.
Источник истины — спеки; этот документ их интерпретирует и не заменяет.

## 1. Верхнеуровневая модель

Продукт измеряет **улучшение карьерных и рабочих исходов**, а не использование
AI (`00_MASTER_ARCHITECTURE.md`). AI — одно из средств; `NON_AI` — полноценное
решение, если оно дешевле, безопаснее или проще (`29_WORK_RECIPE_SPEC.md`).

```
USER/ORG → CONTEXT → GOAL → TASK/WORKFLOW → DIAGNOSIS
→ OPTIONS (AI / NON_AI / HUMAN) → IMPLEMENTATION → VERIFICATION
→ MEASURED OUTCOME → FEEDBACK → UPDATED RECOMMENDATION
```

Единица ценности — `WorkRecipe`: задача + контекст + инструмент + внедрение +
верификация + evidence + expected value (`29_WORK_RECIPE_SPEC.md`).

Каждая рекомендация обязана быть traceable к цели пользователя и наблюдаемому
исходу. Рекомендация без метода верификации не считается завершённой
(`48_BEGINNER_UX_AND_PRODUCT_JOURNEY_SPEC.md`).

## 2. Bounded contexts

Контексты взяты из `00_MASTER_ARCHITECTURE.md`; владельцы и сущности — из
`02_DOMAIN_MODEL_SPEC.md`, `09_DATABASE_ARCHITECTURE_SPEC.md`,
`10_DATA_GOVERNANCE_PROVENANCE_SPEC.md`.

| Контекст | Владеет авторитетными данными | Ключевые спеки |
| --- | --- | --- |
| Identity & Tenancy | Tenant, Person, Organization, Consent, PolicyDecision, AuditEvent | `38_TENANCY_IDENTITY_RBAC_SPEC`, `13_PRIVACY_DATA_SUBJECT_SPEC` |
| Career Intelligence | CareerProfile, Occupation, Skill, Job, MarketSignal | `05_USER_PROFILE_SPEC`, `04_TAXONOMY_SPEC`, `08_MATCHING_SCORING_SPEC` |
| Work Intelligence | Task, Workflow, WorkRecipe | `24_AI_TASK_MAPPING_SPEC`, `25_AI_WORKFLOW_SPEC`, `29_WORK_RECIPE_SPEC` |
| AI Transformation | AIProfile, AICapability, ReadinessAssessment, RiskAssessment | `23_AI_PROFESSION_INTELLIGENCE_SPEC`, `29_AI_LEVERAGE_AND_IMPACT_SPEC`, `49_AI_DATA_MODEL_ADDENDUM` |
| Recommendation Engine | Recommendation, связь Evidence, score, gate results | `01_SDD_ENGINE_SPEC`, `04_RULE_POLICY_ENGINE_SPEC`, `05_GATES_AND_ADAPTERS_SPEC` |
| Outcomes | Outcome, OutcomeMeasurement, Feedback | `31_OUTCOME_ROI_ENGINE_SPEC`, `31_AI_OUTCOME_FEEDBACK_SPEC`, `23_ANALYTICS_PRODUCT_METRICS_SPEC` |
| Knowledge & Research | Source, Claim, Document/Chunk (производные), Tool records | `07_RAG_WIKI_INDEX_SPEC`, `10_DATA_GOVERNANCE_PROVENANCE_SPEC`, `36_SEARCH_WIKI_CONTENT_INDEX_MANIFEST` |
| Implementation & Learning | ImplementationPackage, LearningAsset | `37_IMPLEMENTATION_PACKAGES_SPEC`, `35_AI_LEARNING_PATHS_SPEC`, `33_BEGINNER_AI_ONBOARDING_SPEC` |
| Tools & Adapters | Tool, Connector, Provider | `26_MCP_TOOL_PLUGIN_SPEC`, `34_TOOL_PLUGIN_INTEGRATION_CATALOG_SPEC`, `47_ADAPTER_CATALOG` |
| Growth, Billing, Support, Marketplace | Subscription, Invoice, Partner, Content | `17_MONETIZATION_AND_GTM_SPEC`, `22_BILLING_MONETIZATION_SPEC`, `18_GROWTH_MARKETING_SPEC` |

Правило контекстов: один владелец на сущность; кросс-контекстные ссылки —
стабильные ID и неизменяемые event contracts, а не прямая связь таблиц
(`02_DOMAIN_MODEL_SPEC.md`, `03_EVENT_CONTRACTS_SPEC.md`). Giant mutable
`user profile` object запрещён (`00_MASTER_ARCHITECTURE.md`).

## 3. Авторитетные данные и производные индексы

System of record — реляционная БД (`09_DATABASE_ARCHITECTURE_SPEC.md`).
Search, vector и graph — производные и перестраиваемые:

```
PostgreSQL (authoritative) ──rebuild──▶ OpenSearch / vector / graph
        ▲                                      │
        └────────── event log (immutable) ◀────┘
```

LLM не является источником истины. Memory модели и векторный индекс не являются
источником истины (`01_SDD_ENGINE_SPEC.md`, `10_DATA_GOVERNANCE_PROVENANCE_SPEC.md`).

Evidence hierarchy (`10_DATA_GOVERNANCE_PROVENANCE_SPEC.md`): observed product
outcome > replicated research > authoritative public dataset > vendor claim >
secondary reporting > model inference. Низкие уровни не выдаются за факт.

## 4. Кросс-контекстные правила

- **Детерминизм:** бизнес-правила, gates, entitlement, pricing, permissions,
  safety не зависят от LLM-прозы; LLM может предлагать, typed services решают
  (`01_SDD_ENGINE_SPEC.md`, `04_RULE_POLICY_ENGINE_SPEC.md`).
- **Адаптеры:** vendor SDK не импортируется в domain layer; конфарм-тесты
  на каждый production adapter (`05_GATES_AND_ADAPTERS_SPEC.md`).
- **События:** 17 канонических событий, immutable, idempotent consumers,
  replay-tolerant (`03_EVENT_CONTRACTS_SPEC.md`).
- **Происхождение:** любое consequential relation имеет source, confidence,
  effective dates, verification status (`10_DATA_GOVERNANCE_PROVENANCE_SPEC.md`).
- **Безопасность:** retrieved content и tool output — untrusted input;
  secrets никогда не попадают в model context (`11_SECURITY_ARCHITECTURE_SPEC.md`).

## 5. Слои исполнения

| Слой | Что существует | Спеки |
| --- | --- | --- |
| Foundation | tenancy, auth, RBAC, audit, observability | `38_…`, `11_…`, `42_OBSERVABILITY_SPEC` |
| Domain | 18 сущностей P0 | `02_DOMAIN_MODEL_SPEC`, `09_DATABASE_ARCHITECTURE_SPEC` |
| Decision | SDD engine, policy, gates | `01_…`, `04_…`, `05_…` |
| Intelligence (условно) | LLM, RAG, Wiki | `06_…`, `07_…` — только по `LLM_DECISION.md` |
| Surface | website, onboarding, distribution MVP | `14_…`, `28_…`, `19_SEO_PROGRAMMATIC_SPEC` |
| Measurement | analytics, outcome, cost per outcome | `23_…`, `31_…`, `18_ANALYTICS_EVALS_SPEC` |
| Moat (P2) | knowledge graph, agent runtime, managed AI | `08_KNOWLEDGE_GRAPH_SPEC`, `25_AGENT_RUNTIME_SPEC`, `40_MANAGED_AI_SERVICE_SPEC` |

## 6. Границы, которые нельзя пересекать

1. Ни одна сущность не принадлежит двум контекстам одновременно.
2. Ни один индекс не пишется как авторитетный.
3. Ни один LLM-вывод не становится фактом без evidence и version.
4. Ни один gate не обходится ради скорости.
5. Ни один vendor не становится hard dependency.
6. Ни одна рекомендация не выпускается без метода верификации.
7. Ни один P1/P2 блок не реализуется до своего gate.

## OPEN QUESTIONS, влияющие на карту

- Какой taxonomy crosswalk (O*NET / ESCO / местная) для пилота — влияет на
  структуру Occupation/Skill и процесс нормализации (`04_TAXONOMY_SPEC.md`).
- Нужен ли LLM в P0 и для каких шагов — влияет на слой Intelligence.
- Требует ли пилот загрузку резюме — вводит ли `07_RESUME_INGESTION_SPEC`
  в P0-объём.

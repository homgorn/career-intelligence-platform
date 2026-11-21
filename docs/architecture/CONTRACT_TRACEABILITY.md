# CONTRACT_TRACEABILITY — что чем определено и кто это потребляет

Прослеживаемость контрактов: спека → артефакт → производитель → потребитель.
Нужна для STAGE-02, чтобы ни один контракт не появился «из воздуха» и ни один
потребитель не остался без источника.

Легенда: **S** — спека-источник, **P** — кто производит артефакт,
**C** — кто потребляет.

## 1. Архитектурные контракты

| Контракт | S | P | C |
| --- | --- | --- | --- |
| Канонические события | `03_EVENT_CONTRACTS_SPEC` | STAGE-02 | STAGE-08, 10, 11, 12 |
| Схема данных P0 | `02_DOMAIN_MODEL_SPEC`, `09_DATABASE_ARCHITECTURE_SPEC` | STAGE-02 → STAGE-04 | STAGE-05, 06, 09, 11 |
| API foundation | `37_API_CONTRACTS_SPEC`, `38_TENANCY_IDENTITY_RBAC_SPEC` | STAGE-02 → STAGE-03 | STAGE-08, 11 |
| Политики и гейты | `04_RULE_POLICY_ENGINE_SPEC`, `05_GATES_AND_ADAPTERS_SPEC` | STAGE-05 | STAGE-11, 12 |
| Решение движка (decision record) | `01_SDD_ENGINE_SPEC` | STAGE-05 | STAGE-11, 12, 15 |
| WorkRecipe | `29_WORK_RECIPE_SPEC` | STAGE-05 | STAGE-08, 10, 11 |
| Метрики и телеметрия | `23_ANALYTICS_PRODUCT_METRICS_SPEC` | STAGE-10 | STAGE-12 |
| Outbound ROI | `31_OUTCOME_ROI_ENGINE_SPEC` | STAGE-10 | STAGE-12 |
| LLM-контракт (условно) | `06_LLM_PLATFORM_SPEC` | STAGE-06 | STAGE-08, 10 |
| RAG-контракт (условно) | `07_RAG_WIKI_INDEX_SPEC` | STAGE-06 | STAGE-08 |

## 2. События

Все 17 событий определены в `03_EVENT_CONTRACTS_SPEC.md` и замораживаются
в STAGE-02. Производитель и потребитель — подсистемы, а не «кто угодно».

| Событие | Производитель | Потребители |
| --- | --- | --- |
| `profile.created` | Career Intelligence | Recommendation, Analytics |
| `profile.updated` | Career Intelligence | Recommendation, RAG (переиндексация) |
| `resume.ingested` | Career Intelligence (P1) | Career Intelligence |
| `occupation.matched` | Career Intelligence | Recommendation |
| `task.identified` | Work Intelligence | Recommendation |
| `workflow.created` | Work Intelligence | Recommendation, WorkRecipe |
| `recommendation.generated` | Recommendation Engine | Website, Analytics |
| `recommendation.accepted` | Website / API | Recommendation, Analytics |
| `implementation.started` | Implementation | Outcome, Analytics |
| `implementation.completed` | Implementation | Outcome, Analytics |
| `outcome.recorded` | Outcome | Recommendation (feedback), Analytics |
| `tool.verified` | Tools & Registry (P1) | Recommendation, RAG |
| `policy.blocked` | Policy Engine | Audit, Analytics |
| `consent.granted` | Identity & Tenancy | всё, что трогает внешние данные |
| `consent.revoked` | Identity & Tenancy | RAG, Tools, Analytics |
| `subscription.changed` | Billing (P1) | Entitlement |
| `partner.attributed` | Growth / Partners (P1) | Billing, Analytics |

## 3. Сущности P0

| Сущность | S | Владелец | Стадии |
| --- | --- | --- | --- |
| Person | `02_DOMAIN_MODEL_SPEC` | Identity & Tenancy | 03, 04 |
| Tenant | `38_TENANCY_IDENTITY_RBAC_SPEC` | Identity & Tenancy | 03, 04 |
| CareerProfile | `05_USER_PROFILE_SPEC` | Career Intelligence | 04 |
| AIProfile | `49_AI_DATA_MODEL_ADDENDUM` | AI Transformation | 04 (если нужен 05A) |
| Goal | `14_B2C_VALUE_SPEC` | Career Intelligence | 04, 08 |
| Occupation | `04_TAXONOMY_SPEC` | Career Intelligence | 02, 04 |
| Skill | `04_TAXONOMY_SPEC` | Career Intelligence | 04 |
| Task | `24_AI_TASK_MAPPING_SPEC` | Work Intelligence | 04, 05 |
| Workflow | `25_AI_WORKFLOW_SPEC` | Work Intelligence | 04, 05 |
| WorkRecipe | `29_WORK_RECIPE_SPEC` | Work Intelligence | 05, 08 |
| Tool | `26_AI_TOOL_RECOMMENDATION_SPEC` | Tools | 04, 05 |
| Recommendation | `01_SDD_ENGINE_SPEC` | Recommendation Engine | 05 |
| Evidence | `10_DATA_GOVERNANCE_PROVENANCE_SPEC` | Knowledge | 04, 05 |
| Outcome | `31_OUTCOME_ROI_ENGINE_SPEC` | Outcomes | 04, 10 |
| Source | `10_DATA_GOVERNANCE_PROVENANCE_SPEC` | Knowledge | 02, 04 |
| Consent | `13_PRIVACY_DATA_SUBJECT_SPEC` | Identity & Tenancy | 04, 08, 09 |
| PolicyDecision | `04_RULE_POLICY_ENGINE_SPEC` | Governance | 04, 05, 09 |
| AuditEvent | `11_SECURITY_ARCHITECTURE_SPEC` | Governance | 04, 09, 11 |

## 4. Контракты, которых в архиве нет

Честный список пробелов: их нужно либо спроектировать в STAGE-02 и утвердить
ADR, либо объявить вне P0.

| Пробел | Почему нужен | Куда |
| --- | --- | --- |
| Формат `WorkRecipe` как исполняемой инструкции (шаги, проверки, измеримые поля) | без него рецепт — текст, а не контракт | STAGE-02, ADR |
| Формат `Outcome` (baseline vs assisted, единицы, период) | без него исход нельзя сравнить | STAGE-02, ADR |
| Схема `Evidence` → claim → recommendation | иначе provenance нечем проверить | STAGE-02, ADR |
| Контракт consent scope (что именно разрешено) | без него consent — галочка | STAGE-02, ADR-0005 |
| Формат policy decision reason codes | иначе блокировки не объяснить | STAGE-05 |
| Контракт tenant scope для производных индексов | утечки через индексы | STAGE-06 |

## 5. Как проверяется

```bash
python tools/runbook_validate.py --stage ALWAYS
```

Проверки целостности не дадут потерять контракт незаметно: реестр этапов,
карточки, скиллы и декларации сверяются механически.

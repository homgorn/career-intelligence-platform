# SPEC_INDEX — индекс спецификаций архива

`career-intelligence-research-specs-v02/` — единственный источник спецификаций,
только на чтение. Этот файл — навигация и статусы.

Полный machine-readable список: `docs/specs/SPEC_INDEX_DATA.tsv`
(имя, размер, sha256; без заголовка, 109 строк).
Кураторские статусы: `docs/specs/SPEC_STATUS.json`.
Перегенерация: `python tools/gen_spec_index.py`.

## Как пользоваться

1. У каждой задачи есть `spec_refs` — файл и раздел.
2. Спека со статусом `conflict` требует ADR до кода.
3. Спека со статусом `superseded` не используется, только как исторический контекст.
4. Если темы нет в индексе — это OPEN QUESTION, а не повод додумать.
5. Молчаливое дополнение типов и кардинальностей запрещено: сначала контракт
   на утверждение, потом код.

## Статусы

| Статус | Значение |
| --- | --- |
| `canonical` | канон для своей темы, можно опираться напрямую |
| `conflict` | есть вторая версия той же темы, нужен ADR |
| `superseded` | заменён более поздним документом |
| `reference` | справочник, не контракт |
| `deferred` | тема отложена в P1/P2 |

<!-- GENERATED:BEGIN -->
## Полный индекс

Всего файлов: **109**. Полные sha256 — в `SPEC_INDEX_DATA.tsv`.

| Файл | Статус | P0 | sha256 (12) | Примечание |
| --- | --- | --- | --- | --- |
| `00_INDEX.md` | reference | low | `da76d03d1ce9` | навигация по v01/v02, не контракт |
| `00_MASTER_ARCHITECTURE.md` | canonical | high | `7dc7623a5132` | верхнеуровневый контракт продукта и bounded contexts |
| `01_PRODUCT_THESIS_AND_CRITIQUE.md` | reference | medium | `158e1d668081` | продуктовая теза и разбор ошибок |
| `01_SDD_ENGINE_SPEC.md` | canonical | high | `504896b20442` | pipeline и decision record движка |
| `02_COMPETITOR_RESEARCH.md` | reference | medium | `79334bd15c7c` | позиционирование; «всё в одном» не дифференциатор |
| `02_DOMAIN_MODEL_SPEC.md` | canonical | high | `5c924d90d675` | канон предметной модели для P0 |
| `03_EVENT_CONTRACTS_SPEC.md` | canonical | high | `613d9124f16d` | 17 канонических событий и envelope |
| `03_MARKET_AND_DATA_FOUNDATION.md` | canonical | medium | `514ab21ff7e0` | O*NET/ESCO/Lightcast, market snapshot |
| `04_RULE_POLICY_ENGINE_SPEC.md` | canonical | high | `4fd348bb8502` | typed policy, ALLOW/DENY/GUARDRAILS/HUMAN |
| `04_TAXONOMY_SPEC.md` | canonical | high | `dfb493fab728` | требует crosswalk-ADR (O*NET/ESCO/местная) |
| `05_GATES_AND_ADAPTERS_SPEC.md` | canonical | high | `b1fea6216b58` | обязательные gates и границы адаптеров |
| `05_USER_PROFILE_SPEC.md` | canonical | high | `b7adf1016409` | структура CareerProfile и evidence hierarchy |
| `06_ADAPTIVE_QUIZ_SPEC.md` | deferred | low | `198b1c549403` | P1: адаптивный quiz не обязателен в P0 |
| `06_LLM_PLATFORM_SPEC.md` | canonical | high | `bfec2c4fbf7e` | условный этап STAGE-06 |
| `07_RAG_WIKI_INDEX_SPEC.md` | canonical | high | `7001ee7adb74` | условный этап STAGE-06 |
| `07_RESUME_INGESTION_SPEC.md` | canonical | medium | `6601e2766cd9` | в P0 только если пилот требует резюме |
| `08_KNOWLEDGE_GRAPH_SPEC.md` | deferred | low | `b8d3d4799575` | P2, STAGE-07 |
| `08_MATCHING_SCORING_SPEC.md` | canonical | medium | `98418e0193c8` | 16 измерений соответствия, отказ от ложной точности |
| `09_CAREER_PATH_SPEC.md` | deferred | low | `631fe9d1f335` | P1: переходы и adjacent moves |
| `09_DATABASE_ARCHITECTURE_SPEC.md` | canonical | high | `da33310525e7` | polyglot, PostgreSQL как system of record |
| `10_DATA_GOVERNANCE_PROVENANCE_SPEC.md` | canonical | high | `1a3f4324a90e` | lineage, claim object, коррекции версиями |
| `10_SKILL_GAP_AND_LEARNING_SPEC.md` | deferred | low | `19276b560495` | P1: skill gap и learning recommendation |
| `11_JOB_MATCHING_SPEC.md` | deferred | low | `fb798b9dd3b1` | P1: сопоставление с вакансиями |
| `11_SECURITY_ARCHITECTURE_SPEC.md` | canonical | high | `df3b51a4dcf8` | threat model и controls, OWASP |
| `12_GEO_LOCALIZATION_SPEC.md` | canonical | medium | `227d171838e3` | geo affects demand/salary/license; Central Asia |
| `12_LEGAL_COMPLIANCE_SPEC.md` | canonical | high | `162e3b4c63cd` | jurisdiction-aware, counsel trigger |
| `13_PRIVACY_DATA_SUBJECT_SPEC.md` | canonical | high | `46424ea35e4c` | consent/export/delete, privacy by design |
| `13_PROFESSION_CATEGORY_SPEC.md` | canonical | medium | `49f825f27108` | модули профессий и data maturity |
| `14_B2C_VALUE_SPEC.md` | canonical | high | `402162098a01` | jobs-to-be-done, activation, anti-pattern |
| `14_EXPERIENCE_SENIORITY_SPEC.md` | canonical | medium | `5424addf176b` | seniority по scope/autonomy, не по годам |
| `15_B2B_VALUE_SPEC.md` | deferred | low | `21c3a7d6098b` | P1, STAGE-16 |
| `15_EXPLANATIONS_TRUST_SAFETY_SPEC.md` | canonical | medium | `27e04057073e` | labels stated/verified/inferred, caveats |
| `16_ADMIN_CONTENT_OPERATIONS_SPEC.md` | deferred | low | `09b79f401f2f` | P1: админка и операции с контентом |
| `16_B2B2C_AND_PARTNER_VALUE_SPEC.md` | deferred | low | `8de8dd6bb962` | P1: партнёрская дистрибуция |
| `17_MARKETPLACE_SPEC.md` | deferred | low | `b5d8953f86b8` | P1/P2: marketplace pilot |
| `17_MONETIZATION_AND_GTM_SPEC.md` | deferred | low | `6f10441d6535` | P1: монетизация и GTM |
| `18_ANALYTICS_EVALS_SPEC.md` | conflict | medium | `d61bbfeca302` | C-007: воронка и качество vs 23_ |
| `18_GROWTH_MARKETING_SPEC.md` | deferred | low | `b8069020b0b6` | P1: каналы и эксперименты |
| `19_DATA_MODEL_CONCEPTUAL.md` | superseded | low | `bf9873a9a7e1` | C-005: заменён 02_DOMAIN_MODEL_SPEC |
| `19_SEO_PROGRAMMATIC_SPEC.md` | canonical | medium | `a2e4ed95ada9` | страницы только с уникальной ценностью |
| `20_CONTENT_ENGINE_SPEC.md` | deferred | low | `d979a58c599c` | P1: контентная система |
| `20_OPEN_QUESTIONS_AND_RESEARCH_BACKLOG.md` | canonical | high | `34e912cc94ee` | 15 открытых вопросов и 5 экспериментов |
| `21_PROFESSION_MODULE_TEMPLATE.md` | reference | medium | `c0a5cc0774bb` | шаблон модуля профессии |
| `21_SALES_CRM_SPEC.md` | deferred | low | `0ea525af4ac8` | P1: CRM и revenue operations |
| `22_BILLING_MONETIZATION_SPEC.md` | deferred | low | `493cf2743ea1` | P1: модели монетизации |
| `22_RESEARCH_CRITIQUE.md` | reference | medium | `8060596788c1` | уверенность гипотез и главные риски |
| `23_AI_PROFESSION_INTELLIGENCE_SPEC.md` | canonical | high | `2b16a79d0715` | ядро AI-слоя, task-level classification |
| `23_ANALYTICS_PRODUCT_METRICS_SPEC.md` | canonical | high | `d5cc176ea21e` | метрики и north-star |
| `24_AI_TASK_MAPPING_SPEC.md` | canonical | high | `f38b1b6691c0` | task schema, applicability rubric, coverage |
| `24_EVALUATION_AND_BENCHMARKS_SPEC.md` | conflict | medium | `86f5eef94664` | C-001: eval продукта vs 47_ |
| `25_AGENT_RUNTIME_SPEC.md` | deferred | low | `c0a44282ddf4` | P2, STAGE-18/агентский слой |
| `25_AI_WORKFLOW_SPEC.md` | canonical | medium | `bca220838ea9` | workflow contract и 7 паттернов |
| `26_AI_TOOL_RECOMMENDATION_SPEC.md` | canonical | medium | `3a70971c2458` | tool card, hard constraints, currentness |
| `26_MCP_TOOL_PLUGIN_SPEC.md` | deferred | low | `fcbb08ada0d6` | P1, STAGE-18 |
| `27_AI_SKILL_GAP_SPEC.md` | deferred | low | `e0cfd535f3d5` | P1: AI-навыки и барьеры |
| `27_SKILLS_PLUGIN_MAPPING_SPEC.md` | canonical | medium | `b142f664eb30` | маппинг задач на навыки; plugin не продукта |
| `28_AI_READINESS_SPEC.md` | canonical | medium | `d8d377527f50` | уровни готовности 0–5 |
| `28_BEGINNER_ONBOARDING_AND_ADOPTION_SPEC.md` | canonical | high | `d09224923422` | journey и три режима |
| `29_AI_LEVERAGE_AND_IMPACT_SPEC.md` | canonical | medium | `9281735fbd98` | экономика leverage, guardrails |
| `29_WORK_RECIPE_SPEC.md` | canonical | high | `b4347989657f` | центральная сущность и формула ранжирования |
| `30_AI_AGENT_AUTOMATION_SPEC.md` | deferred | low | `3033d099fbf7` | P2: лестница автономности A0–A5 |
| `30_IMPLEMENTATION_PACKAGES_SPEC.md` | superseded | low | `739da539e42a` | C-003: поглощён 37_ |
| `31_AI_OUTCOME_FEEDBACK_SPEC.md` | canonical | medium | `f6a5de114521` | обратная связь и поля outcome |
| `31_OUTCOME_ROI_ENGINE_SPEC.md` | canonical | high | `14b98fb10704` | expected/observed value, decision bands |
| `32_AI_PROFESSION_MODULE_TEMPLATE.md` | reference | medium | `978810a284b2` | расширенный шаблон AI-модуля |
| `32_HUMAN_REVIEW_ESCALATION_SPEC.md` | canonical | medium | `d552ad5c0995` | где автоматизация обязана остановиться |
| `33_BEGINNER_AI_ONBOARDING_SPEC.md` | canonical | high | `2e9d59938a5d` | принципы, 8 шагов, safety |
| `33_CHANGE_MANAGEMENT_SPEC.md` | superseded | low | `860d21e74996` | C-004: поглощён 46_ |
| `34_SUPPORT_OPERATIONS_SPEC.md` | deferred | low | `8f791ddca639` | P1: поддержка и SLA |
| `34_TOOL_PLUGIN_INTEGRATION_CATALOG_SPEC.md` | deferred | low | `4fa3c3cbc431` | P1: каталог инструментов и freshness |
| `35_AI_LEARNING_PATHS_SPEC.md` | deferred | low | `cdd393a54666` | P1: learning paths L0–L5 |
| `35_LOCALIZATION_ACCESSIBILITY_SPEC.md` | superseded | low | `4db5256b54ab` | C-002: поглощён 44_ |
| `36_DOCUMENTATION_AND_RUNBOOKS_SPEC.md` | deferred | low | `e26b5e306a90` | P1: документация workflow |
| `36_SEARCH_WIKI_CONTENT_INDEX_MANIFEST.md` | canonical | medium | `3d91574585a5` | логические индексы и canonical rule |
| `37_API_CONTRACTS_SPEC.md` | canonical | high | `b24827ca19de` | краткий: versioned, idempotent, typed errors |
| `37_IMPLEMENTATION_PACKAGES_SPEC.md` | canonical | medium | `5c2cdd9de361` | лестница из 6 пакетов и guardrails |
| `38_AI_ADOPTION_BARRIERS_SPEC.md` | canonical | medium | `69e8e41d820b` | C-006: таксономия барьеров |
| `38_TENANCY_IDENTITY_RBAC_SPEC.md` | canonical | high | `2b671da6e59c` | роли, scopes, ABAC, isolation tests |
| `39_BILLING_ENTITLEMENT_SPEC.md` | deferred | low | `38b5e6aff8ea` | P1: entitlement отдельно от платежей |
| `39_IMPLEMENTATION_COST_AND_ROI_SPEC.md` | canonical | medium | `fb8da0409e3b` | cost components и sensitivity analysis |
| `40_DEVOPS_SRE_SPEC.md` | canonical | high | `0d4eb50eaa23` | среды, release gates, error budgets |
| `40_MANAGED_AI_SERVICE_SPEC.md` | deferred | low | `13da1e7fc611` | P2: done-for-you |
| `41_INTEGRATIONS_AND_INTEROPERABILITY_SPEC.md` | deferred | low | `1f7a4b3be359` | P1: методы интеграций и metadata |
| `41_TESTING_QA_SPEC.md` | canonical | high | `ce6ad297099e` | слои тестирования и AI-тесты |
| `42_AI_GOVERNANCE_PRIVACY_SAFETY_SPEC.md` | canonical | high | `e05774a1ee7c` | data classification, high-consequence domains |
| `42_OBSERVABILITY_SPEC.md` | canonical | high | `a4bb00e7c79b` | trace до outcome, redaction в логах |
| `43_AI_ENABLED_ROLES_AND_NEW_BUSINESS_SPEC.md` | deferred | low | `4ff56103b3bb` | P1/P2: новые роли и бизнесы |
| `43_RESEARCH_BACKLOG_MASTER.md` | canonical | high | `cff001f27221` | register неопределённостей; не строить под нерешённое |
| `44_LOCALIZATION_ACCESSIBILITY_SPEC.md` | canonical | medium | `a53682e9685d` | проверка доступности инструмента по стране |
| `44_MASTER_ROADMAP_P0_P2.md` | canonical | high | `c72a4ad53185` | P0 шаги 1–8 и gate по доказательству |
| `45_HUMAN_SUPPORT_AND_ESCALATION_SPEC.md` | deferred | low | `f35935d25519` | P1: поддержка и escalation triggers |
| `45_IDE_EXECUTION_BACKLOG_SCHEMA.md` | canonical | high | `ce01eb154c61` | поля задачи и agent rule |
| `46_CHANGE_MANAGEMENT_SPEC.md` | canonical | medium | `27675efaae37` | 10 шагов и team readiness |
| `46_GATES_CHECKLIST.md` | canonical | high | `09254db013e9` | 8 gate-чеклистов |
| `47_ADAPTER_CATALOG.md` | canonical | medium | `30bfd1d75622` | категории адаптеров; exit strategy |
| `47_EVALUATION_AND_BENCHMARKS_SPEC.md` | conflict | medium | `e8ed3a4fe660` | C-001: test set и dimensions vs 24_ |
| `48_BEGINNER_UX_AND_PRODUCT_JOURNEY_SPEC.md` | canonical | high | `86c405f95a8c` | простой/продвинутый/экспертный режимы |
| `48_SKILL_PATHS_FOR_IDE.md` | reference | low | `20a4b94c0486` | предлагаемый путь навыков для IDE |
| `49_AI_DATA_MODEL_ADDENDUM.md` | canonical | high | `793a042b2e21` | AI-слой данных; применять по STAGE-05A |
| `49_DEFINITION_OF_DONE_GLOBAL.md` | canonical | high | `5636d6c724f9` | DoD: customer value, correctness, ops, measurement |
| `50_RESEARCH_SOURCES_MASTER.md` | reference | medium | `7f5a10cbc11e` | источники: Anthropic, McKinsey, ESCO, NIST, OWASP, MCP |
| `50_ROADMAP_AND_RESEARCH_BACKLOG_V02.md` | reference | medium | `d84b115e72b6` | фазы MVP и kill criteria |
| `51_MISSING_LAYERS_AND_PRODUCT_CRITIQUE.md` | reference | high | `99d8e522363c` | 15 пропущенных слоёв и стратегический риск |
| `52_RESEARCH_SOURCES_V02.md` | reference | medium | `6fc70f98a816` | вендорские документы и 5 продуктовых выводов |
| `IDE_TASK_TEMPLATE.json` | canonical | high | `5ff0eb038e61` | шаблон задачи |
| `MASTER_ARCHIVE_AUDIT.md` | reference | low | `d03fdd8a97d1` | состав архива и ограничения |
| `MASTER_DEPENDENCY_GRAPH.json` | canonical | high | `46e9417fd47a` | базовый граф задач P0/P1/P2 |
| `MASTER_FILE_INDEX.md` | reference | low | `b9b2cf83f73b` | заявляет 108 файлов, фактически 109 (самоё себя не перечисляет) |
| `MASTER_MANIFEST.json` | reference | low | `95384ccb27d9` | манифест слоёв, контекстов и gates |
<!-- GENERATED:END -->

## Конфликты, требующие ADR

### C-001. Evaluation: 24 vs 47

- `24_EVALUATION_AND_BENCHMARKS_SPEC.md` — offline/online evals, benchmark sets,
  release gate по регрессии метрик.
- `47_EVALUATION_AND_BENCHMARKS_SPEC.md` — test set, evaluation dimensions,
  методы, drift, acceptance criteria для workflow.

**Цена решения:** два разных набора тестов и два понимания «release gate».
**Предрешение:** 24 — канон метрик и гейтов; 47 влить разделом «test set
и dimensions». Оформить ADR в STAGE-02.

### C-002. Localization: 35 vs 44

- `35_LOCALIZATION_ACCESSIBILITY_SPEC.md` — короткий оглавок.
- `44_LOCALIZATION_ACCESSIBILITY_SPEC.md` — полный: измерения, geography,
  verification по стране, accessibility, language quality, acceptance criteria.

**Предрешение:** 44 — канон, 35 — `superseded`.

### C-003. Implementation packages: 30 vs 37

- `30_IMPLEMENTATION_PACKAGES_SPEC.md` — список пакетов + no-value gate.
- `37_IMPLEMENTATION_PACKAGES_SPEC.md` — лестница из 6 пакетов, package card,
  guardrails, acceptance criteria.

**Предрешение:** 37 — канон, правило «no-value gate» из 30 сохранить в нём.

### C-004. Change management: 33 vs 46

- `33_CHANGE_MANAGEMENT_SPEC.md` — стадии, владельцы, readiness gates.
- `46_CHANGE_MANAGEMENT_SPEC.md` — шаги, team readiness, job impact,
  acceptance criteria.

**Предрешение:** 46 — канон процесса, readiness gates из 33 сохранить.

### C-005. Три модели данных: 02 vs 19 vs 49

- `02_DOMAIN_MODEL_SPEC.md` — 27 сущностей, ownership, identity.
- `19_DATA_MODEL_CONCEPTUAL.md` — 24 сущности, другие имена (`User`, `Profile`,
  `CareerGoal`).
- `49_AI_DATA_MODEL_ADDENDUM.md` — 19 AI-сущностей, provenance-поля,
  state fields, avoid-list.

**Цена решения:** самая высокая в архиве. **Предрешение:** 02 — канон для P0;
19 — `superseded`; 49 — применять как addendum, только если STAGE-05A обосновал
LLM. Оформить `ADR-0003`.

### C-006. Новичковая адаптация: 28 vs 33 vs 38

- `28_BEGINNER_ONBOARDING_AND_ADOPTION_SPEC.md` — путь, три режима, failure recovery.
- `33_BEGINNER_AI_ONBOARDING_SPEC.md` — принципы, 8-шаговый journey, safety.
- `38_AI_ADOPTION_BARRIERS_SPEC.md` — таксономия барьеров, diagnostics, ethics.

**Предрешение:** не конфликт, а пересечение. Роли: 28 — journey, 33 — принципы
и safety, 38 — диагностика барьеров. Закрепить в ADR, чтобы IDE не смешивал.

### C-007. Аналитика: 18 vs 23

- `18_ANALYTICS_EVALS_SPEC.md` — воронка, recommendation quality, fairness,
  human evaluation.
- `23_ANALYTICS_PRODUCT_METRICS_SPEC.md` — метрики продукта.

**Предрешение:** 23 — канон определений метрик, 18 — воронка и качество
рекомендаций. Закрепить в ADR.

### C-008. Расхождение индекса архива

`MASTER_FILE_INDEX.md` заявляет 108 файлов, на диске 109: индекс не перечисляет
сам себя. Примечание: не блокер, но при любых подсчётах брать факт с диска
(`SPEC_INDEX_DATA.tsv`), а не заявленное число.

## Исключенные материалы

| Материал | Статус |
| --- | --- |
| `old specs не трогать пока.7z` | не распаковывать, не читать |
| Папка архива целиком | read-only, не копировать в `docs/specs` |
| `MASTER_FILE_INDEX.md`, `MASTER_MANIFEST.json` | служебные, не контракты |

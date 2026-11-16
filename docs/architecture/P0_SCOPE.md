# P0_SCOPE

Что обязательно в P0, что отложено и почему. Основание: `44_MASTER_ROADMAP_P0_P2.md`,
`51_MISSING_LAYERS_AND_PRODUCT_CRITIQUE.md`, `00_INDEX.md`.

P0 должен доказать **полный customer-value loop на одном конкретном workflow**.
Всё, что не нужно для этого доказательства, откладывается — даже если спека
подробная и красивая (`AGENTS.md`, правило 18).

## P0 REQUIRED

### Люди и доступ

- Tenant, Person, Organization; auth; RBAC foundation; tenant isolation с
  автоматическими negative-тестами (`38_TENANCY_IDENTITY_RBAC_SPEC.md`).
- Consent, PolicyDecision, AuditEvent (`13_PRIVACY_DATA_SUBJECT_SPEC.md`,
  `04_RULE_POLICY_ENGINE_SPEC.md`, `11_SECURITY_ARCHITECTURE_SPEC.md`).

### Предметная область (срез пилота)

- CareerProfile и AIProfile как отдельные сущности (`02_DOMAIN_MODEL_SPEC.md`).
- Occupation, Skill, Task, Workflow — только в объёме выбранной профессии.
- WorkRecipe как самостоятельная сущность (`29_WORK_RECIPE_SPEC.md`).
- Goal, Recommendation, Evidence, Outcome, Source
  (`01_SDD_ENGINE_SPEC.md`, `10_DATA_GOVERNANCE_PROVENANCE_SPEC.md`).
- Tool — в объёме, необходимом для первой WorkRecipe.

### Движок

- Deterministic scoring и policy gates (`01_SDD_ENGINE_SPEC.md`,
  `04_RULE_POLICY_ENGINE_SPEC.md`). LLM — только по обоснованию STAGE-05A.
- Decision record с provenance и engine version.

### Поверхность

- Один vertical slice: Goal → Task → Diagnosis → Recommendation → WorkRecipe →
  Implementation → Verification → Outcome (`48_BEGINNER_UX_AND_PRODUCT_JOURNEY_SPEC.md`).
- Три режима: сделаю сам / проведи меня / помоги сделать
  (`28_BEGINNER_ONBOARDING_AND_ADOPTION_SPEC.md`).
- Дистрибуция MVP: лендинг + 10–30 страниц + один канал
  (`44_MASTER_ROADMAP_P0_P2.md`, шаги 6–7).

### Измерение

- События из замороженного каталога (`03_EVENT_CONTRACTS_SPEC.md`).
- time-to-first-value, recommendation acceptance, implementation completion,
  verified outcome, cost per verified outcome (`23_ANALYTICS_PRODUCT_METRICS_SPEC.md`).
- North-star привязан к outcome, а не к активности.

### Инженерия

- PostgreSQL как system of record; migrations; rollback
  (`09_DATABASE_ARCHITECTURE_SPEC.md`).
- Observability: trace request → engine → output → action → outcome
  (`42_OBSERVABILITY_SPEC.md`).
- Security baseline и isolation tests (`11_SECURITY_ARCHITECTURE_SPEC.md`).
- Тесты: unit, integration, contract, authorization, tenant leakage
  (`41_TESTING_QA_SPEC.md`).

## P1 DEFERRED

| Тема | Спека | Причина |
| --- | --- | --- |
| Расширение таксономии и библиотеки рецептов | `04_TAXONOMY_SPEC` (рост) | сначала один профессионный срез |
| Quiz / adaptive assessment | `06_ADAPTIVE_QUIZ_SPEC` | не обязателен для первого value loop |
| Resume ingestion и multi-resume | `07_RESUME_INGESTION_SPEC` | только если пилот докажет необходимость |
| Job matching | `11_JOB_MATCHING_SPEC` | P0 заканчивается исходом по WorkRecipe |
| Career path / transitions | `09_CAREER_PATH_SPEC` | требует накопленных outcomes |
| Tool registry и MCP | `26_MCP_TOOL_PLUGIN_SPEC`, `47_ADAPTER_CATALOG` | после первых ручных рекомендаций |
| Learning paths | `35_AI_LEARNING_PATHS_SPEC` | после подтверждённого спроса |
| B2B diagnostic | `15_B2B_VALUE_SPEC` | требует пилота и P0 gate |
| Partner program | `16_B2B2C_AND_PARTNER_VALUE_SPEC` | после продуктового fit |
| SEO/content scale | `18_GROWTH_MARKETING_SPEC`, `20_CONTENT_ENGINE_SPEC` | после P0 gate; минимум уже в P0 |
| CRM/sales | `21_SALES_CRM_SPEC` | самообслуживание в P0 |
| Billing complexity | `39_BILLING_ENTITLEMENT_SPEC` | P0 — минимальная монетизация |

## P2 DEFERRED

| Тема | Спека | Причина |
| --- | --- | --- |
| Knowledge graph | `08_KNOWLEDGE_GRAPH_SPEC` | derived projection после стабилизации модели |
| Agent runtime / MCP | `25_AGENT_RUNTIME_SPEC`, `26_MCP_TOOL_PLUGIN_SPEC` | лестница автономности A0–A5 не нужна для P0 |
| Managed AI service | `40_MANAGED_AI_SERVICE_SPEC` | требует готовых пакетов и качества |
| Enterprise governance/procurement | `42_AI_GOVERNANCE_PRIVACY_SAFETY_SPEC` (расшижение) | после B2B |
| Marketplace | `17_MARKETPLACE_SPEC` | только после стандартов качества и vetting |
| Data moat / benchmarks | `44_MASTER_ROADMAP_P0_P2.md` | сетевые эффекты позже |
| Internationalization scale | `44_LOCALIZATION_ACCESSIBILITY_SPEC` (масштаб) | пилот ограничен одной страной |

## Явные non-goals P0

- Не «всё в одном»: каталог AI-инструментов, LMS, маркетплейс, автоматизация-билдер
  (`02_COMPETITOR_RESEARCH.md`, `51_MISSING_LAYERS_AND_PRODUCT_CRITIQUE.md`).
- Не строить graph DB ради технологии (`09_DATABASE_ARCHITECTURE_SPEC.md`).
- Не оптимизировать под количество рекомендаций, промптов и AI-вызовов
  (`00_MASTER_ARCHITECTURE.md`).
- Не выпускать в P0 ни одного P1/P2 блока «заранее».

## OPEN QUESTIONS, влияющие на границу P0

1. Нужен ли LLM в P0 и для каких шагов — решает STAGE-05A.
2. Требует ли пилот загрузку резюме — тогда `07_RESUME_INGESTION_SPEC`
   частично попадает в P0.
3. Какая таксономия — влияет на состав справочника Occupation/Skill.
4. Какой первый шаг value loop не требует LLM — может упростить P0.

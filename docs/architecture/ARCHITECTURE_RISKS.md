# ARCHITECTURE_RISKS

Риски, найденные аудитом архива. Severity: CRITICAL / HIGH / MEDIUM / LOW.
Evidence — файл и раздел. Mitigation привязана к этапам runbook'а.

| ID | Риск | Severity | Evidence | Влияние | Mitigation | Этап |
| --- | --- | --- | --- | --- | --- | --- |
| R-01 | Архив внутренне противоречив: 3 модели данных, 2 версии evaluation, localization, packages, change management | HIGH | `SPEC_INDEX.md`, C-001…C-007 | IDE сверяет списки и додумывает кардинальности | `SPEC_INDEX.md` + ADR до кода; `conflict` → ADR | STAGE-00/02 |
| R-02 | Спеки — оглавления (~1,2 КБ), а не типизированные контракты | HIGH | все 109 файлов | «Реализуй строго по спеке» невыполнимо без додумывания | Contract freeze: DDL/API/events через ADR | STAGE-02 |
| R-03 | Стек не выбран (язык, фреймворк, фронтенд, хостинг) | MEDIUM | `00_INDEX.md`, `48_SKILL_PATHS_FOR_IDE.md` | Foundation может быть построен на неверном стеке | ADR-0002 после пилота; storage-стек уже задан спекой 09 | STAGE-00A |
| R-04 | Таксономия не выбрана: O*NET / ESCO / местная / гибрид | HIGH | `04_TAXONOMY_SPEC.md`, `03_MARKET_AND_DATA_FOUNDATION.md` | Качество Occupation/Skill и нормализация | Решение в `PILOT_DECISION.md`; crosswalk-ADR | STAGE-00A/02 |
| R-05 | Юрисдикция неизвестна → legal gate невозможен | HIGH | `12_LEGAL_COMPLIANCE_SPEC.md`, `20_OPEN_QUESTIONS_AND_RESEARCH_BACKLOG.md` | Нет consent/delete/export требований | Страна фиксируется в пилоте; counsel trigger | STAGE-00A |
| R-06 | Распределение отсутствовало в исходной цепочке | MEDIUM | `44_MASTER_ROADMAP_P0_P2.md` (шаги 6–7) | P0 gate не на ком проверять | STAGE-08A: лендинг + 10–30 страниц + канал | STAGE-08A |
| R-07 | Scope explosion: архив покрывает 8 продуктовых слоёв | HIGH | `51_MISSING_LAYERS_AND_PRODUCT_CRITIQUE.md`, `02_COMPETITOR_RESEARCH.md` | Продукт расползается, ценностная петля не закрывается | `P0_SCOPE.md`; gates по доказательству | все |
| R-08 | LLM может быть построен в P0 без необходимости | MEDIUM | `29_WORK_RECIPE_SPEC.md`, `51_…` («do not use AI here») | Деньги, риск, задержка | STAGE-05A: `LLM_REQUIRED`/`DEFERRED`/`PARTIAL` | STAGE-05A |
| R-09 | События аналитики определяются после кода | MEDIUM | `03_EVENT_CONTRACTS_SPEC.md` vs `PROMPT 10` | Инструментировать придётся задним числом | Каталог событий замораживается в STAGE-02 | STAGE-02/10 |
| R-10 | Tenant isolation и security-тесты появятся только в STAGE-03/09 | MEDIUM | `38_TENANCY_IDENTITY_RBAC_SPEC.md`, `11_SECURITY_ARCHITECTURE_SPEC.md` | Поздно обнаруженная утечка дороже | Isolation tests сразу в domain/data; security gate дважды | STAGE-04/09 |
| R-11 | Freshness каталога инструментов: цены и доступность меняются | MEDIUM | `34_TOOL_PLUGIN_INTEGRATION_CATALOG_SPEC.md`, `26_AI_TOOL_RECOMMENDATION_SPEC.md` | Устаревшая рекомендация убивает доверие | Versioned availability + verification dates (P1) | STAGE-18 |
| R-12 | Пользователь может уйти в «красивый отчёт без действия» | HIGH | `14_B2C_VALUE_SPEC.md`, `48_BEGINNER_UX_AND_PRODUCT_JOURNEY_SPEC.md` | Ценности нет, удержания нет | UX требует next action на каждом экране; outcome обязателен | STAGE-08/12 |
| R-13 | Ложная численная точность («93%», «87%») | MEDIUM | `08_MATCHING_SCORING_SPEC.md`, `22_RESEARCH_CRITIQUE.md` | Доверие и legal risk | Qualitative levels + calibration; explainability | STAGE-05/08 |
| R-14 | Runbook не имеет машиночитаемых проверок | LOW | весь `docs/ops/` | DoD субъективен, дрейф незаметен | Assertions + validator + skills | готово |
| R-15 | `MASTER_FILE_INDEX.md` заявляет 108 файлов при 109 на диске | LOW | C-008 в `SPEC_INDEX.md` | Путаница в подсчётах | Брать факт с диска через TSV | — |
| R-16 | Решения человека рассредоточены и не подписаны | MEDIUM | `44_MASTER_ROADMAP_P0_P2.md`, `20_OPEN_QUESTIONS_AND_RESEARCH_BACKLOG.md` | Gate нельзя оспорить, повторный запуск дорог | `signed_by`/`signed_at` на всех human-документах; WAIT в валидаторе | все |

## Общая картина

Преобладают риски **не технические, а объёмные и решений**: пилот не выбран,
стек не выбран, юрисдикция не выбрана, scope может расползтись. Это
подтверждает порядок runbook'а: сначала Human-решение по пилоту, потом
контракты, потом код.

Технические риски (tenant isolation, security, provenance) покрыты спеками,
но их реализация сдвинута на STAGE-03/04/09 — это приемлемо, если P0 не
выходит в production до прохождения gate.

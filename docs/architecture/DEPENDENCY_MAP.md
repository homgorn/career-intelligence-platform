# DEPENDENCY_MAP

Зависимости между подсистемами и артефактами. Направление стрелки:
«предоставляет». Обратная стрелка — запрет или ограничение.

## 1. Зависимости подсистем

```text
Identity & Tenancy ───────────────▶ все остальные (tenant scope, authz)
Market/Taxonomy data ─────────────▶ Career Intelligence
Career Intelligence ──────────────▶ Matching / Recommendation
Work Intelligence ────────────────▶ Recommendation / WorkRecipe
Recommendation Engine ────────────▶ WorkRecipe / Implementation
Outcomes ─────────────────────────▶ Recommendation feedback
Knowledge & Research ─────────────▶ Recommendation (evidence), RAG
Tools & Adapters ─────────────────▶ Implementation, Automation
LLM / RAG (условно) ──────────────▶ Extraction, mapping, synthesis
Analytics / Observability ◀──────── все (telemetry)
Governance (policy, security, legal) ─▶ gates на каждом шаге
```

## 2. Порядок разблокировки P0

```text
PILOT_DECISION (человек)
        │
        ▼
Contracts freeze (events, data model, API)
        │
        ├──────────────► Foundation (tenancy, auth, migrations)
        │                        │
        │                        ▼
        │               Domain & Data (18 сущностей)
        │                        │
        │                        ▼
        │               Recommendation Engine + policy gates
        │                        │
        │                        ▼
        │               [STAGE-05A: нужен ли LLM?]
        │                        │
        │              ┌─────────┴─────────┐
        │              ▼                   ▼
        │       Website/Onboarding    LLM/RAG (условно)
        │              │                   │
        │              └─────────┬─────────┘
        │                        ▼
        │                 Analytics + outcome
        │                        │
        │                        ▼
        │                 Distribution MVP
        │                        │
        └────────────────────────▼
                         Vertical slice E2E
                                 │
                                 ▼
                           P0 value gate
```

## 3. Запрещённые направления зависимостей

| Запрет | Обоснование |
| --- | --- |
| Domain layer → vendor SDK | `05_GATES_AND_ADAPTERS_SPEC.md` |
| Derived index → authoritative write | `09_DATABASE_ARCHITECTURE_SPEC.md` |
| LLM → policy/security/legal/billing decision | `01_SDD_ENGINE_SPEC.md`, `04_RULE_POLICY_ENGINE_SPEC.md` |
| Gate → обход ради скорости | `46_GATES_CHECKLIST.md` |
| P1/P2 feature → до своего gate | `44_MASTER_ROADMAP_P0_P2.md` |
| Prompt → хранение бизнес-правила | `04_RULE_POLICY_ENGINE_SPEC.md` |
| Testimonial/metric → без baseline и метода | `29_AI_LEVERAGE_AND_IMPACT_SPEC.md` |
| История evidence → перезапись | `10_DATA_GOVERNANCE_PROVENANCE_SPEC.md` |

## 4. Критический путь P0

1. Пилот выбран и подписан → без этого всё ниже заблокировано.
2. Каталог событий заморожен → от него зависит аналитика и E2E.
3. Target-схема P0 заморожена → от неё зависит domain/data.
4. Policy gates работают → без них recommendation не выпускается.
5. Outcome пишется и измеряется → без этого P0 gate не на чем проверять.
6. Дистрибуция есть → без неё нет пользователей для gate.

Узкие места: шаг 1 (человеческая петля), шаг 4 (корректность политик),
шаг 5 (измеримость исхода), шаг 6 (распределение усилий).

## 5. Зависимости артефактов runbook

| Артефакт | Зависит от | Кто потребляет |
| --- | --- | --- |
| `PILOT_DECISION.md` | STAGE-00 | всё дальше |
| `EVENT-CATALOG.md` | STAGE-00, спека 03 | analytics, E2E, audit |
| `DATA-MODEL-P0.md` | PILOT, спека 02/09 | foundation, domain, tests |
| `API-FOUNDATION.md` | спеки 37/38 | surface, domain |
| `MASTER_BACKLOG.json` | PILOT, контракты | selector, executor |
| `NEXT_TASK.md` | backlog, gates | STAGE-13/14 |
| `RELEASE-GATE-P0.md` | метрики, E2E, gates | разрешение P1 |
| `PRODUCTION-GATE.md` | все gates | выпуск |

## 6. Внутренние зависимости архива

Конфликтующие пары и их влияние на порядок — `docs/specs/SPEC_INDEX.md`,
раздел «Конфликты, требующие ADR». Правило: ADR раньше кода, который опирается
на спеку со статусом `conflict`.

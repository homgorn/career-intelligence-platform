# docs — рабочая документация проекта

Единственный источник спецификаций — `../career-intelligence-research-specs-v02/`
(только на чтение). Здесь живут артефакты выполнения.

## Навигация

| Путь | Что это |
| --- | --- |
| `ops/RUNBOOK.md` | порядок этапов, реестр, запреты |
| `ops/stages/` | карточки этапов STAGE-00…19 с промптами для IDE |
| `ops/STAGE-INDEX.csv` | машиночитаемый реестр этапов |
| `ops/STAGE-STATUS.md` | журнал этапов и задач |
| `specs/SPEC_INDEX.md` | канон спецификаций, конфликты, статусы |
| `specs/SPEC_INDEX_DATA.tsv` | все файлы архива с sha256 |
| `architecture/MASTER_ARCHITECTURE_MAP.md` | контексты, system of record, границы |
| `architecture/DEPENDENCY_MAP.md` | зависимости подсистем и порядок P0 |
| `architecture/P0_SCOPE.md` | что в P0, что отложено и почему |
| `architecture/ARCHITECTURE_RISKS.md` | 16 рисков с причинами и действиями |
| `architecture/OPEN_QUESTIONS.md` | реестр неопределённостей с владельцами |
| `architecture/CONTRACT_TRACEABILITY.md` | спека → артефакт → производитель → потребитель |
| `architecture/PILOT_OPTIONS.md` | кандидаты пилота (вход для STAGE-00A) |
| `architecture/GLOSSARY.md` | русский термин → английский канон |
| `decisions/` | ADR и реестр решений |
| `contracts/` | API, events, domain контракты |
| `tasks/` | бэклог и карточки задач |
| `gates/` | отчёты gate |
| `templates/` | шаблоны задач, ADR, gate report |
| `research/` | research и evidence |
| `wiki/` | продуктовая база знаний |

## Порядок работы

1. Читай `../AGENTS.md`.
2. Читай `ops/RUNBOOK.md`.
3. Получи от человека имя этапа или TASK-ID.
4. Работай по карточке этапа. Один этап за сеанс.
5. Остановись и жди человека.

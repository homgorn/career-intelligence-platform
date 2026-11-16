# skills — скиллы этапов проекта

Канонические копии скиллов OpenCode для проекта Career Intelligence /
AI Profession Intelligence. Скилл не дублирует карточку этапа: он подключает
её (`docs/ops/stages/STAGE-XX-*.md`) и добавляет границы и команду валидатора.

## Установка

Рабочий каталог OpenCode: `~/.config/opencode/skills/`.

```bash
python tools/install_skills.py            # установить или обновить все
python tools/install_skills.py --list     # что установлено
python tools/install_skills.py --status   # сравнение репо и каталога
python tools/install_skills.py --uninstall
```

Установщик копирует только папки с префиксом `ci-`, чужие скиллы в каталоге
не трогает. Без `--force` не перезаписывает уже изменённые файлы.

## Правила использования

- Скилл подключается по описанию, когда человек называет этап или задачу.
- Один этап за сеанс. Два этапа подряд не запускать.
- Решение человека (пилот, LLM, gate) скилл не подменяет.
- После этапа — валидатор и `docs/ops/STAGE-STATUS.md`.

## Состав

| Скилл | Этап |
| --- | --- |
| `ci-runbook` | маршрутизатор |
| `ci-stage-00-audit` | STAGE-00 |
| `ci-stage-00a-pilot` | STAGE-00A |
| `ci-stage-01-readiness` | STAGE-01 |
| `ci-stage-02-contracts-backlog` | STAGE-02 |
| `ci-stage-03-foundation` | STAGE-03 |
| `ci-stage-04-domain-data` | STAGE-04 |
| `ci-stage-05-recommendation` | STAGE-05 |
| `ci-stage-05a-llm-necessity` | STAGE-05A |
| `ci-stage-06-llm-rag-wiki` | STAGE-06 |
| `ci-stage-07-knowledge-graph` | STAGE-07 (P2) |
| `ci-stage-08-website-onboarding` | STAGE-08 |
| `ci-stage-08a-distribution` | STAGE-08A |
| `ci-stage-09-security-privacy-legal` | STAGE-09 |
| `ci-stage-10-analytics-outcome` | STAGE-10 |
| `ci-stage-11-vertical-slice` | STAGE-11 |
| `ci-stage-12-p0-gate` | STAGE-12 |
| `ci-stage-13-next-task` | STAGE-13 |
| `ci-stage-14-task-executor` | STAGE-14 |
| `ci-stage-15-health-check` | STAGE-15 |
| `ci-stage-16-b2b` | STAGE-16 |
| `ci-stage-17-seo-growth` | STAGE-17 |
| `ci-stage-18-tool-registry` | STAGE-18 |
| `ci-stage-19-production-readiness` | STAGE-19 |

## Как добавить скилл

1. Создай папку `skills/ci-<slug>/SKILL.md`.
2. В frontmatter укажи точное `name` и `description` с именем проекта —
   иначе скилл может сработать в чужом проекте.
3. В теле ссылайся на карточку этапа, не копируй её.
4. Добавь вызов `python tools/runbook_validate.py --stage STAGE-XX`.
5. Прогони `python tools/install_skills.py`.

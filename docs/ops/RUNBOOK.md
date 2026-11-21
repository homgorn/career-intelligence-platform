# RUNBOOK — порядок выполнения проекта

Единственный источник правды о том, что и в каком порядке делается.
Карточки этапов: `docs/ops/stages/STAGE-XX-*.md`.
Правила и ограничения: `AGENTS.md`.

## 1. Договорённость об этапе

Каждый этап — это сеанс с явным началом и явным концом:

```
TRIGGER → INPUTS → STEPS → OUTPUTS → DEFINITION OF DONE → HARD STOP → ROLLBACK
```

- **Trigger** — что должно быть завершено, чтобы этап можно было запустить.
- **Inputs** — какие артефакты и какие спеки читаются.
- **Outputs** — какие файлы создаются или меняются.
- **Definition of Done** — проверяемые признаки завершения.
- **HARD STOP** — этап окончен, ждём человека.
- **Rollback** — как отменить артефакты этапа, если он сделан неверно.

Этап нельзя «доделать позже» в том же сеансе. Нельзя начать следующий этап
в том же сеансе, даже если предыдущий прошёл идеально.

## 2. Реестр этапов

| Этап | Название | Бывший PROMPT | Archive task | Зависит от | Gate |
| --- | --- | --- | --- | --- | --- |
| STAGE-00 | Audit | PROMPT 00 | — | — | stage |
| STAGE-00A | Pilot decision (человек) | новый | TASK-P0-001 | 00 | stage + подпись человека |
| STAGE-01 | Readiness review | PROMPT 01 | — | 00, 00A | stage |
| STAGE-02 | Contracts + backlog | PROMPT 02 | TASK-P0-002 | 00A | stage |
| STAGE-03 | Foundation | PROMPT 03 | — | 02 | stage |
| STAGE-04 | Domain + data | PROMPT 04 | TASK-P0-002, P0-003 | 03 | stage |
| STAGE-05 | Recommendation engine | PROMPT 05 | TASK-P0-004 | 04 | stage |
| STAGE-05A | LLM necessity gate | новый | — | 05 | stage |
| STAGE-06 | LLM + RAG + wiki | PROMPT 06 | — | 05A (условно) | stage |
| STAGE-07 | Knowledge graph | PROMPT 07 | P2 | 02 | deferred → P2 |
| STAGE-08 | Website + onboarding | PROMPT 08 | TASK-P0-007 | 04, 05 | stage |
| STAGE-08A | Distribution MVP | новый (часть PROMPT 16) | TASK-P0-008 | 08 | stage |
| STAGE-09 | Security + privacy + legal | PROMPT 09 | — | 02 (дизайн), 11 (реализация) | stage |
| STAGE-10 | Analytics + outcome | PROMPT 10 | TASK-P0-006 | 02, 08 | stage |
| STAGE-11 | Vertical slice E2E | PROMPT 11 | TASK-P0-003…006 | 05, 08, 10 | stage |
| STAGE-12 | P0 value gate | PROMPT 12 | TASK-P0-009 | 11 | release |
| STAGE-13 | Next task selector | PROMPT 13 | recurring | после каждой задачи | — |
| STAGE-14 | Task executor | универсальный исполнитель | recurring | после 13 | stage |
| STAGE-15 | Health check | PROMPT 14 | recurring | объективный триггер | stage |
| STAGE-16 | B2B layer | PROMPT 15 | TASK-P1-004 | release P1 | release P1 |
| STAGE-17 | SEO + growth | PROMPT 16 | TASK-P1-006 | release P1 | release P1 |
| STAGE-18 | Tool / plugin registry | PROMPT 17 | TASK-P1-002 | release P1 | release P1 |
| STAGE-19 | Production readiness | PROMPT 18 | release gate | release P2 | production |

Машиночитаемая копия: `docs/ops/STAGE-INDEX.csv`.

## 3. Порядок выполнения

Обязательная последовательность до P0 gate:

```
STAGE-00 → STAGE-00A → STAGE-01 → STAGE-02 → STAGE-03 → STAGE-04
→ STAGE-05 → STAGE-05A → [STAGE-06 только если 05A обосновал LLM]
→ STAGE-08 → STAGE-08A → STAGE-09 (дизайн) → STAGE-10
→ STAGE-11 → STAGE-09 (реализация) → STAGE-12
```

`STAGE-07` — явно отложен в P2. В P0 не запускается.

После STAGE-12 цикл `STAGE-13 → STAGE-14` используется постоянно, по одной задаче
за раз, до следующего gate.

## 4. Три уровня gate

1. **Stage gate** — после каждого этапа. IDE проверяет DoD, человек подтверждает.
   Артефакт: `docs/gates/STAGE-GATE-XX.md`.
2. **Release gate** — граница P0/P1/P2. Решение принимает человек, IDE готовит
   доказательства. Не проходит по факту готовности бэклога.
   Артефакт: `docs/gates/RELEASE-GATE-P0.md`.
3. **Production gate** — перед выпуском. Внешний аудит при необходимости.
   Артефакт: `docs/gates/PRODUCTION-GATE.md`.

## 5. Единый бэклог

Один живой бэклог: `docs/tasks/MASTER_BACKLOG.json`.
ID задач берутся из `MASTER_DEPENDENCY_GRAPH.json` архива и продолжают нумерацию.
Второй граф заводить нельзя. Каждая задача — карточка `docs/tasks/P0|TASK-XXXX.md`
по шаблону `docs/templates/TASK_CARD.md` с обязательными `spec_refs`.

`docs/tasks/NEXT_TASK.md` содержит ровно одну задачу и обновляется после каждой
выполненной задачи.

## 6. Инструменты проверки

Проверка этапов частично автоматизирована. Декларация — в `docs/ops/assertions/`,
описание формата — в `docs/ops/ASSERTIONS.md`.

**Одна команда — всё, что значит «зелёный»:**

```bash
python tools/check.py                 # полный прогон (то же делает CI)
python tools/check.py --quick         # без перегенерации индекса и STAGE-00
python tools/check.py --skip-info     # без информационного блока будущих этапов
python tools/check.py --json          # машиночитаемый результат
```

Раннер выполняет: целостность JSON/CSV, `ruff check`, `ruff format --check`,
`pytest`, перегенерацию индекса спек + `git diff`-гейт (анти-дрейф архива),
валидаторы `ALWAYS` и `STAGE-00`, селектор (ожидаемо заблокирован пилотом,
код 2 — валидный исход). CI вызывает **ту же** команду, поэтому локальная и
облачная проверки не могут разъехаться.

Отдельные инструменты:

```bash
python tools/gen_spec_index.py                   # перегенерировать индекс спецификаций архива
python tools/runbook_validate.py --list          # какие этапы и проверки задекларированы
python tools/runbook_validate.py                     # полная валидация артефактов
python tools/runbook_validate.py --stage STAGE-00    # один этап (+ его входы)
python tools/runbook_validate.py --prereq            # только входы и зависимости
python tools/runbook_next.py                         # механический выбор следующей задачи
```

Валидатор проверяет артефакты, а не качество кода. `WAIT` означает, что нужна
подпись или решение человека, и этап не считается закрытым.

Селектор `runbook_next.py` реализует правила выбора из STAGE-13 механически.
Если `value_score`, `risk_score`, `cost_score` у задач не заполнены, он честно
сообщает, что приоритет требует человека, а не выдумывает оценку.

## 6.1. Скиллы этапов

Скилл не дублирует карточку этапа: он подключает её и добавляет границы
и команду валидатора. Канонические копии версионируются в `skills/`,
установщик кладёт их в рабочий каталог OpenCode (`~/.config/opencode/skills/`):

```bash
python tools/install_skills.py            # установить / обновить
python tools/install_skills.py --list     # что где лежит
python tools/install_skills.py --status   # сравнение по хэшам
python tools/install_skills.py --uninstall
```

Скилл срабатывает, когда человек называет этап или задачу. Он не даёт
права запускать следующий этап без команды и не заменяет решения человека.

## 7. Запрещённые действия

- Запускать два этапа подряд.
- Строить P1/P2 до прохождения соответствующего gate.
- Принимать blocking issue молча — только с явной записью в ADR или gate report.
- Менять публичные контракты без ADR.
- Выдумывать требования там, где спецификация молчит.
- Копировать или править архив спецификаций.
- Читать `old specs не трогать пока.7z`.
- Оценивать готовность по наличию функций.

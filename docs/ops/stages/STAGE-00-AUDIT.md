# STAGE-00 — Audit (только чтение)

> Бывший PROMPT 00. Не создаёт production-код. В конце — HARD STOP.

## Назначение

Построить карту архитектуры по архиву, найти противоречия и недостающие
контракты, определить, что обязательно для P0 и что запрещено до P0 gate.

## Trigger

Первый этап. Запускается после прочтения `AGENTS.md` и `docs/ops/RUNBOOK.md`.

## Inputs

- `career-intelligence-research-specs-v02/` — все 109 файлов, через двухпроходное чтение:
  1. **Инвентаризация** — по одному предложению на файл: что это, к какой подсистеме,
     релевантность P0 (высокая / средняя / низкая).
  2. **Целевое глубокое чтение** — только спеки, влияющие на P0 и на границы подсистем.
- `MASTER_DEPENDENCY_GRAPH.json` — базовый граф задач.
- `MASTER_FILE_INDEX.md`, `MASTER_ARCHIVE_AUDIT.md`.
- `old specs не трогать пока.7z` — **не читать**.

## Шаги

1. Составить инвентаризацию всех файлов архива.
2. Прочитать спеки P0-глубоко, остальные — по инвентаризации.
3. Определить bounded contexts и authoritative data sources.
4. Построить карту зависимостей между подсистемами.
5. Найти противоречия между спеками.
6. Найти отсутствующие контракты.
7. Найти архитектурные риски.
8. Определить P0-required и запреты до P0 gate.
9. Записать OPEN QUESTIONS — только вопросы, без выдуманных ответов.

## Outputs

- `docs/specs/SPEC_INDEX.md` — канон → путь → sha256 → статус (`canonical` / `conflict` / `deferred`). Свериться с `docs/specs/SPEC_INDEX_DATA.tsv`.
- `docs/architecture/MASTER_ARCHITECTURE_MAP.md`
- `docs/architecture/DEPENDENCY_MAP.md`
- `docs/architecture/P0_SCOPE.md`
- `docs/architecture/ARCHITECTURE_RISKS.md`
- `docs/architecture/GLOSSARY.md` — русский термин → английский канон.
- `docs/decisions/ADR-0001-project-architecture.md`
- `OPEN QUESTIONS` внутри каждого отчёта.

## Definition of Done

- [ ] Каждый из 109 файлов архива упомянут в `SPEC_INDEX` со статусом.
- [ ] Каждая строка в `SPEC_INDEX` содержит путь и sha256, сверенные с TSV.
- [ ] Каждый FACT в отчётах ссылается на файл и раздел спеки.
- [ ] Каждый CONFLICT описан как «спека A говорит X, спека B говорит Y, цена решения Z».
- [ ] Ни одного предложения по стеку, языку, фреймворку, хостингу.
- [ ] Есть список P0 REQUIRED и список «запрещено до P0 gate».
- [ ] Все неопределённости — в OPEN QUESTIONS, без догадок.

## Запрещено

- Любые решения по архитектуре, стеку и технологиям. `00_INDEX.md`: архитектура
  выбирается после пилота.
- Копировать или править файлы архива.
- Распаковывать `old specs не трогать пока.7z`.
- Создавать таски и бэклог — это STAGE-02.

## HARD STOP

Вывести:

```
FACTS
ASSUMPTIONS
CONFLICTS
RISKS
P0 REQUIRED
P1 DEFERRED
P2 DEFERRED
OPEN QUESTIONS
```

Заполнить `docs/ops/STAGE-STATUS.md`. Ждать команды человека.

## Rollback

Отчёты — обычные файлы. Для отмены удалить созданные файлы и вернуть статус
`PENDING` в `STAGE-STATUS.md`. Архив не затрагивается.

## Промпт для IDE

```text
Ты работаешь над проектом Career Intelligence / AI Profession Intelligence.

Твоя первая задача — НЕ писать код. Ты проводишь аудит архива спецификаций.

Прочитай AGENTS.md и docs/ops/RUNBOOK.md. Затем изучи архив в
career-intelligence-research-specs-v02/ в два прохода:
1) инвентаризация: по одному предложению на каждый из 109 файлов;
2) глубокое чтение только тех спеков, что влияют на P0 и на границы подсистем.

Файл "old specs не трогать пока.7z" не распаковывать и не читать.
Архив не копировать и не править.

Ключевой принцип проекта: CUSTOMER OUTCOME FIRST.
Основной цикл: USER/ORG → CONTEXT → GOAL → TASK/WORKFLOW → DIAGNOSIS →
AI / NON_AI / HUMAN OPTIONS → IMPLEMENTATION → VERIFICATION → MEASURED OUTCOME
→ FEEDBACK → UPDATED RECOMMENDATION.
Центральная сущность — WorkRecipe.

Твоя задача:
1. Построить карту архитектуры.
2. Определить bounded contexts.
3. Определить authoritative data sources.
4. Определить зависимости между подсистемами.
5. Найти противоречия между спеками.
6. Найти отсутствующие контракты.
7. Найти потенциальные архитектурные риски.
8. Определить, что обязательно для P0.
9. Определить, что нельзя реализовывать до прохождения P0 gate.

Ничего не реализуй. Не выбирай стек, язык, фреймворк, хостинг.

Создай:
docs/specs/SPEC_INDEX.md
docs/architecture/MASTER_ARCHITECTURE_MAP.md
docs/architecture/DEPENDENCY_MAP.md
docs/architecture/P0_SCOPE.md
docs/architecture/ARCHITECTURE_RISKS.md
docs/architecture/GLOSSARY.md
docs/decisions/ADR-0001-project-architecture.md

В конце выведи: FACTS, ASSUMPTIONS, CONFLICTS, RISKS, P0 REQUIRED,
P1 DEFERRED, P2 DEFERRED, OPEN QUESTIONS.

Не придумывай отсутствующие требования. Если спека недостаточно определена —
помечай это как OPEN QUESTION. Ни один вывод не считай фактом без ссылки
на файл и раздел спеки.
```

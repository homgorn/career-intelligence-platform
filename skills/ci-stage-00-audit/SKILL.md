---
name: ci-stage-00-audit
description: "Career Intelligence / AI Profession Intelligence, этап STAGE-00 — Audit. Применять только по явной команде человека. Двухпроходный аудит архива спецификаций: карта архитектуры, bounded contexts, зависимости, конфликты, P0_SCOPE, риски, SPEC_INDEX, GLOSSARY, ADR-0001. Код не пишется, стек не выбирается."
---

# STAGE-00 — Audit

Полный источник шагов — `docs/ops/stages/STAGE-00-AUDIT.md`. Прочитай его
и работай строго по нему.

## Перед стартом

- [ ] Прочитаны `AGENTS.md` и `docs/ops/RUNBOOK.md`.
- [ ] Это первый этап, предыдущих нет.

## Границы

- Только чтение и анализ. Production-код не пишется.
- Не выбирать стек, язык, фреймворк, хостинг: сначала пилот (`00_INDEX.md`).
- `old specs не трогать пока.7z` не распаковывать и не читать.
- Архив не копировать и не править.

## Чтение в два прохода

1. Инвентаризация: по одному предложению на каждый из 109 файлов.
2. Глубоко — только спеки, влияющие на P0 и границы подсистем.

## Выходы

- `docs/specs/SPEC_INDEX.md`
- `docs/architecture/MASTER_ARCHITECTURE_MAP.md`
- `docs/architecture/DEPENDENCY_MAP.md`
- `docs/architecture/P0_SCOPE.md`
- `docs/architecture/ARCHITECTURE_RISKS.md`
- `docs/architecture/GLOSSARY.md`
- `docs/decisions/ADR-0001-project-architecture.md`

## Контроль

```bash
python tools/runbook_validate.py --stage STAGE-00
```

## Финиш

Заполни `docs/ops/STAGE-STATUS.md`. Выведи FACTS / ASSUMPTIONS / CONFLICTS /
RISKS / P0 REQUIRED / P1 DEFERRED / P2 DEFERRED / OPEN QUESTIONS.
Остановись.

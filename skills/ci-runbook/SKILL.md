---
name: ci-runbook
description: "Проект Career Intelligence / AI Profession Intelligence — запуск любого этапа (STAGE-00…STAGE-19) или задачи (TASK-P0/P1/P2) по runbook. Применять, когда человек говорит «запусти этап», «выполняй TASK-…», «следующая задача», «проверь gate», «health check». Маршрутизирует на карточку этапа и правила AGENTS.md."
---

# Career Intelligence — runbook router

Единственный источник правил — `AGENTS.md`. Единственный источник порядка —
`docs/ops/RUNBOOK.md`. Источник шагов этапа — `docs/ops/stages/STAGE-XX-*.md`.

## Что делать

1. Определи этап или TASK-ID из сообщения человека.
2. Прочитай карточку этапа в `docs/ops/stages/`.
3. Работай строго по карточке. Не дублируй её содержимое в ответ.
4. В конце прогони валидатор этапа и заполни `docs/ops/STAGE-STATUS.md`.
5. Остановись. Жди команду человека.

## Если этап не назван

НЕ угадывай. Позови селектор:

```bash
python tools/runbook_next.py
```

Он скажет, какая задача следующая по правилам 1–8, или назовёт причину блокировки
(`BLOCKED_ON_PILOT`, закрытый gate, незакрытые зависимости).

## Общие запреты проекта

- Один этап за сеанс. Два этапа подряд не запускать.
- P1 только после release gate P0 = PASS. P2 только после P1 = PASS.
- Не выбирать стек и архитектуру до `PILOT_DECISION.md` со подписью.
- Не выдумывать требования: молчание спеки = OPEN QUESTION.
- Архив `career-intelligence-research-specs-v02/` — только на чтение.
- `old specs не трогать пока.7z` не читать.

## Карта этапов

| Слой | Этапы |
| --- | --- |
| До кода | 00, 00A, 01, 02 |
| Ядро P0 | 03, 04, 05, 05A, 06* |
| Поверхность P0 | 08, 08A, 09, 10, 11 |
| Gate P0 | 12 |
| Постоянный цикл | 13, 14, 15 |
| После P1 | 16, 17, 18 |
| Финал | 19 |

\* STAGE-06 только если `docs/gates/LLM_DECISION.md` = `LLM_REQUIRED` / `LLM_PARTIAL`.

## Полезные команды

```bash
python tools/runbook_validate.py              # вся валидация
python tools/runbook_validate.py --prereq     # что готово к запуску
python tools/runbook_validate.py --list       # задекларированные проверки
```

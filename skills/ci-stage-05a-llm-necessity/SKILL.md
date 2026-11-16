---
name: ci-stage-05a-llm-necessity
description: "Career Intelligence / AI Profession Intelligence, этап STAGE-05A — LLM necessity gate. Применять только после STAGE-05. Письменно обосновывает, нужен ли LLM в P0, по шагам value loop: LLM_REQUIRED / LLM_DEFERRED / LLM_PARTIAL. Если DEFERRED — STAGE-06 не запускается. Это валидный исход, а не ошибка."
---

# STAGE-05A — LLM necessity gate

Полный источник шагов — `docs/ops/stages/STAGE-05A-LLM-NECESSITY.md`.

## Суть

P0 может работать без LLM. `NON_AI` — полноценное решение, иерархия evidence
ставит model inference последним. Не строить LLM-слой «потому что AI-продукт».

## По каждому шагу value loop ответь

- Работает ли не-AI решение?
- Если нет: задача — extraction / mapping / synthesis / generation?
- Сколько вызовов на пользователя и сколько стоит один пользователь?
- Риск: provenance, prompt injection, cost?
- Можно ли отложить до P1 без потери доказательства ценности?

## Вердикты

- `LLM_REQUIRED` — нужен LLM, обоснован по шагам.
- `LLM_DEFERRED` — не нужен, STAGE-06 не запускается.
- `LLM_PARTIAL` — нужен для перечня конкретных шагов.

## Условия запуска STAGE-06

Только `LLM_REQUIRED` или `LLM_PARTIAL` + подтверждение человека + доступы
к провайдеру и бюджет.

## Выход

`docs/gates/LLM_DECISION.md`

## Контроль

```bash
python tools/runbook_validate.py --stage STAGE-05A
```

## Финиш

Жди подтверждения человека, особенно при `LLM_REQUIRED`. Остановись.

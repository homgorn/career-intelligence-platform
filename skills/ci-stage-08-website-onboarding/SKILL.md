---
name: ci-stage-08-website-onboarding
description: "Career Intelligence / AI Profession Intelligence, этап STAGE-08 — Website + onboarding. Применять только после STAGE-04 и STAGE-05. Один complete vertical slice: Goal → Current work → Painful task → Diagnosis → Recommendation → WorkRecipe → Action → Verification → Outcome. Три режима: сделаю сам / проведи меня / помоги сделать. Не делать «огромный тест → красивый AI report»."
---

# STAGE-08 — Website + onboarding

Полный источник шагов — `docs/ops/stages/STAGE-08-WEBSITE-ONBOARDING.md`.

## Перед стартом

- [ ] Завершены STAGE-04 и STAGE-05.
- [ ] STAGE-06 выполнен, если LLM обоснован.

## Главный UX

```
Goal → Current work → Painful task → Context → Diagnosis
→ Recommendation → WorkRecipe → Action → Verification → Outcome
```

Нужен путь к результату, а не «пройди тест → получи отчёт».

## Три режима

Сделаю сам / Проведи меня / Помоги сделать.

## На каждом экране

- зачем это пользователю;
- что он получит;
- что происходит с его данными;
- следующий action.

Responsive UX. Не добавлять dashboard complexity, не нужную P0.

## События

Только из замороженного каталога `docs/contracts/events/EVENT-CATALOG.md`.
`consent.granted` — до любой внешней интеграции.

## Контроль

```bash
python tools/runbook_validate.py --stage STAGE-08
```

## Финиш

Покажи пройденный путь и список событий. Остановись.

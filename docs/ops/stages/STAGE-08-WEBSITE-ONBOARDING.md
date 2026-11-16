# STAGE-08 — Website + onboarding

> Бывший PROMPT 08. Без изменений по существу, добавлена привязка к
> каноническому списку событий.

## Назначение

Реализовать customer-facing P0: один полный vertical slice от цели до
зафиксированного исхода.

## Trigger

Завершены STAGE-04 и STAGE-05 (и STAGE-06, если LLM обоснован).

## Inputs

- `14_B2C_VALUE_SPEC.md`
- `28_BEGINNER_ONBOARDING_AND_ADOPTION_SPEC.md`
- `48_BEGINNER_UX_AND_PRODUCT_JOURNEY_SPEC.md`
- `33_BEGINNER_AI_ONBOARDING_SPEC.md`
- `29_WORK_RECIPE_SPEC.md`
- `19_SEO_PROGRAMMATIC_SPEC.md` — только требования к страницам
- `44_LOCALIZATION_ACCESSIBILITY_SPEC.md`
- `docs/contracts/events/EVENT-CATALOG.md`

## Главный UX

```
Goal → Current work → Painful task → Context → Diagnosis
→ Recommendation → WorkRecipe → Action → Verification → Outcome
```

Не делай «пройди огромный тест → получи красивый AI report». Нужен путь к
результату.

## Три режима

1. Сделаю сам
2. Проведи меня
3. Помоги сделать

## На каждом экране

- зачем это пользователю;
- что он получит;
- что происходит с его данными;
- следующий action.

Responsive UX. Не добавляй unnecessary dashboard complexity.

## Outputs

- Working vertical slice
- Onboarding flow
- Event instrumentation по замороженному каталогу
- Tests

## Definition of Done

- [ ] Пользователь проходит Goal → Outcome без участия разработчика.
- [ ] Все три режима доступны и понятны.
- [ ] Каждое действие пользователя порождает событие из канонического каталога.
- [ ] Нет экрана без ответа на вопрос «что я получу».
- [ ] Accessibility-проверки пройдены (keyboard, contrast, screen reader labels).
- [ ] Нет dashboard complexity, не нужной P0.
- [ ] `consent.granted` пишется до любой внешней интеграции.

## HARD STOP

Показать пройденный путь и список событий. Ждать человека.

## Rollback

Feature flags на новые экраны, откат фронтенда, откат миграций при необходимости.
Данные пользователей не удаляются.

## Промпт для IDE

```text
Этап STAGE-08 — website + onboarding.

Основывайся на:
- career-intelligence-research-specs-v02/14_B2C_VALUE_SPEC.md
- career-intelligence-research-specs-v02/28_BEGINNER_ONBOARDING_AND_ADOPTION_SPEC.md
- career-intelligence-research-specs-v02/48_BEGINNER_UX_AND_PRODUCT_JOURNEY_SPEC.md
- career-intelligence-research-specs-v02/33_BEGINNER_AI_ONBOARDING_SPEC.md
- career-intelligence-research-specs-v02/29_WORK_RECIPE_SPEC.md
- career-intelligence-research-specs-v02/44_LOCALIZATION_ACCESSIBILITY_SPEC.md
- docs/contracts/events/EVENT-CATALOG.md

Главный UX: Goal → Current work → Painful task → Context → Diagnosis →
Recommendation → WorkRecipe → Action → Verification → Outcome.

Не делай продукт как "пройди огромный тест → получи красивый AI report".
Нужен путь к результату.

Три режима: сделаю сам / проведи меня / помоги сделать.

На каждом экране: зачем это пользователю, что он получит, что происходит
с его данными, следующий action.

Responsive UX. Не добавляй unnecessary dashboard complexity.
Сначала реализуй один complete vertical slice.

Все действия пользователя пишутся как события из замороженного каталога.
consent.granted — до любой внешней интеграции.

В конце заполни docs/ops/STAGE-STATUS.md и остановись.
```

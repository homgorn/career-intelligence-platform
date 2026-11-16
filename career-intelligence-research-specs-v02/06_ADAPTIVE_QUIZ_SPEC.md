# Adaptive Career Quiz Specification

## Principle
Не один длинный тест. Система задаёт минимальный набор вопросов и углубляется только там, где ответ materially changes ranking.

## Modules
Intent / Current State / Work Preferences / Constraints / Interests / Work Style / Skills / Experience / Education / Financial Target / Geography / Learning Willingness.

## Question types
single choice, multiple choice, pairwise choice, ranking, scale, scenario, forced trade-off, open text, confidence.

## Forced trade-offs
Пример:
A) +25% income, сменный график
B) обычный график, ниже income.
Это измеряет реальную utility.

## Branching
Hard constraints должны исключать невозможные paths; soft preferences только менять ranking.

## Stop condition
Останавливать, когда ranking стабилен и дополнительный вопрос мало меняет решение.

## Re-questioning
После изменения профиля спрашивать только affected dimensions.

## Accessibility
mobile-first, pause/resume, plain language, multilingual, voice option.

## Boundary
Это decision support, не психологический диагноз.

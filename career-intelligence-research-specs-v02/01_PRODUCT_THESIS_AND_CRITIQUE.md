# Product Thesis & Critique

## What to build
Персонализированный сервис карьерной навигации, отвечающий не только «какая профессия мне подходит?», а:
- что я уже умею;
- какие роли мне доступны;
- что подходит с учётом ограничений;
- что изменится при смене географии/режима;
- какие навыки дадут максимальный эффект;
- какие вакансии доступны сейчас.

## Critique
### Ошибка: personality quiz
Интересы ≠ навыки ≠ способности ≠ опыт ≠ доступность вакансий ≠ зарплата.

### Ошибка: top-5 careers
Нужны trade-offs и альтернативы.

### Ошибка: CV = полный профиль
CV selection-biased; нужны self-report + assessment + evidence.

### Ошибка: geography = filter
География меняет спрос, зарплату, лицензирование, язык, обучение, конкуренцию и remote viability.

### Ошибка: LLM сама решает
LLM должна интерпретировать evidence; eligibility/scoring должны быть структурированы.

## Differentiator
**Multi-signal career decision layer**:
profile → occupations → alternatives → gaps → paths → jobs → outcomes.

## Confidence
Высокая: простые quiz/AI resume/job-match рынки уже насыщены.
Средняя: multi-signal decision layer может дать лучшую UX-ценность.
Низкая: willingness-to-pay и лучший стартовый сегмент требуют экспериментов.

## Product shape
Universal core + profession modules + geo modules + market snapshots.

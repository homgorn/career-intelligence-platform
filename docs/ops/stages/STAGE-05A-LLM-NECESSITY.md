# STAGE-05A — LLM necessity gate

> Новый этап. В исходной цепочке LLM/RAG строился внутри P0 до того, как было
> доказано, что он нужен. Архив говорит прямо: `NON_AI` — полноценное решение,
> иерархия evidence ставит model inference последним, а `51_MISSING_LAYERS…`
> требует «do not use AI here» как first-class output.

## Назначение

Письменно обосновать, нужен ли LLM в P0, или отложить его до P1. Это экономит
деньги, снижает риск и остаётся верным принципу customer outcome first.

## Trigger

Завершён STAGE-05. Набор curated recipes и deterministic scoring работают.

## Inputs

- Decision records из STAGE-05.
- `PILOT_DECISION.md` — какой workflow выбран.
- `29_WORK_RECIPE_SPEC.md`, `01_SDD_ENGINE_SPEC.md`.
- `06_LLM_PLATFORM_SPEC.md`, `07_RAG_WIKI_INDEX_SPEC.md` — только для оценки.

## Шаги

1. Пройти по шагам value loop и найти шаги, где не-AI решение **не работает**.
   Кандидаты обычно: extraction из свободного текста (резюме, описание задачи),
   mapping на таксономию, synthesis длинного контекста, generation инструкций.
2. Для каждого кандидата ответить: задача, модель, число вызовов на пользователя,
   стоимость одного пользователя, latency, риск (provenance, injection, cost),
   можно ли отложить до P1 без потери доказательства ценности.
3. Вынести вердикт: `LLM_REQUIRED` / `LLM_DEFERRED` / `LLM_PARTIAL`.

## Outputs

- `docs/gates/LLM_DECISION.md`

## Definition of Done

- [ ] Вердикт принят по каждому шагу value loop, а не «в целом».
- [ ] У каждого шага с LLM есть оценка стоимости на пользователя.
- [ ] У каждого шага с LLM есть план fallback на случай недоступности провайдера.
- [ ] Если вердикт `LLM_DEFERRED` — STAGE-06 не запускается, и это записано.
- [ ] Если вердикт `LLM_PARTIAL` — перечислены только эти шаги, остальное
      работает без LLM.

## Если LLM не нужен

Это валидный и желаемый исход. Записать в `LLM_DECISION.md` обоснование и
перейти к STAGE-08. LLM добавляется в P1 уже на доказанной ценности.

## HARD STOP

Ждать подтверждения человека, особенно при `LLM_REQUIRED`: нужны доступы
к провайдеру и бюджет.

## Rollback

Вердикт пересматривается новой версией `LLM_DECISION.md`. Уже построенный
LLM-слой не выбрасывается, а помечается `deferred_by_decision`.

## Промпт для IDE

```text
Этап STAGE-05A — гейт необходимости LLM.

Оцени, нужен ли LLM в P0 конкретно для выбранного пилота.

Прочитай:
- docs/ops/stages/STAGE-05-RECOMMENDATION-ENGINE.md
- docs/architecture/PILOT_DECISION.md
- career-intelligence-research-specs-v02/29_WORK_RECIPE_SPEC.md
- career-intelligence-research-specs-v02/01_SDD_ENGINE_SPEC.md
- career-intelligence-research-specs-v02/06_LLM_PLATFORM_SPEC.md
- career-intelligence-research-specs-v02/07_RAG_WIKI_INDEX_SPEC.md

По каждому шагу value loop ответь:
- работает ли не-AI решение?
- если нет: какая задача (extraction / mapping / synthesis / generation)?
- сколько вызовов на пользователя и сколько стоит один пользователь?
- какой риск: provenance, prompt injection, cost?
- можно ли отложить до P1 без потери доказательства ценности?

Вердикт по проекту: LLM_REQUIRED / LLM_DEFERRED / LLM_PARTIAL.

Создай docs/gates/LLM_DECISION.md.
Если LLM_DEFERRED — STAGE-06 не запускается.
Остановись и жди подтверждения человека.
```

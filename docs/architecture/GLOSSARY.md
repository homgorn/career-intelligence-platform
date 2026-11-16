# GLOSSARY — русский термин → английский канон

Идентификаторы, имена событий, поля API и БД, значения enum — только так,
как в этой таблице. Нарративные документы могут быть на русском, но при первом
упоминании термина в скобках указывается английский канон.

## Сущности

| Русский | Английский канон |
| --- | --- |
| человек | `Person` |
| арендатор, тенант | `Tenant` |
| организация | `Organization` |
| команда | `Team` |
| участник | `Member` |
| профиль карьеры | `CareerProfile` |
| AI-профиль | `AIProfile` |
| цель | `Goal` |
| профессия | `Occupation` |
| специализация | `Specialization` |
| навык | `Skill` |
| задача | `Task` |
| рабочий процесс | `Workflow` |
| шаг процесса | `WorkflowStep` |
| рецепт работы | `WorkRecipe` |
| инструмент | `Tool` |
| плагин | `Plugin` |
| коннектор | `Connector` |
| агент | `Agent` |
| рекомендация | `Recommendation` |
| доказательство | `Evidence` |
| источник | `Source` |
| исход, результат | `Outcome` |
| внедрение | `Implementation` |
| верификация | `Verification` |
| диагностика | `Diagnosis` |
| диагноз | `Diagnosis` |
| контекст | `Context` |
| политика | `Policy` |
| решение по политике | `PolicyDecision` |
| согласие | `Consent` |
| событие аудита | `AuditEvent` |
| подписка | `Subscription` |
| счёт | `Invoice` |
| эксперимент | `Experiment` |
| партнёр | `Partner` |
| вакансия | `Job` |
| рыночный сигнал | `MarketSignal` |
| учебный актив | `LearningAsset` |
| пакет внедрения | `ImplementationPackage` |

## Процесс и измерения

| Русский | Английский канон |
| --- | --- |
| кандидат-вмешательство | `Candidate intervention` |
| тип решения | `Solution type` |
| без AI | `NON_AI` |
| человек | `HUMAN` |
| AI-дополнение | `AI_AUGMENT` |
| AI-автоматизация | `AI_AUTOMATION` |
| агент | `AGENT` |
| гибрид | `HYBRID` |
| оценка | `Score` |
| ранжирование | `Ranking` |
| уверенность evidence | `evidence_confidence` |
| осуществимость | `feasibility` |
| трение | `friction` |
| происхождение данных | `Provenance` |
| уровень evidence | `evidence_level` |
| воронка | `Funnel` |
| активация | `Activation` |
| удержание | `Retention` |
| стоимость привлечения | `CAC` |
| пожизненная ценность | `LTV` |
| цена подтверждённого исхода | `Cost per verified outcome` |
| время до первой ценности | `Time-to-first-value` |
| эталонный набор | `Golden dataset` |
| эталонный тест | `Benchmark` |
| граница контекста | `Bounded context` |
| проекция | `Projection` |
| построенная связь | `Inferred edge` |
| утверждённая связь | `Asserted edge` |
| жизненный цикл инструмента | `Tool lifecycle` |
| адаптер | `Adapter` |
| гейт | `Gate` |

## События

Пишутся только в канонической форме из `03_EVENT_CONTRACTS_SPEC.md`:
`profile.created`, `profile.updated`, `resume.ingested`, `occupation.matched`,
`task.identified`, `workflow.created`, `recommendation.generated`,
`recommendation.accepted`, `implementation.started`, `implementation.completed`,
`outcome.recorded`, `tool.verified`, `policy.blocked`, `consent.granted`,
`consent.revoked`, `subscription.changed`, `partner.attributed`.

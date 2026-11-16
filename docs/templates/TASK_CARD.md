# TASK-XXXX — <название>

Шаблон задачи. Основан на `career-intelligence-research-specs-v02/IDE_TASK_TEMPLATE.json`
и `45_IDE_EXECUTION_BACKLOG_SCHEMA.md`. ID берётся из `MASTER_DEPENDENCY_GRAPH.json`
архива и никогда не перезапускает нумерацию.

## Поля

```yaml
task_id: TASK-XXXX
title: ""
objective: ""
customer_value: ""          # измеримое; если нельзя измерить — задача невалидна
priority: P0 | P1 | P2
status: PENDING | IN_PROGRESS | BLOCKED_ON_PILOT | BLOCKED_ON_QUESTION | DONE
context: ""                 # где именно в value loop применяется
dependencies: []            # только TASK-ID из MASTER_BACKLOG.json
spec_refs:                  # файл + раздел спеки, никакой памяти
  - file: "career-intelligence-research-specs-v02/XX_SPEC.md"
    section: "## Pipeline"
affected_domains: []        # bounded contexts, которых касается задача
inputs: []
outputs: []
required_skills: []
recommended_plugins: []
implementation_notes: ""
acceptance_criteria: []     # измеримые, проверяемые машиной или человеком
security: []
legal_trigger: ""           # что должно вызвать legal review, или "нет"
analytics: []               # какие события и метрики задача добавляет
tests: []
rollback: ""
definition_of_done: []
evidence: ""                # ссылка на результат прогона, скриншот, лог
```

## Правила заполнения

- `customer_value` без измеримого критерия запрещён.
- `spec_refs` обязателен: решение, не опирающееся на спеку, оформляется через ADR.
- `dependencies` только по ID из бэклога. Не ссылки на «предыдущие работы».
- `rollback` — что именно откатывается и как проверяется.
- `legal_trigger` — пусто означает «legal review не требуется», а не «не подумали».
- `analytics` — события только из замороженного каталога.

## Definition of Done (глобальный)

Code/config implemented; tests pass; security/privacy checks pass;
telemetry added; docs updated; migration/recovery verified;
acceptance criteria demonstrated.

## AI-specific DoD

Model/provider/version recorded; evals pass; provenance/citations validated;
tool permissions constrained; failure behavior tested.

## Production DoD

Monitoring; alert; backup/recovery impact; migration plan;
deployment/rollback tested.

# gates — отчёты гейтов

Три уровня:

| Уровень | Когда | Кто решает | Файл |
| --- | --- | --- | --- |
| Stage gate | после каждого этапа | IDE проверяет, человек подтверждает | `STAGE-GATE-XX.md` |
| Release gate | граница P0/P1/P2 | человек | `RELEASE-GATE-P0.md` |
| Production gate | перед выпуском | человек + внешний аудит при необходимости | `PRODUCTION-GATE.md` |

Шаблон: `../templates/GATE-REPORT.md`.

## Производные gate-отчёты

| Файл | Этап |
| --- | --- |
| `SECURITY_GATE.md` | STAGE-09 |
| `PRIVACY_GATE.md` | STAGE-09 |
| `LEGAL_GATE.md` | STAGE-09 |
| `LLM_DECISION.md` | STAGE-05A |

## Правила

- Blocking finding не закрывается молча.
- Gate не проходит по факту готовности бэклога.
- Release gate требует доказательства повторяемой ценности и приемлемой экономики.
- Юридический вывод не принимается внутри IDE — создаётся legal review trigger.

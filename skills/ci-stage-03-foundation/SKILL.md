---
name: ci-stage-03-foundation
description: "Career Intelligence / AI Profession Intelligence, этап STAGE-03 — Foundation. Применять только после заморозки контрактов STAGE-02. Первый этап с кодом: project structure, database, migrations, domain boundaries, API foundation, auth, tenant isolation, RBAC, logging, tracing, secrets, tests, CI, observability. Ничего лишнего. В конце HARD STOP."
---

# STAGE-03 — Foundation

Полный источник шагов — `docs/ops/stages/STAGE-03-FOUNDATION.md`.

## Перед стартом

- [ ] Контракты из STAGE-02 утверждены (`ADR-0003`, `ADR-0004`).
- [ ] Прочитаны `ADR-0002-stack-and-pilot.md` и `PILOT_DECISION.md`.

## Включай только необходимое

project structure; environment configuration; database; migrations;
domain module boundaries; API foundation; authentication; tenant isolation;
RBAC foundation; error handling; logging; tracing; configuration;
secrets handling; test infrastructure; CI; local development;
basic observability.

## Не реализуй

marketplace, сложный agent runtime, knowledge graph, массовый SEO,
B2B enterprise, сложный billing, десятки интеграций. Это P1/P2.

## Порядок

Спеки → implementation plan → dependency order → код → проверки.

## Обязательные проверки после кода

- Тесты проходят, команда запуска записана.
- Migrations применяются с нуля и откатываются.
- Tenant isolation проверен тестом на cross-tenant leakage.
- Auth работает, MFA заложена для привилегированных ролей.
- Secrets не в репозитории, логах и контексте модели.
- Observability: логи, трейс, метрики, алерты.
- Rollback деплоя проверен.

## Выходы

Implementation report, test report, security checklist, remaining issues.

## Контроль

```bash
python tools/runbook_validate.py --stage STAGE-03
```

## Финиш

HARD STOP. Не переходи к STAGE-04 в том же сеансе.

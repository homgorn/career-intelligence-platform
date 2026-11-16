# STAGE-03 — Foundation

> Бывший PROMPT 03. Первый этап, где пишется код. Только фундамент, ничего лишнего.

## Назначение

Создать минимальный production-ready фундамент, на котором можно реализовать
полный customer-value loop для одного workflow.

## Trigger

Подписаны контракты STAGE-02 (`ADR-0003`, `ADR-0004`) и бэклог.

## Inputs

- `docs/contracts/api/API-FOUNDATION.md`
- `docs/contracts/domain/DATA-MODEL-P0.md` (если уже есть P0-схема)
- `PILOT_DECISION.md`, `ADR-0002-stack-and-pilot.md`
- `11_SECURITY_ARCHITECTURE_SPEC.md`, `38_TENANCY_IDENTITY_RBAC_SPEC.md`,
  `42_OBSERVABILITY_SPEC.md`, `41_TESTING_QA_SPEC.md`, `40_DEVOPS_SRE_SPEC.md`

## Включай только необходимое

- project structure;
- environment configuration;
- database;
- migrations;
- domain module boundaries;
- API foundation;
- authentication;
- tenant isolation;
- RBAC foundation;
- error handling;
- logging;
- tracing;
- configuration;
- secrets handling;
- test infrastructure;
- CI;
- local development;
- basic observability.

## Не реализуй

marketplace, сложный agent runtime, knowledge graph, массовый SEO, B2B enterprise,
сложный billing, десятки интеграций. Это P1/P2.

## Порядок

1. Прочитай соответствующие спеки и контракты.
2. Составь implementation plan.
3. Покажи dependency order.
4. Реализуй.
5. Прогони тесты, migrations, проверки.

## Outputs

- Implementation report
- Test report
- Security checklist
- Remaining issues

## Definition of Done

- [ ] Тесты проходят; команда запуска зафиксирована в README.
- [ ] Migrations применяются с нуля и откатываются.
- [ ] Tenant isolation проверен автоматическим тестом (cross-tenant leakage).
- [ ] Auth работает; MFA для привилегированных ролей заложена.
- [ ] Secrets не попадают в репозиторий, логи и контекст модели.
- [ ] Observability: логи, трейс, метрики, алерты — минимальный набор.
- [ ] Rollback деплоя проверен.
- [ ] Нет секретов в коде и конфигах; `.env` в `.gitignore`.
- [ ] Open questions зафиксированы.

## HARD STOP

Не переходи к следующему этапу автоматически. Заполни `STAGE-STATUS.md`,
покажи отчёты, жди человека.

## Rollback

Откат migration назад, удаление созданных модулей, возврат статуса `PENDING`.
Любая секретная утечка — немедленная ротация секретов, а не просто правка кода.

## Промпт для IDE

```text
Этап STAGE-03 — foundation.

Начинаем код P0, но только фундамент.

Прочитай:
- docs/contracts/api/API-FOUNDATION.md
- docs/architecture/PILOT_DECISION.md
- docs/decisions/ADR-0002-stack-and-pilot.md
- career-intelligence-research-specs-v02/11_SECURITY_ARCHITECTURE_SPEC.md
- career-intelligence-research-specs-v02/38_TENANCY_IDENTITY_RBAC_SPEC.md
- career-intelligence-research-specs-v02/42_OBSERVABILITY_SPEC.md
- career-intelligence-research-specs-v02/41_TESTING_QA_SPEC.md
- career-intelligence-research-specs-v02/40_DEVOPS_SRE_SPEC.md

Цель: минимальный production-ready фундамент под customer-value loop.

Включи только необходимое:
project structure, environment configuration, database, migrations,
domain module boundaries, API foundation, authentication, tenant isolation,
RBAC foundation, error handling, logging, tracing, configuration,
secrets handling, test infrastructure, CI, local development, basic observability.

Не реализуй: marketplace, сложный agent runtime, knowledge graph, массовый SEO,
B2B enterprise, сложный billing, десятки integrations.

Перед кодом: прочитай спеки, составь implementation plan, покажи dependency order.

После реализации проверь: tests, migrations, tenant isolation, auth, secrets,
observability.

Создай: implementation report, test report, security checklist, remaining issues.

Не переходи к следующему этапу автоматически.
```

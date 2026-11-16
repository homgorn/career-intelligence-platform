# AI Profession Intelligence — Product Specification

Version 0.2

## Purpose
Преобразовать описание профессии в практическую карту того, как генеративный AI, классический ML, RPA, агенты и цифровые инструменты меняют конкретную работу человека. Не выдавать общий прогноз «AI заменит профессию на X%».

## Core output
Для выбранной профессии, специализации, уровня и контекста пользователь получает:
1. карту задач и рабочих процессов;
2. оценку применимости AI по каждой задаче;
3. варианты: использовать AI как помощника, автоматизировать часть процесса, передать ограниченный шаг агенту, не применять AI;
4. конкретные инструменты и требования;
5. план освоения и внедрения;
6. ожидаемые выгоды, стоимость, риски и способы проверки;
7. альтернативные специализации и новые источники дохода, возникающие благодаря AI.

## Primary entity chain
`Person → Profession → Role variant → Work context → Workflow → Task → AI capability → Tool/Agent → Implementation → Human control → Outcome → Evidence`.

## Segmentation dimensions
- profession / specialization / seniority;
- employee / freelancer / owner / manager / apprentice;
- company size and digital maturity;
- country, language, regulation and tool availability;
- task frequency, volume, complexity, variability and consequence of error;
- available devices, connectivity, budget and existing software;
- user confidence and AI literacy.

## Task-level classification
Each task must be classified independently:
- AI can assist: draft, explain, search, summarize, classify, calculate with verification, compare;
- AI can partially automate: predictable substeps with deterministic checks;
- agent candidate: bounded multi-step work with scoped tools, approvals and rollback;
- human-led: physical execution, accountable judgment, relationship work, high-consequence decisions;
- not suitable now: weak data, unreliable model capability, excessive risk or negative economics.

## Required recommendation record
`task_id, user_context, applicability, capability_type, recommended_pattern, tools, prerequisites, setup_effort, recurring_effort, cost_range, risk_level, verification_method, expected_benefit_range, confidence, evidence_date, source_refs`.

## UX principles
- Start from the user's work, not from AI terminology.
- Show one useful next action, not a catalogue of 50 tools.
- Separate "possible in principle" from "available to this user, in this country and plan".
- Offer manual, assisted and automated paths.
- Never imply that a suggested workflow is already installed or connected.
- Show what the human remains responsible for.

## Non-goals
- Predicting exact job displacement percentages.
- Replacing professional licensing, safety procedures or legal advice.
- Recommending AI for every task.
- Treating a vendor's marketing claim as proof of measured productivity.

## Acceptance criteria
A recommendation is useful only if a user can identify the task, understand the value, see prerequisites and risks, choose a tool, follow setup steps, test the result and measure whether it helped.

# Job Matching Specification

Career matching = «какую профессию выбрать?»
Job matching = «какую конкретную вакансию подавать?»

## Inputs
normalized profile, occupation, specialization, seniority, skills, location, language, salary, schedule, work authorization.

## Job result
fit level, reasons, matched skills, missing skills, blockers, salary source, remote/commute, employer, freshness, application route.

## Job quality
duplicate/stale detection, suspicious listing detection, title mismatch, unrealistic requirements, missing salary.

## Explainable match
Prefer:
«8/10 required skills; location fits; salary meets minimum; one mandatory certificate missing»
instead of uncalibrated «93%».

## Closed loop
viewed → rejected → interview → offer → hired.
Outcomes feed ranking evaluation.

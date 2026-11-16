# AI Leverage & Impact Specification

## Principle
Do not claim a profession is "X% automatable". Estimate the potential leverage of a specific workflow under stated assumptions.

## Impact dimensions
- time saved per execution;
- throughput / capacity;
- quality and error rate;
- response time;
- revenue opportunity;
- cost avoided;
- user experience;
- safety and compliance;
- job quality and cognitive load;
- new service or specialization potential.

## Economics
Calculate:
`Net benefit = verified value created − tool cost − implementation cost − operation cost − review/rework cost − risk-adjusted expected loss`.

For time:
`Net time saved = baseline time − AI-assisted time − verification time − exception handling time`.

Use ranges and scenarios: conservative / expected / optimistic. Include sample size and confidence interval where possible.

## AI leverage score
A decision aid, not a universal truth:
`Leverage = expected benefit × feasibility × repeatability × adoption likelihood / (implementation effort + risk burden)`.
Expose component values; never show only the composite score.

## Measurement
Capture baseline before pilot. Compare like-for-like tasks and account for learning curve, seasonality, task mix and user selection bias.

## Guardrails
- Do not count generated output as value until accepted and used.
- Do not count time "saved" if review and rework are excluded.
- Do not monetize safety or compliance shortcuts.
- Do not infer job loss from task-level automation.
- Report distribution: some users/tasks may benefit while others do not.

## Acceptance criteria
Every impact claim has a baseline, method, period, sample size, assumptions and confidence label.

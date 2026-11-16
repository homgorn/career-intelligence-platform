# AI Outcome & Feedback Specification

## Purpose
Close the loop from recommendation to real-world result.

## Lifecycle
Opportunity identified → user chooses → setup completed → first use → repeat use → measured outcome → review → improve / retain / retire.

## Events
recommendation_shown, recommendation_saved, tool_selected, connection_started, connection_completed, tutorial_started, tutorial_completed, workflow_published, workflow_run, human_override, error, rework, outcome_submitted, subscription_cancelled.

## Outcome fields
Task, baseline, assisted result, human review time, total cycle time, quality, error/rework, actual cost, user confidence, frequency, sample size, date and evidence.

## Feedback methods
- one-tap useful / not useful;
- structured reason;
- before/after task sample;
- optional time diary;
- workflow telemetry with consent;
- practitioner interview;
- periodic review.

## Attribution
Do not claim causality from a single positive rating. Distinguish user perception, observed telemetry and independently verified business result.

## Privacy
Collect the minimum. Provide opt-out, export and deletion processes. Do not use customer data to train general recommendations without a lawful basis and explicit appropriate consent.

## Acceptance criteria
A recommendation can be labeled "validated in practice" only after a defined sample, time period and outcome method. Otherwise label it "untested" or "pilot evidence".

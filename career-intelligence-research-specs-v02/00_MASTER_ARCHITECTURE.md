# Master architecture and operating model

This document is the top-level contract for the product. The product goal is measurable improvement in a person's career/work outcomes, not AI usage itself. AI is one means; a non-AI recommendation is valid when it creates more value, lower risk, or lower implementation cost.

## Core value loop

`USER/ORG → CONTEXT → GOAL → TASK/WORKFLOW → DIAGNOSIS → OPTIONS (AI / NON-AI / HUMAN) → IMPLEMENTATION → VERIFICATION → MEASURED OUTCOME → FEEDBACK → UPDATED RECOMMENDATION`.

Every recommendation must be traceable to a user goal and an observable outcome.

## Bounded contexts

Career Intelligence; Work Intelligence; AI Transformation; Tool & Plugin Intelligence; Learning; Implementation; Outcome Intelligence; Trust & Governance; Marketplace; Growth; Billing; Support; Knowledge/Research.

Bounded contexts communicate through explicit contracts. Avoid one giant mutable "user profile" object.

## North-star principle

Optimize for time-to-value, outcome quality, user confidence, and sustainable adoption. Do not optimize for number of AI recommendations, prompts, tools, or generated text.

## P0 architecture rule

A first release must be able to deliver one complete value loop for one concrete workflow. Everything else may exist as contracts, adapters, or stubs, but must not block validation.

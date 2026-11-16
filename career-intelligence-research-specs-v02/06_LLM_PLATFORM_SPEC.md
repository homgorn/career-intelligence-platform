# LLM platform and model routing

LLMs are probabilistic components inside a controlled platform. The system must support model routing, structured outputs, retrieval, tool use, guardrails, evaluation and fallback.

## Model roles

Classifier; extractor; summarizer; recommender; planner; conversational agent; evaluator; content generator. Prefer small/cheap models for deterministic extraction/classification when quality is sufficient.

## Routing

Route by task complexity, sensitivity, latency, cost, language, context size, and required capabilities. Record model/provider/version for every consequential run.

## Structured output

Use JSON schemas or typed function contracts. Reject invalid output rather than silently coercing ambiguous data.

## Human review

Risky or irreversible actions require approval. LLM confidence is not a substitute for policy or human review.

## Evaluation

Maintain golden datasets for extraction, occupation mapping, task mapping, recommendations, explanations, safety and outcome prediction. Track regression by model/version.

<div align="center">

# Career Intelligence / AI Profession Intelligence

**Spec-driven execution platform where every claim carries provenance,
every decision has a version, and no stage advances without passing a gate.**

[English](README.md) · [Русский](README.ru.md)

[![CI](https://github.com/homgorn/career-intelligence-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/homgorn/career-intelligence-platform/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](pyproject.toml)
[![Spec integrity](https://img.shields.io/badge/spec%20archive-109%20files%20hashed-blue.svg)](docs/specs/SPEC_INDEX.md)

</div>

---

## The problem this repository solves

Most AI career products optimize for AI usage: more prompts, more
recommendations, longer reports, more time in the app. This project optimizes
for a **measurable customer outcome** — a person performs a real task, adopts an
intervention, verifies it, and the result is recorded.

That single principle reshapes everything else:

| Principle | Consequence in this repo |
| --- | --- |
| Customer outcome > AI feature | A non-AI recommendation is a valid, first-class outcome |
| Evidence > assumption | Every recommendation stores its evidence chain |
| Deterministic policy > LLM judgment | LLM proposes; typed services decide |
| Authoritative DB > derived index > LLM memory | Search, vector and graph indexes are rebuildable projections |
| Provenance is mandatory | Claims carry source, date, geography, confidence, version |
| Irreversible actions require approval | No agent executes high-impact steps unattended |

The core value loop, identical in every layer of the architecture:

```
USER/ORG → CONTEXT → GOAL → TASK/WORKFLOW → DIAGNOSIS
→ OPTIONS (AI / NON_AI / HUMAN) → IMPLEMENTATION → VERIFICATION
→ MEASURED OUTCOME → FEEDBACK → UPDATED RECOMMENDATION
```

The central unit of value is the **WorkRecipe** — a reusable, evidence-backed
recipe that connects a person's real task to a practical intervention and a
measured result.

## What is in this repository

This is the **specification and execution system**, not yet the application.
The application is deliberately deferred until a pilot is chosen and the
contracts are frozen.

| Component | Count | Purpose |
| --- | --- | --- |
| Master specification archive | 109 files | Read-only source of truth. Domain contracts, evidence hierarchy, policy, gates, security, legal, data, roadmap |
| Stage cards | 23 | `STAGE-00`…`STAGE-19`: trigger, inputs, steps, outputs, Definition of Done, hard stop, rollback |
| Machine-readable assertions | 24 | Declarative, per-stage checks that a validator executes |
| Agent skills | 24 | One skill per stage so an IDE loads the right card automatically |
| Python tooling | 4 tools | Validator, task selector, spec-index generator, skill installer |
| Tests | 47 | Behaviour-level tests at the CLI and check seams |
| Architecture documents | 5 | Architecture map, dependency map, P0 scope, risk register, glossary |
| ADRs | 1 | `ADR-0001` — the operating model and its nine decisions |

### Repository layout

```
career-intelligence-platform/
├── AGENTS.md                              # rules an IDE agent loads automatically
├── README.md / README.ru.md               # this file / Russian version
├── career-intelligence-research-specs-v02 # 109 spec files, read-only
├── docs/
│   ├── ops/
│   │   ├── RUNBOOK.md                     # stage registry, order, prohibitions
│   │   ├── STAGE-INDEX.csv                # machine-readable stage registry
│   │   ├── STAGE-STATUS.md                # execution journal
│   │   ├── ASSERTIONS.md                  # assertion format reference
│   │   ├── stages/                        # 23 stage cards
│   │   └── assertions/                    # 24 assertion declarations
│   ├── architecture/                      # maps, P0 scope, risks, glossary
│   ├── contracts/                         # events, data model, API (STAGE-02)
│   ├── decisions/                         # ADRs
│   ├── gates/                             # gate reports
│   ├── specs/                             # spec index + sha256 of every archive file
│   ├── tasks/                             # single live backlog + task cards
│   ├── templates/                         # task, ADR, gate report, pilot decision
│   ├── research/  wiki/
├── skills/                                # 24 stage skills
└── tools/
    ├── runbook_validate.py                # artifact + contract validator
    ├── runbook_next.py                    # mechanical task selector
    ├── gen_spec_index.py                  # regenerates the spec index
    ├── install_skills.py                  # installs skills into the agent runtime
    └── tests/                             # 47 tests
```

## Quick start

```bash
git clone https://github.com/homgorn/career-intelligence-platform.git
cd career-intelligence-platform

python tools/runbook_validate.py            # validate every declared artifact
python tools/runbook_validate.py --stage STAGE-00
python tools/runbook_next.py                # which task is next, and why
python tools/gen_spec_index.py              # regenerate the spec index
```

Local checks used by CI:

```bash
pip install ruff pytest
ruff check tools
ruff format --check tools
pytest tools/tests
```

## How execution works

Work moves through stages. Each stage has a trigger, declared inputs, declared
outputs, a Definition of Done, a hard stop and a rollback path.

```
STAGE-00 audit → STAGE-00A pilot → STAGE-01 readiness → STAGE-02 contracts
  → STAGE-03 foundation → STAGE-04 domain/data → STAGE-05 recommendation
  → STAGE-05A LLM gate → [STAGE-06 LLM/RAG, conditional]
  → STAGE-08 website → STAGE-08A distribution → STAGE-09 security/legal
  → STAGE-10 analytics → STAGE-11 vertical slice → STAGE-12 P0 gate
  → STAGE-13/14 (task cycle) → STAGE-15 health check → STAGE-16..19
```

Three rules make the process trustworthy:

1. **One stage per session.** A stage ends with a hard stop and waits for a human.
2. **Human decisions stay human.** Pilot choice, LLM necessity and release gates
   are never automated. The tooling reports `WAIT` instead of silently passing.
3. **Definition of Done is partly executable.** Assertions describe what each
   stage must produce; the validator executes them and fails the build.

The LLM layer is conditional by design: `STAGE-05A` requires an explicit,
written justification before any LLM or RAG work starts, because `NON_AI` is a
legitimate outcome and model inference sits at the bottom of the evidence
hierarchy.

## P0 scope and the value gate

P0 proves **one complete value loop for one concrete workflow**. Everything
else is explicitly deferred — see `docs/architecture/P0_SCOPE.md`.

P0 covers: multi-tenant foundation, auth and isolation, the pilot profession's
taxonomy slice, `WorkRecipe`, the deterministic recommendation engine with
policy gates, one complete vertical slice with three adoption modes
(*do it myself / guide me / do it for me*), outcome recording, analytics over a
frozen event catalog, and a minimal distribution channel.

P0 explicitly excludes: adaptive quiz, resume ingestion, job matching, career
path engine, tool registry and MCP, learning paths, B2B, partner programs, SEO
scale, complex billing, knowledge graph, agent runtime, marketplace.

The P0 gate compares measured results against thresholds the owner sets **before**
the work starts, in `docs/architecture/PILOT_DECISION.md`:

| Metric | Reference threshold |
| --- | --- |
| Real users completing the loop | ≥ 20, not staff or friends |
| Time to first value | ≤ 15 minutes (median) |
| Completed at least one WorkRecipe action | ≥ 30% |
| Returned to record an outcome within 14 days | ≥ 10% |
| Unresolved security / privacy blockers | 0 |
| Recommendations with provenance and policy version | 100% |
| Cost per verified outcome | within the target set at pilot decision |

`PASS` requires every threshold. `CONDITIONAL_PASS` allows one. `FAIL` if the
outcome is unproven or a legal or security blocker is open. A failed gate does
not unlock P1.

## Current status

| Stage | Status |
| --- | --- |
| `STAGE-00` audit | Complete — 109 files inventoried, 8 archive conflicts recorded |
| `STAGE-00A` pilot decision | Waiting on the owner: ICP, profession, workflow, country, thresholds |
| `STAGE-01`…`STAGE-19` | Not started |

The next stage requires a human decision and cannot be automated. The selector
reports this explicitly:

```
=== Селектор следующей задачи ===
Пилот подписан: НЕТ (нет docs/architecture/PILOT_DECISION.md)
Gate: P0=None P1=None P2=None
Разрешённые приоритеты: P0

[BLOCKED] BLOCKED_ON_PILOT: нет docs/architecture/PILOT_DECISION.md
```

## Documentation map

Project documentation is written in Russian, matching the working language of
the team. Code identifiers, event names and API fields stay in English exactly
as they appear in the archive (`WorkRecipe`, `NON_AI`, `recommendation.generated`).
`docs/architecture/GLOSSARY.md` maps one to the other.

| Path | Contents |
| --- | --- |
| `docs/specs/SPEC_INDEX.md` | Spec index, statuses, the eight archive conflicts |
| `docs/architecture/` | Architecture map, dependency map, P0 scope, risks, glossary |
| `docs/ops/RUNBOOK.md` | Stage registry, execution order, prohibitions |
| `docs/ops/stages/` | Stage cards with ready-to-paste prompts |
| `docs/ops/ASSERTIONS.md` | Assertion schema and the list of check kinds |
| `docs/decisions/` | Architecture Decision Records |
| `docs/gates/` | Security, privacy, legal, release and production gate reports |
| `docs/tasks/` | Single live backlog and task cards |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Short version: one stage per pull
request, no public contract changes without an ADR, and `ruff check` +
`pytest` + the stage validator must pass.

## Legacy archive

`old specs не трогать пока.7z` is a frozen legacy archive. It is committed
verbatim, must not be extracted, edited or deleted until it is explicitly
released, and it is not part of the P0 specification surface.

## License

MIT — see [LICENSE](LICENSE). A proposed monetization strategy
(open core + premium API) is under owner review in
[docs/architecture/MONETIZATION_STRATEGY.md](docs/architecture/MONETIZATION_STRATEGY.md).

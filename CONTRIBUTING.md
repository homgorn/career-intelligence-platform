# Contributing

This repository follows the operating model in `AGENTS.md` and
`docs/ops/RUNBOOK.md`. Both are binding: an agent or a human may only work
inside the scope of a declared stage.

> Документация проекта ведётся на русском. Этот файл и код — на английском.
> Русская версия README: [README.ru.md](README.ru.md).

## Rules that do not bend

1. **One stage per pull request.** A PR that mixes stages cannot be reviewed
   against a Definition of Done.
2. **No public contract changes without an ADR.** Contracts live in
   `docs/contracts/`. If a change is required, open an ADR first.
3. **The archive is read-only.** `career-intelligence-research-specs-v02/` is
   the source of truth. Never edit, rename, copy or extract it. The legacy
   `.7z` is frozen.
4. **Evidence over assumption.** If a specification is silent, record an OPEN
   QUESTION — do not invent a requirement.
5. **Human decisions stay human.** Pilot choice, LLM necessity and release
   gates are never automated.

## Before you open a PR

Every PR must be signed off with the Developer Certificate of Origin (DCO):

```bash
git commit --signoff
```

PRs without `Signed-off-by:` in every commit cannot be merged.
By signing off you certify that you wrote the contribution, or have the
right to submit it under the license that applies to the touched path
(see `LICENSE-MAP.md`).

```bash
pip install ruff pytest
ruff check tools
ruff format --check tools
pytest tools/tests
python tools/runbook_validate.py --stage STAGE-XX
python tools/gen_spec_index.py && git diff --exit-code -- docs/specs/
```

CI runs exactly these checks. A red CI means the change is not ready.

## Adding a stage

1. Create `docs/ops/stages/STAGE-XX-NAME.md` using an existing card as the
   shape: trigger, inputs, steps, outputs, Definition of Done, hard stop,
   rollback, and a ready-to-paste prompt.
2. Register it in `docs/ops/RUNBOOK.md` and `docs/ops/STAGE-INDEX.csv`.
3. Declare machine-checkable assertions in
   `docs/ops/assertions/STAGE-XX.json`. If an outcome cannot be checked
   mechanically, declare it with the `manual` kind — do not fake a check.
4. Add a skill in `skills/ci-stage-XX-<slug>/SKILL.md` and register it in
   `skills/README.md`.
5. Update `docs/ops/STAGE-STATUS.md`.

## Adding a validator check

1. Add a `check_<kind>` function to `tools/runbook_validate.py` that takes
   `(ctx, params)` and returns `(status, detail)`.
2. Register it in the `CHECKS` dictionary.
3. Cover it in `tools/tests/test_runbook_validate.py` — including the failing
   case.
4. Document the new kind in `docs/ops/ASSERTIONS.md`.

Statuses are `PASS`, `FAIL`, `WAIT` (a human decision is required), and `SKIP`
(for things no machine can verify). Never convert a `WAIT` into a silent pass.

## Style

- Identifiers, event names, API and database fields are English, exactly as in
  the archive. Narrative documentation is Russian.
- No new runtime dependencies in `tools/` — standard library only. Dev
  dependencies live in the `dev` extra.
- Prefer a mechanical check over a prose promise.
- Line length 100, double quotes, `ruff format` is the source of truth.

## Reporting a problem

Use the issue templates. A useful bug report includes the exact command, the
expected result and the actual output.

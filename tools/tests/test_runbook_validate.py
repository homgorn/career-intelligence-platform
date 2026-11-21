"""Тесты валидатора runbook'а.

Шов — публичные функции проверок `CHECKS`: им передаётся временный корень,
поэтому тесты не трогают реальные артефакты проекта.
"""

from __future__ import annotations

import hashlib
import json

import pytest
import runbook_validate as rv
from conftest import write


@pytest.fixture()
def ctx(tmp_path):
    return rv.Ctx(tmp_path)


def test_file_exists_pass_and_fail(ctx):
    write(ctx.path("a.md"), "x")
    assert rv.check_file_exists(ctx, {"path": "a.md"})[0] == rv.PASS
    assert rv.check_file_exists(ctx, {"path": "missing.md"})[0] == rv.FAIL


def test_dir_exists(ctx):
    ctx.path("sub").mkdir()
    assert rv.check_dir_exists(ctx, {"path": "sub"})[0] == rv.PASS
    assert rv.check_dir_exists(ctx, {"path": "nope"})[0] == rv.FAIL


def test_json_valid_rejects_broken_json(ctx):
    write(ctx.path("bad.json"), "{not json")
    status, detail = rv.check_json_valid(ctx, {"path": "bad.json"})
    assert status == rv.FAIL
    assert "невалидный JSON" in detail


def test_json_valid_missing_file(ctx):
    assert rv.check_json_valid(ctx, {"path": "none.json"})[0] == rv.FAIL


def test_tsv_rows_min(ctx):
    write(ctx.path("d.tsv"), "a\t1\nb\t2\n")
    assert rv.check_tsv_rows_min(ctx, {"path": "d.tsv", "min": 2})[0] == rv.PASS
    assert rv.check_tsv_rows_min(ctx, {"path": "d.tsv", "min": 3})[0] == rv.FAIL


def test_nonempty_field_finds_empty_values(ctx):
    write(
        ctx.path("b.json"),
        json.dumps({"tasks": [{"customer_value": "yes"}, {"customer_value": "  "}]}),
    )
    status, detail = rv.check_nonempty_field(
        ctx, {"path": "b.json", "pointer": "tasks[*].customer_value"}
    )
    assert status == rv.FAIL
    assert "1 пустых" in detail


def test_nonempty_field_pointer_not_found(ctx):
    write(ctx.path("b.json"), json.dumps({"tasks": []}))
    assert rv.check_nonempty_field(ctx, {"path": "b.json", "pointer": "other[*].x"})[0] == rv.FAIL


def test_nonempty_field_accepts_filled_list(ctx):
    write(ctx.path("b.json"), json.dumps({"tasks": [{"a": [1]}, {"a": [2]}]}))
    assert rv.check_nonempty_field(ctx, {"path": "b.json", "pointer": "tasks[*].a"})[0] == rv.PASS


def test_deps_exist_flags_unknown_dependency(ctx):
    write(
        ctx.path("b.json"),
        json.dumps(
            {
                "tasks": [
                    {"id": "T1", "depends_on": ["T2"]},
                    {"id": "T2", "depends_on": []},
                    {"id": "T3", "depends_on": ["GHOST"]},
                ]
            }
        ),
    )
    status, detail = rv.check_deps_exist(ctx, {"path": "b.json"})
    assert status == rv.FAIL
    assert "GHOST" in detail


def test_deps_acyclic_detects_cycle(ctx):
    write(
        ctx.path("b.json"),
        json.dumps(
            {
                "tasks": [
                    {"id": "T1", "depends_on": ["T2"]},
                    {"id": "T2", "depends_on": ["T1"]},
                ]
            }
        ),
    )
    assert rv.check_deps_acyclic(ctx, {"path": "b.json"})[0] == rv.FAIL


def test_deps_acyclic_passes_dag(ctx):
    write(
        ctx.path("b.json"),
        json.dumps(
            {
                "tasks": [
                    {"id": "T1", "depends_on": []},
                    {"id": "T2", "depends_on": ["T1"]},
                ]
            }
        ),
    )
    assert rv.check_deps_acyclic(ctx, {"path": "b.json"})[0] == rv.PASS


def test_canonical_events_requires_all_seventeen(ctx):
    doc = " ".join(rv.CANONICAL_EVENTS)
    write(ctx.path("events.md"), doc)
    assert rv.check_canonical_events(ctx, {"path": "events.md"})[0] == rv.PASS

    write(ctx.path("short.md"), doc.replace("policy.blocked", ""))
    status, detail = rv.check_canonical_events(ctx, {"path": "short.md"})
    assert status == rv.FAIL
    assert "policy.blocked" in detail


def test_canonical_events_count_is_stable():
    assert len(rv.CANONICAL_EVENTS) == 17


def test_human_signed_waits_without_signature(ctx):
    write(ctx.path("p.md"), "# Пилот\nРешение: X\n")
    assert rv.check_human_signed(ctx, {"path": "p.md"})[0] == rv.WAIT


def test_human_signed_reads_owner_and_date(ctx):
    write(ctx.path("p.md"), "---\nsigned_by: owner\nsigned_at: 2026-11-16\n---\n")
    status, detail = rv.check_human_signed(ctx, {"path": "p.md"})
    assert status == rv.PASS
    assert "owner" in detail and "2026-11-16" in detail


@pytest.mark.parametrize(
    "line,expected",
    [
        ("STATUS: PASS", rv.PASS),
        ("STATUS: CONDITIONAL_PASS", rv.WAIT),
        ("STATUS: FAIL", rv.FAIL),
        ("P0_STATUS: PASS", rv.PASS),
    ],
)
def test_gate_status_parses_verdicts(ctx, line, expected):
    write(ctx.path("gate.md"), f"# Gate\n{line}\n")
    assert rv.check_gate_status(ctx, {"path": "gate.md"})[0] == expected


def test_gate_status_ignores_template_placeholder(ctx):
    """Шаблон с `STATUS: PASS | CONDITIONAL_PASS | FAIL` не должен считаться PASS."""
    write(ctx.path("template.md"), "STATUS: PASS | CONDITIONAL_PASS | FAIL\n")
    assert rv.check_gate_status(ctx, {"path": "template.md"})[0] == rv.FAIL


def test_next_task_single(ctx):
    write(ctx.path("next.md"), "TASK-P0-003 выбрать.\n")
    assert rv.check_next_task_single(ctx, {"path": "next.md"})[0] == rv.PASS

    write(ctx.path("zero.md"), "задача ещё не выбрана\n")
    assert rv.check_next_task_single(ctx, {"path": "zero.md"})[0] == rv.FAIL

    write(ctx.path("two.md"), "TASK-P0-003 или TASK-P1-001?\n")
    assert rv.check_next_task_single(ctx, {"path": "two.md"})[0] == rv.FAIL


def test_archive_hashes_detects_stale_hash(ctx):
    archive = ctx.path("career-intelligence-research-specs-v02")
    archive.mkdir()
    target = archive / "spec.md"
    target.write_text("content", encoding="utf-8")
    real = hashlib.sha256(b"content").hexdigest()

    write(ctx.path("docs/specs/SPEC_INDEX_DATA.tsv"), f"spec.md\t7\t{real}\n")
    assert rv.check_archive_hashes(ctx, {})[0] == rv.PASS, rv.check_archive_hashes(ctx, {})

    write(ctx.path("docs/specs/SPEC_INDEX_DATA.tsv"), f"spec.md\t8\t{'0' * 64}\n")
    assert rv.check_archive_hashes(ctx, {})[0] == rv.FAIL


def test_archive_hashes_detects_missing_entry(ctx):
    archive = ctx.path("career-intelligence-research-specs-v02")
    archive.mkdir()
    (archive / "new.md").write_text("x", encoding="utf-8")
    # TSV без новой записи: покрывает «новый файл на диске, нет в TSV».
    # Случай «TSV отсутствует» покрывает test_archive_hashes_fails_without_tsv.
    write(ctx.path("docs/specs/SPEC_INDEX_DATA.tsv"), "old.md\t1\t" + "0" * 64 + "\n")
    status, detail = rv.check_archive_hashes(ctx, {})
    assert status == rv.FAIL
    assert "new.md" in detail


def test_archive_hashes_fails_without_tsv(ctx):
    ctx.path("career-intelligence-research-specs-v02").mkdir(parents=True)
    status, detail = rv.check_archive_hashes(ctx, {})
    assert status == rv.FAIL
    assert "SPEC_INDEX_DATA.tsv" in detail


def test_spec_index_mentions_all(ctx):
    archive = ctx.path("career-intelligence-research-specs-v02")
    archive.mkdir()
    (archive / "one.md").write_text("x", encoding="utf-8")
    (archive / "two.md").write_text("y", encoding="utf-8")
    write(
        ctx.path("docs/specs/SPEC_INDEX_DATA.tsv"),
        f"one.md\t1\t{hashlib.sha256(b'x').hexdigest()}\n"
        f"two.md\t1\t{hashlib.sha256(b'y').hexdigest()}\n",
    )

    write(ctx.path("docs/specs/SPEC_INDEX.md"), "Упоминает `one.md`, но не второе.\n")
    status, detail = rv.check_spec_index_mentions_all(ctx, {})
    assert status == rv.FAIL, detail
    assert "two.md" in detail

    write(ctx.path("docs/specs/SPEC_INDEX.md"), "`one.md` и `two.md`\n")
    assert rv.check_spec_index_mentions_all(ctx, {})[0] == rv.PASS


def test_manual_check_is_skip_with_note(ctx):
    status, detail = rv.check_manual(ctx, {"note": "проверяет человек"})
    assert status == rv.SKIP
    assert "человек" in detail


CARD_BODY = """# STAGE

## Trigger

x

## Inputs

x

## Outputs

x

## Definition of Done

- [ ] x

## HARD STOP

x

## Rollback

x

## Промпт для IDE

```text
x
```
"""

CSV_HEADER = "stage_id,name,former_prompt,archive_task,depends_on,gate,status\n"


def seed_registry(ctx, stages=("STAGE-00", "STAGE-01")) -> None:
    write(
        ctx.path("docs/ops/STAGE-INDEX.csv"),
        CSV_HEADER + "".join(f"{s},Name,-,-,-,stage,pending\n" for s in stages),
    )
    for s in stages:
        write(ctx.path(f"docs/ops/stages/{s}-DEMO.md"), CARD_BODY)
        write(
            ctx.path(f"skills/ci-{s.lower()}-demo/SKILL.md"),
            f"---\nname: ci-{s.lower()}-demo\ndescription: demo\n---\n\nbody\n",
        )
        write(
            ctx.path(f"docs/ops/assertions/{s}.json"),
            json.dumps({"stage": s, "depends_on": [], "inputs": [], "outputs": [], "checks": []}),
        )


def test_stage_registry_consistent_pass(ctx):
    seed_registry(ctx)
    status, detail = rv.check_stage_registry_consistent(ctx, {})
    assert status == rv.PASS, detail


def test_stage_registry_flags_missing_card(ctx):
    seed_registry(ctx)
    ctx.path("docs/ops/stages/STAGE-01-DEMO.md").unlink()
    status, detail = rv.check_stage_registry_consistent(ctx, {})
    assert status == rv.FAIL
    assert "STAGE-01" in detail


def test_stage_registry_flags_missing_section(ctx):
    seed_registry(ctx)
    write(
        ctx.path("docs/ops/stages/STAGE-01-DEMO.md"), CARD_BODY.replace("## Outputs", "## Выходы")
    )
    status, detail = rv.check_stage_registry_consistent(ctx, {})
    assert status == rv.FAIL
    assert "## Outputs" in detail


def test_stage_registry_flags_orphan_card(ctx):
    seed_registry(ctx)
    write(ctx.path("docs/ops/stages/STAGE-99-GHOST.md"), CARD_BODY)
    status, detail = rv.check_stage_registry_consistent(ctx, {})
    assert status == rv.FAIL
    assert "вне реестра" in detail


def test_skills_cover_stages_pass(ctx):
    seed_registry(ctx)
    status, detail = rv.check_skills_cover_stages(ctx, {})
    assert status == rv.PASS, detail


def test_skills_flags_missing_skill(ctx):
    seed_registry(ctx)
    import shutil

    shutil.rmtree(ctx.path("skills/ci-stage-01-demo"))
    status, detail = rv.check_skills_cover_stages(ctx, {})
    assert status == rv.FAIL
    assert "STAGE-01" in detail


def test_skills_flags_frontmatter_mismatch(ctx):
    seed_registry(ctx)
    write(
        ctx.path("skills/ci-stage-00-demo/SKILL.md"),
        "---\nname: wrong-name\ndescription: demo\n---\n",
    )
    status, detail = rv.check_skills_cover_stages(ctx, {})
    assert status == rv.FAIL
    assert "frontmatter" in detail


def test_assertions_cover_stages_pass(ctx):
    seed_registry(ctx)
    status, detail = rv.check_assertions_cover_stages(ctx, {})
    assert status == rv.PASS, detail


def test_assertions_flags_missing_declaration(ctx):
    seed_registry(ctx)
    ctx.path("docs/ops/assertions/STAGE-01.json").unlink()
    status, detail = rv.check_assertions_cover_stages(ctx, {})
    assert status == rv.FAIL
    assert "STAGE-01" in detail


def test_markdown_links_resolve_pass(ctx):
    write(ctx.path("docs/guide.md"), "target")
    write(ctx.path("README.md"), "См. [гид](docs/guide.md) и [внешнее](https://example.org).\n")
    status, detail = rv.check_markdown_links_resolve(ctx, {"paths": ["README.md", "docs"]})
    assert status == rv.PASS, detail


def test_markdown_links_resolve_flags_missing_target(ctx):
    write(ctx.path("docs/guide.md"), "target")
    write(ctx.path("README.md"), "См. [гид](docs/guide.md) и [пропажу](docs/gone.md).\n")
    status, detail = rv.check_markdown_links_resolve(ctx, {"paths": ["README.md", "docs"]})
    assert status == rv.FAIL
    assert "docs/gone.md" in detail
    assert "README.md" in detail


def test_markdown_links_resolve_ignores_anchors_and_mailto(ctx):
    write(ctx.path("README.md"), "[якорь](#section) [почта](mailto:a@b.c) [внешнее](https://x.y)\n")
    status, detail = rv.check_markdown_links_resolve(ctx, {"paths": ["README.md"]})
    assert status == rv.PASS
    assert "проверено ссылок: 0" in detail


def test_markdown_links_resolve_handles_badge_links(ctx):
    write(ctx.path("docs/LICENSE.md"), "license")
    write(ctx.path("README.md"), "[![badge](https://img.example/b.svg)](docs/LICENSE.md)\n")
    status, detail = rv.check_markdown_links_resolve(ctx, {"paths": ["README.md"]})
    assert status == rv.PASS, detail


def test_markdown_links_resolve_ignores_anchor_suffix(ctx):
    write(ctx.path("docs/ADR-0001.md"), "adr")
    write(ctx.path("README.md"), "[решение](docs/ADR-0001.md#контекст)\n")
    status, detail = rv.check_markdown_links_resolve(ctx, {"paths": ["README.md"]})
    assert status == rv.PASS, detail


def test_markdown_links_resolve_ignores_links_in_code(ctx):
    write(
        ctx.path("README.md"),
        "Пример: `[битая](docs/gone.md)` и блок:\n\n```md\n[тоже битая](docs/gone.md)\n```\n",
    )
    status, detail = rv.check_markdown_links_resolve(ctx, {"paths": ["README.md"]})
    assert status == rv.PASS, detail
    assert "проверено ссылок: 0" in detail


def test_min_occurrences_counts_matches(ctx):
    write(ctx.path("risks.md"), "| R-01 | a |\n| R-02 | b |\n")
    status, detail = rv.check_min_occurrences(
        ctx, {"path": "risks.md", "pattern": r"^\|\s*R-\d+", "min": 2}
    )
    assert status == rv.PASS, detail

    status, detail = rv.check_min_occurrences(
        ctx, {"path": "risks.md", "pattern": r"^\|\s*R-\d+", "min": 3}
    )
    assert status == rv.FAIL
    assert "2" in detail


def test_min_occurrences_rejects_bad_regex(ctx):
    write(ctx.path("a.md"), "x")
    status, detail = rv.check_min_occurrences(ctx, {"path": "a.md", "pattern": "([", "min": 1})
    assert status == rv.FAIL
    assert "шаблон" in detail


def test_frontmatter_equals_pass(ctx):
    write(ctx.path("adr.md"), "---\nstatus: ACCEPTED\n---\n\ntext\n")
    status, detail = rv.check_frontmatter_equals(
        ctx, {"path": "adr.md", "field": "status", "equals": "ACCEPTED"}
    )
    assert status == rv.PASS, detail


def test_frontmatter_equals_mismatch(ctx):
    write(ctx.path("adr.md"), "---\nstatus: PROPOSED\n---\n")
    status, detail = rv.check_frontmatter_equals(
        ctx, {"path": "adr.md", "field": "status", "equals": "ACCEPTED"}
    )
    assert status == rv.FAIL
    assert "PROPOSED" in detail


def test_frontmatter_equals_missing_field_and_block(ctx):
    write(ctx.path("a.md"), "---\ntitle: x\n---\n")
    assert (
        rv.check_frontmatter_equals(ctx, {"path": "a.md", "field": "status", "equals": "ACCEPTED"})[
            0
        ]
        == rv.FAIL
    )

    write(ctx.path("b.md"), "нет frontmatter\n")
    assert (
        rv.check_frontmatter_equals(ctx, {"path": "b.md", "field": "status", "equals": "ACCEPTED"})[
            0
        ]
        == rv.FAIL
    )


def test_real_registry_is_consistent():
    """Инвариант проекта: реестр, карточки, скиллы и декларации согласованы."""
    ctx = rv.Ctx(rv.ROOT)
    for check in (
        rv.check_stage_registry_consistent,
        rv.check_skills_cover_stages,
        rv.check_assertions_cover_stages,
    ):
        status, detail = check(ctx, {})
        assert status == rv.PASS, f"{check.__name__}: {detail}"


def test_real_archive_hashes_are_current():
    """Инвариант проекта: хэши в TSV совпадают с диском."""
    status, _ = rv.check_archive_hashes(rv.Ctx(rv.ROOT), {})
    assert status == rv.PASS, "SPEC_INDEX_DATA.tsv устарел: python tools/gen_spec_index.py"


def test_real_backlog_has_no_cycles():
    status, _ = rv.check_deps_acyclic(rv.Ctx(rv.ROOT), {})
    assert status == rv.PASS

"""Тесты генератора индекса и установщика скиллов.

Оба инструмента читают модульные константы путей, поэтому тесты подменяют их
на временный каталог и не пишут в репозиторий.
"""

from __future__ import annotations

import hashlib
import json

import gen_spec_index as gi
import install_skills as inst
import pytest
from conftest import read

# --------------------------------------------------------------------------
# gen_spec_index
# --------------------------------------------------------------------------


@pytest.fixture()
def gen_env(tmp_path, monkeypatch):
    archive = tmp_path / "archive"
    archive.mkdir()
    (archive / "a.md").write_text("alpha", encoding="utf-8")
    (archive / "b.md").write_text("beta", encoding="utf-8")

    status = tmp_path / "SPEC_STATUS.json"
    status.write_text(
        json.dumps(
            {
                "files": {
                    "a.md": {"status": "canonical", "relevance": "high", "note": "A"},
                }
            }
        ),
        encoding="utf-8",
    )

    index = tmp_path / "SPEC_INDEX.md"
    index.write_text(
        "# SPEC_INDEX\n\n"
        f"{gi.BEGIN}\nстарое содержимое, должно исчезнуть\n{gi.END}\n\n"
        "## Конфликты\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(gi, "ARCHIVE", archive)
    monkeypatch.setattr(gi, "STATUS_FILE", status)
    monkeypatch.setattr(gi, "INDEX_FILE", index)
    monkeypatch.setattr(gi, "TSV_FILE", tmp_path / "SPEC_INDEX_DATA.tsv")
    return tmp_path


def test_generator_writes_tsv_and_table(gen_env, capsys):
    assert gi.main() == 0
    tsv = read(gen_env / "SPEC_INDEX_DATA.tsv").strip().splitlines()
    assert len(tsv) == 2
    name, size, digest = tsv[0].split("\t")
    assert name == "a.md"
    assert size == str(len("alpha"))
    assert digest == hashlib.sha256(b"alpha").hexdigest()

    doc = read(gen_env / "SPEC_INDEX.md")
    assert "`a.md`" in doc and "`b.md`" in doc
    assert "старое содержимое" not in doc
    assert "## Конфликты" in doc


def test_generator_is_idempotent(gen_env):
    gi.main()
    first = (gen_env / "SPEC_INDEX.md").read_bytes()
    gi.main()
    second = (gen_env / "SPEC_INDEX.md").read_bytes()
    assert first == second


def test_generator_warns_about_unmapped_files(gen_env, capsys):
    gi.main()
    out = capsys.readouterr().out
    assert "без кураторской записи" in out
    assert "b.md" in out


def test_generator_defaults_unmapped_to_reference(gen_env):
    gi.main()
    doc = read(gen_env / "SPEC_INDEX.md")
    row_b = next(line for line in doc.splitlines() if "`b.md`" in line)
    assert "reference" in row_b


def test_real_archive_index_matches_disk():
    status_map = json.loads(read(gi.ROOT / "docs/specs/SPEC_STATUS.json"))["files"]
    actual = {p.name for p in gi.ARCHIVE.iterdir() if p.is_file()}
    assert set(status_map) == actual, "SPEC_STATUS.json разошёлся с архивом"


# --------------------------------------------------------------------------
# install_skills
# --------------------------------------------------------------------------


@pytest.fixture()
def inst_env(tmp_path, monkeypatch):
    target = tmp_path / "skills"
    monkeypatch.setattr(inst, "target_dir", lambda: target)
    return target


def run_install(monkeypatch, capsys, args=None):
    monkeypatch.setattr("sys.argv", ["install_skills.py"] + (args or []))
    code = inst.main()
    return code, capsys.readouterr().out


def test_install_copies_all_project_skills(inst_env, monkeypatch, capsys):
    expected = [
        p.name
        for p in inst.SOURCE.iterdir()
        if p.name.startswith(inst.PREFIX) and (p / "SKILL.md").exists()
    ]
    code, out = run_install(monkeypatch, capsys)
    assert code == 0
    installed = [p.name for p in inst_env.iterdir()] if inst_env.is_dir() else []
    assert sorted(installed) == sorted(expected)
    assert f"Установлено: {len(expected)}" in out


def test_uninstall_removes_only_project_skills(inst_env, monkeypatch, capsys):
    run_install(monkeypatch, capsys)
    (inst_env / "foreign-skill").mkdir()
    code, out = run_install(monkeypatch, capsys, ["--uninstall"])
    assert code == 0
    assert "foreign-skill" in [p.name for p in inst_env.iterdir()]
    assert not (inst_env / "ci-runbook").exists()


def test_status_reports_mismatch(inst_env, monkeypatch, capsys):
    run_install(monkeypatch, capsys)
    skill_md = inst_env / "ci-runbook" / "SKILL.md"
    skill_md.write_text("изменено локально", encoding="utf-8")
    code, out = run_install(monkeypatch, capsys, ["--status"])
    assert code == 0
    assert "ОТЛИЧАЕТСЯ" in out


def test_install_without_force_keeps_local_changes(inst_env, monkeypatch, capsys):
    run_install(monkeypatch, capsys)
    skill_md = inst_env / "ci-runbook" / "SKILL.md"
    skill_md.write_text("local edit", encoding="utf-8")
    code, out = run_install(monkeypatch, capsys)
    assert code == 0
    assert "[SKIP]" in out
    assert skill_md.read_text(encoding="utf-8") == "local edit"

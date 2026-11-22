"""Тесты селектора следующей задачи.

Шов — CLI `main()`: подменяем корень, бэклог, пилот и argv через monkeypatch,
поэтому тесты не зависят от реального состояния проекта.
"""

from __future__ import annotations

import json

import pytest
import runbook_next as rn
from conftest import write


@pytest.fixture()
def env(tmp_path, monkeypatch):
    """Временный корень с подконтрольными бэклогом, пилотом и gate-файлами."""

    def make_backlog(tasks: list[dict]) -> None:
        write(
            tmp_path / "docs/tasks/MASTER_BACKLOG.json",
            json.dumps({"tasks": tasks}, ensure_ascii=False),
        )

    def sign_pilot(signed: bool = True) -> None:
        block = "---\nsigned_by: owner\nsigned_at: 2026-11-16\n---\n" if signed else "# Черновик\n"
        write(tmp_path / "docs/architecture/PILOT_DECISION.md", block)

    def set_gate(level: str, verdict: str) -> None:
        write(
            tmp_path / f"docs/gates/RELEASE-GATE-{level}.md",
            f"# Gate {level}\nSTATUS: {verdict}\n",
        )

    monkeypatch.setattr(rn, "ROOT", tmp_path)
    monkeypatch.setattr(rn, "BACKLOG", tmp_path / "docs/tasks/MASTER_BACKLOG.json")
    monkeypatch.setattr(rn, "PILOT", tmp_path / "docs/architecture/PILOT_DECISION.md")
    monkeypatch.setattr(rn, "PROJECT_ROOT", tmp_path, raising=False)
    return type(
        "Env",
        (),
        {
            "backlog": staticmethod(make_backlog),
            "pilot": staticmethod(sign_pilot),
            "gate": staticmethod(set_gate),
        },
    )()


def run_cli(monkeypatch, capsys, args=None):
    monkeypatch.setattr("sys.argv", ["runbook_next"] + (args or []))
    code = rn.main()
    captured = capsys.readouterr().out
    return code, captured


def task(tid, priority="P0", status="PENDING", deps=(), **extra):
    base = {
        "id": tid,
        "title": f"Задача {tid}",
        "priority": priority,
        "status": status,
        "depends_on": list(deps),
    }
    base.update(extra)
    return base


def test_pilot_task_is_selectable_without_signature(env, monkeypatch, capsys):
    """Задача, создающая PILOT_DECISION, не блокируется отсутствием пилота."""
    env.backlog(
        [
            task("TASK-P0-001", produces_pilot_decision=True),
            task("TASK-P0-002", deps=["TASK-P0-001"], value_score=100),
        ]
    )
    code, out = run_cli(monkeypatch, capsys)
    assert code == 0
    assert "TASK: TASK-P0-001" in out
    assert "создающая PILOT_DECISION" in out


def test_without_pilot_task_everything_blocks(env, monkeypatch, capsys):
    env.backlog([task("TASK-P0-002")])
    code, out = run_cli(monkeypatch, capsys)
    assert code == 2
    assert "BLOCKED_ON_PILOT" in out


def test_missing_pilot_blocks(env, monkeypatch, capsys):
    env.backlog([task("TASK-P0-001")])
    code, out = run_cli(monkeypatch, capsys)
    assert code == 2
    assert "BLOCKED_ON_PILOT" in out


def test_unsigned_pilot_blocks(env, monkeypatch, capsys):
    env.backlog([task("TASK-P0-001")])
    env.pilot(signed=False)
    code, out = run_cli(monkeypatch, capsys)
    assert code == 2
    assert "BLOCKED_ON_PILOT" in out


def test_signed_pilot_opens_p0(env, monkeypatch, capsys):
    env.backlog([task("TASK-P0-001"), task("TASK-P0-002", deps=["TASK-P0-001"])])
    env.pilot()
    code, out = run_cli(monkeypatch, capsys)
    assert code == 0
    assert "TASK-P0-001" in out
    assert "Разрешённые приоритеты: P0" in out


def test_dependency_not_done_excludes_task(env, monkeypatch, capsys):
    """Задача с незакрытой зависимостью исключается даже при высоком score."""
    env.backlog(
        [
            task("TASK-P0-001", status="PENDING", value_score=1),
            # P0-002 зависит от P0-001 (не DONE) — не должен выиграть despite score 99.
            task("TASK-P0-002", deps=["TASK-P0-001"], value_score=99),
            task("TASK-P0-003", deps=[], value_score=1),
        ]
    )
    env.pilot()
    code, out = run_cli(monkeypatch, capsys)
    assert code == 0
    # P0-002 исключён: его зависимость P0-001 не DONE.
    # P0-001 и P0-003 имеют равный score 1 → выигрывает алфавитный P0-001.
    assert "TASK: TASK-P0-001" in out
    assert "TASK-P0-002" not in out


def test_p1_forbidden_until_p0_gate_passes(env, monkeypatch, capsys):
    env.backlog(
        [
            task("TASK-P0-001", status="DONE"),
            task("TASK-P1-001", priority="P1", deps=["TASK-P0-001"]),
        ]
    )
    env.pilot()
    env.gate("P0", "FAIL")
    code, out = run_cli(monkeypatch, capsys)
    assert code == 2
    assert "[BLOCKED] нет подходящей задачи" in out
    assert "TASK-P1-001: priority P1" in out
    assert "TASK:" not in out


def test_p1_allowed_after_p0_gate_pass(env, monkeypatch, capsys):
    env.backlog(
        [
            task("TASK-P0-001", status="DONE"),
            task("TASK-P1-001", priority="P1", deps=["TASK-P0-001"]),
        ]
    )
    env.pilot()
    env.gate("P0", "PASS")
    code, out = run_cli(monkeypatch, capsys)
    assert code == 0
    assert "TASK-P1-001" in out


def test_priority_respects_score(env, monkeypatch, capsys):
    env.backlog(
        [
            task("TASK-P0-001", value_score=2, risk_score=0, cost_score=0),
            task("TASK-P0-002", value_score=9, risk_score=1, cost_score=0),
        ]
    )
    env.pilot()
    code, out = run_cli(monkeypatch, capsys)
    assert code == 0
    assert "TASK-P0-002" in out
    assert "score (value-risk-cost): 8" in out


def test_unscored_tasks_flag_needs_human(env, monkeypatch, capsys):
    env.backlog([task("TASK-P0-001")])
    env.pilot()
    code, out = run_cli(monkeypatch, capsys)
    assert code == 0
    assert "требует человека" in out


def test_json_output_shape(env, monkeypatch, capsys):
    env.backlog([task("TASK-P0-001")])
    env.pilot()
    code, out = run_cli(monkeypatch, capsys, args=["--json"])
    assert code == 0
    data = json.loads(out)
    assert data["pilot_signed"] is True
    assert data["selected"]["task_id"] == "TASK-P0-001"
    assert data["gates"]["P0"] is None


def test_no_eligible_task_reports_block(env, monkeypatch, capsys):
    env.backlog([task("TASK-P0-001", status="DONE")])
    env.pilot()
    code, out = run_cli(monkeypatch, capsys)
    assert code == 2
    assert "[BLOCKED] нет подходящей задачи" in out
    assert "TASK-P0-001: статус DONE" in out

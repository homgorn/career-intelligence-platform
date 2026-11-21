"""Тесты раннера локальных проверок `tools/check.py`.

Шов — `run` и `run_all`: им передаются произвольные шаги и рабочий каталог,
поэтому тесты не запускают собственный pytest рекурсивно и не зависят от
состояния проекта.
"""

from __future__ import annotations

import json
import sys

import check

PY = sys.executable


def ok_step(name: str = "ok") -> check.Step:
    return check.Step(name, [PY, "-c", "print('fine')"])


def fail_step(name: str = "fail") -> check.Step:
    return check.Step(name, [PY, "-c", "import sys; print('boom'); sys.exit(3)"])


def test_run_captures_success(tmp_path):
    name, code, out = check.run(ok_step(), cwd=tmp_path)
    assert name == "ok"
    assert code == 0
    assert "fine" in out


def test_run_captures_failure_output(tmp_path):
    name, code, out = check.run(fail_step(), cwd=tmp_path)
    assert code == 3
    assert "boom" in out


def test_run_reports_missing_command(tmp_path):
    step = check.Step("ghost", ["definitely-not-a-real-binary-xyz"])
    name, code, out = check.run(step, cwd=tmp_path)
    assert code == 127
    assert "не найдена" in out


def test_run_all_marks_failures(tmp_path):
    results = check.run_all([ok_step("a"), fail_step("b")], cwd=tmp_path)
    assert [r["status"] for r in results] == ["PASS", "FAIL"]
    assert results[0]["exit"] == 0
    assert results[1]["exit"] == 3


def test_run_all_honours_allow_exit(tmp_path):
    # Селектор до подписи пилота возвращает 2 — это валидный исход.
    step = check.Step("blocked", [PY, "-c", "import sys; sys.exit(2)"], allow_exit=(2,))
    assert check.run_all([step], cwd=tmp_path)[0]["status"] == "PASS"


def test_run_all_skips_quick_steps(tmp_path):
    steps = [
        check.Step("slow", [PY, "-c", "print('x')"], quick=True),
        ok_step("fast"),
    ]
    quick = check.run_all(steps, quick=True, cwd=tmp_path)
    assert quick[0]["status"] == "SKIP"
    assert quick[1]["status"] == "PASS"

    full = check.run_all(steps, quick=False, cwd=tmp_path)
    assert [r["status"] for r in full] == ["PASS", "PASS"]


def test_build_steps_covers_the_non_negotiable_checks():
    names = [s.name for s in check.build_steps(PY)]
    joined = " | ".join(names)
    for required in ("ruff check", "ruff format --check", "pytest", "validator ALWAYS"):
        assert required in joined, f"отсутствует обязательная проверка: {required}"
    assert any("git diff" in n for n in names), "нет гейта на дрейф индекса"


def test_build_steps_marks_expensive_steps_quick():
    by_name = {s.name: s for s in check.build_steps(PY)}
    assert by_name["gen_spec_index (перегенерация индекса)"].quick
    assert by_name["git diff (индекс соответствует архиву)"].quick
    assert not by_name["pytest"].quick


def test_selector_step_allows_blocked_exit():
    by_name = {s.name: s for s in check.build_steps(PY)}
    assert 2 in by_name["selector заблокирован пилотом"].allow_exit


def test_render_text_marks_failures_and_summary():
    results = [
        {"name": "a", "status": "PASS", "detail": ""},
        {"name": "b", "status": "FAIL", "detail": "stack trace", "exit": 1},
    ]
    text = check.render_text(results, [])
    assert "[PASS] a" in text
    assert "[FAIL] b" in text
    assert "stack trace" in text
    assert "1 шаг(ов) упало" in text


def test_render_text_all_green():
    text = check.render_text([{"name": "a", "status": "PASS", "detail": ""}], [])
    assert "всё зелёное" in text


def test_info_stages_exist_in_registry():
    """INFO_STAGES — список этапов с будущими артефактами; он не должен разъезжаться."""
    registry = (check.ROOT / "docs" / "ops" / "STAGE-INDEX.csv").read_text(encoding="utf-8")
    for stage in check.INFO_STAGES:
        assert stage in registry, f"{stage} нет в STAGE-INDEX.csv"


def test_main_json_output(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(check, "build_steps", lambda py: [ok_step("only")])
    monkeypatch.setattr(check, "collect_info", lambda py, cwd=None: [])
    code = check.main(["--json"])
    assert code == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["passed"] is True
    assert payload["results"][0]["name"] == "only"


def test_main_returns_one_when_a_step_fails(monkeypatch, capsys):
    monkeypatch.setattr(check, "build_steps", lambda py: [fail_step("bad")])
    monkeypatch.setattr(check, "collect_info", lambda py, cwd=None: [])
    assert check.main([]) == 1
    assert "[FAIL] bad" in capsys.readouterr().out


def test_main_skip_info_avoids_stage_calls(monkeypatch, capsys):
    called = {"info": False}

    def fake_info(py, cwd=None):
        called["info"] = True
        return []

    monkeypatch.setattr(check, "build_steps", lambda py: [ok_step("only")])
    monkeypatch.setattr(check, "collect_info", fake_info)
    assert check.main(["--skip-info"]) == 0
    assert called["info"] is False

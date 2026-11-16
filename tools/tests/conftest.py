"""Общая конфигурация тестов инструментов runbook'а."""

from __future__ import annotations

import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parents[1]
PROJECT_ROOT = TOOLS_DIR.parent

if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

ARCHIVE_DIR = PROJECT_ROOT / "career-intelligence-research-specs-v02"


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")

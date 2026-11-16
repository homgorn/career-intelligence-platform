#!/usr/bin/env python3
"""
Установщик скиллов проекта в рабочий каталог OpenCode.

Канонические скиллы версионируются в skills/. Каталог OpenCode:
~/.config/opencode/skills/ (Linux/macOS) или %APPDATA%/opencode/skills.

Запуск:
    python tools/install_skills.py            # установить/обновить
    python tools/install_skills.py --list     # что в репо и что установлено
    python tools/install_skills.py --status   # сравнение по хэшам
    python tools/install_skills.py --uninstall
    python tools/install_skills.py --force    # перезаписать изменённые

Скиллы с префиксом ci- принадлежат проекту. Чужие папки в каталоге
не трогаются.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "skills"
PREFIX = "ci-"


def target_dir() -> Path:
    if sys.platform.startswith("win"):
        base = Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
        candidate = base / "opencode" / "skills"
        if candidate.exists():
            return candidate
    return Path.home() / ".config" / "opencode" / "skills"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def project_skills() -> list[Path]:
    if not SOURCE.is_dir():
        return []
    return sorted(
        p
        for p in SOURCE.iterdir()
        if p.is_dir() and p.name.startswith(PREFIX) and (p / "SKILL.md").exists()
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Установка скиллов проекта")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--list", action="store_true")
    group.add_argument("--status", action="store_true")
    group.add_argument("--uninstall", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    dest_root = target_dir()
    skills = project_skills()

    if not skills:
        print(f"[ERROR] нет скиллов в {SOURCE}")
        return 1

    if args.list:
        installed = (
            {p.name for p in dest_root.iterdir() if p.is_dir()} if dest_root.is_dir() else set()
        )
        for skill in skills:
            mark = "установлен" if skill.name in installed else "не установлен"
            print(f"{skill.name:<40} {mark}")
        print(f"\nКаталог: {dest_root}")
        return 0

    if args.status:
        dest_root.mkdir(parents=True, exist_ok=True)
        for skill in skills:
            src_file = skill / "SKILL.md"
            dst_file = dest_root / skill.name / "SKILL.md"
            if not dst_file.exists():
                state = "нет в каталоге"
            elif digest(src_file) == digest(dst_file):
                state = "совпадает"
            else:
                state = "ОТЛИЧАЕТСЯ (изменён локально или устарел)"
            print(f"{skill.name:<40} {state}")
        return 0

    if args.uninstall:
        removed = 0
        for skill in skills:
            target = dest_root / skill.name
            if target.exists():
                shutil.rmtree(target)
                removed += 1
        print(f"Удалено скиллов: {removed}")
        return 0

    dest_root.mkdir(parents=True, exist_ok=True)
    copied = skipped = 0
    for skill in skills:
        target = dest_root / skill.name
        if target.exists() and not args.force:
            changed = [
                f
                for f in skill.rglob("*")
                if f.is_file() and digest(f) != digest(target / f.relative_to(skill))
            ]
            if changed:
                print(
                    f"[SKIP] {skill.name}: есть отличия, используй --force ({len(changed)} файлов)"
                )
                skipped += 1
                continue
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(skill, target)
        copied += 1

    print(f"Каталог: {dest_root}")
    print(f"Установлено: {copied}, пропущено: {skipped}")
    print("Перезапусти IDE, чтобы скиллы подхватились.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

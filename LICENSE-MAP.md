# LICENSE MAP — какие лицензии применяются к каким путям

Карта имеет приоритет над любым одиночным `LICENSE` в корне, который описывает
только код под MIT. Принятие этой карты зафиксировано в
`docs/decisions/ADR-0002-license-busl.md` (ACCEPTED 2026-11-16, владелец —
homgorn, в ответ на "делай ок").

| Путь | Лицензия | Файл |
| --- | --- | --- |
| `career-intelligence-research-specs-v02/` (archive) | CC BY 4.0 | `LICENSES/CC-BY-4.0.txt` |
| `docs/` (all documentation, runbook, specs, gates) | CC BY 4.0 | `LICENSES/CC-BY-4.0.txt` |
| `skills/` | MIT | `LICENSE` |
| `tools/` | MIT | `LICENSE` |
| `.github/` (CI, templates) | MIT | `LICENSE` |
| `README.md`, `README.ru.md`, `CONTRIBUTING.md`, `LICENSE*` | MIT | `LICENSE` |
| `engine/` (создаётся при появлении движка) | BUSL 1.1 | `LICENSES/BUSL-1.1.txt` |
| будущие policy packs / live recipes / verification runtime (определятся при создании `engine/`) | BUSL 1.1 | `LICENSES/BUSL-1.1.txt` |

## BUSL parameters (only for BUSL-licensed files)

- **Licensor**: Career Intelligence contributors, repository owner.
- **Change License**: GPL-3.0-or-later (satisfies the MariaDB covenant: Change License must be GPLv2-compatible).
- **Change Date**: 2 years from the date of each release of the Licensed Work (per-release conversion; independent dates per version).
- **Additional Use Grant**: Production use for one's own products is permitted; providing the Licensed Work as a hosted service, or as the basis of a competing hosted product, requires a commercial license.

## What stays MIT forever

History before adoption (commits up to and including `bc50614`) is MIT and
remains MIT. The docs/skills/tools layer is MIT by intent permanently.
The archive and docs are CC BY 4.0 permanently.

## What BUSL does NOT do

- It is not a security control and grants no confidentiality.
- It prevents no forks and no contributions under terms the owner accepts.
- It cannot retroactively relicense already published MIT code.

# Installation

Install the **whole `partner-801-preparation` folder**, not the `Subclass801` wrapper. It needs no skill-specific executable or package. Your agent must be able to read linked Markdown; document/browsing capabilities depend on the host.

## Download and copy
Extract the public skill ZIP. For a repository download, find `Subclass801/partner-801-preparation/`. Keep SKILL.md, references, templates, guides and licence together. Use a file manager with hidden folders visible; create the appropriate parent `skills` folder and copy the inner folder there. Avoid double nesting.

| Agent | Personal destination | Project destination | Activation |
|---|---|---|---|
| Claude Code | `~/.claude/skills/partner-801-preparation/` | `.claude/skills/partner-801-preparation/` | Ask to use this named skill; check slash-menu discovery |
| Codex | `~/.agents/skills/partner-801-preparation/` | `.agents/skills/partner-801-preparation/` | Select via skill menu or explicitly name the skill |

`~` means the user home folder; on Windows use the equivalent user-profile home. Project paths are inside the agent's actual workspace. These paths were checked against [Claude Code documentation](https://code.claude.com/docs/en/skills) and [Codex documentation](https://developers.openai.com/codex/skills) on 8 October 2026. Documentation-checked is not end-to-end tested. Account policies can restrict capability. Local folders do not automatically appear in web/cloud/remote sessions; follow that product's current custom-skill upload instructions rather than assuming a local copy works there.

## Hermes and other hosts
Use your host's documented active skills folder and copy the entire inner folder. In Hermes, confirm the active profile/home with its documentation or settings; do not put private maintenance sources into the applicant installation. Native Hermes installation is not performed by this package creation.

If native loading is unavailable, keep the folder accessible and say:
> Read partner-801-preparation/SKILL.md and every supporting reference it requires. Follow it for my subclass 801 preparation task.

For ordinary chat, attach readable files through supported context/attachments. ZIP access and persistent activation are not guaranteed. If the host cannot inspect documents or browse, use redacted readable text and leave unavailable checks Needs verification.

## Smoke test and maintenance
Start a new session and ask:
> Load partner-801-preparation. State your preparation scope and supporting files. Do not assess me yet.

Expected: disclaimer first, scope and reference loading, then at most one relevant question if needed. This does not establish policy accuracy. If discovery fails, check folder nesting, name, active workspace/profile, disabled skills and product support. Reload/restart as documented.

For updates, back up personal customisations, replace only this entire skill folder and reload. Installed copies do not auto-sync with GitHub. To remove it, delete only this folder or use the host's supported uninstall/disable control; do not delete case documents or other skills. See [usage](USAGE.md).

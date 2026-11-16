# Installation

## Choose CLI installation or a downloadable ZIP

Immigent® provides both options. Install only reusable skill files; no applicant documents are needed.

### Easiest option — Drag the ZIP into agent chat

For agents that support file attachments, opening ZIP files and installing skills:

1. Download this skill’s attached ZIP from the release page linked in Option B below. Choose the skill ZIP under Assets, not a Source code archive.
2. Drag the ZIP into your agent’s chat, or use its attachment button. You do not need to extract it first if the agent can open ZIPs.
3. Paste this request and approve only the intended installation permissions:

> Please inspect the attached ZIP and read its INSTALL.md. Install the complete `partner-801-preparation` skill, including its references, templates and other supporting files, using this agent’s supported installation method for the current profile or workspace. Preserve the supplied files; do not rewrite or summarise them. Ask before replacing an existing installation. Verify that the skill is discoverable, then tell me its name, version if supplied, installation location and how to start using it. If persistent installation is unavailable, explain the limitation instead of claiming success.

Attaching or reading the ZIP is not the same as installing it. If your agent cannot open the ZIP or install skills, use the CLI or manual instructions below, or its supported skill-upload interface. Check your provider’s file-processing and retention settings; attach only the reusable skill ZIP, not applicant records.

### Option A — CLI for supported local agents

Requires **Node.js 22.20 or later**, including npm/npx, and internet access. `npx` downloads and runs the third-party **Vercel Labs skills** installer; review its source, prompts and permissions. It is separate from Immigent® and from your agent. Its telemetry/security-audit settings are described in the [installer documentation](https://github.com/vercel-labs/skills/blob/main/docs/troubleshooting.md#telemetry).

Run from the project where you want to use the skill. This example selects Claude Code and copies the complete folder:

```bash
npx skills add ScriptSavvy/AustraliaVisaSkills --skill partner-801-preparation --agent claude-code --copy
```

Replace `claude-code` with **`codex`**, **`cursor`** or **`opencode`** for those agents. Use your agent's exact identifier from the [supported-agent list](https://github.com/vercel-labs/skills/blob/main/docs/agents.md); do not assume every AI app is supported. Specifying the agent avoids automatic selection of an unintended host. Review any proposed overwrite before accepting.

- Default: current-project installation. Add **`-g`** for user-wide installation across projects. Do not add it if you want project isolation.
- `--copy` requests copied files rather than agent-specific symlinks. Current installer project destinations include `.claude/skills/` for Claude Code and shared `.agents/skills/` for Codex, Cursor and OpenCode. Shared loaders can see the same folder; agent selection is not a security boundary.
- To discover available skills without installing: `npx skills add ScriptSavvy/AustraliaVisaSkills --list`. Use `--list` alone, not with `--json`.
- This command uses the repository's current default branch, **not a release ZIP**. Contents may differ from an attached release. For a specific packaged release, choose Option B.
- It does not install the host agent, enable missing capabilities, or upload a skill to ChatGPT/Claude web or remote workers. Use those products' own supported import methods.

CLI discovery and whole-folder copying were checked on **14 November 2026**, using installer **1.8.1** in an isolated project. This is not an end-to-end test of each host's activation, applicant responses or policy accuracy. Native destinations described elsewhere in this guide are manual alternatives, not additional copies you must install.

### Option B — ZIP download / no terminal

Open this skill's [release page](https://github.com/ScriptSavvy/AustraliaVisaSkills/releases/tag/subclass801) and download its attached **`partner-801-preparation-v<version>.zip`**. Choose the skill ZIP under Assets, not GitHub's automatic Source code archives or another skill's release. For manual installation instead, extract it and follow the instructions below. Keep the entire **`partner-801-preparation/`** folder, including references, templates, any scripts, guides and licence files; SKILL.md alone is not enough.

After either option, start a fresh agent session and run the smoke check below with synthetic facts. Installed copies do not automatically update. Before updating or removing, preserve customisations and case records; use the same installation scope and avoid duplicate manual/CLI copies. `npx skills list` (or `npx skills list -g` for user scope) checks installer discovery, not correct host behaviour.

Installer command/source basis: [Vercel Labs skills](https://github.com/vercel-labs/skills) and its [CLI reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md), checked 14 November 2026. No immigration-source verification dates were advanced.

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

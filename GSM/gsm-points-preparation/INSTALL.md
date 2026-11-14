# Install the whole skill folder

## Choose CLI installation or a downloadable ZIP

Immigent® provides both options. Install only reusable skill files; no applicant documents are needed.

### Option A — CLI for supported local agents

Requires **Node.js 22.20 or later**, including npm/npx, and internet access. `npx` downloads and runs the third-party **Vercel Labs skills** installer; review its source, prompts and permissions. It is separate from Immigent® and from your agent. Its telemetry/security-audit settings are described in the [installer documentation](https://github.com/vercel-labs/skills/blob/main/docs/troubleshooting.md#telemetry).

Run from the project where you want to use the skill. This example selects Claude Code and copies the complete folder:

```bash
npx skills add ScriptSavvy/AustraliaVisaSkills --skill gsm-points-preparation --agent claude-code --copy
```

Replace `claude-code` with **`codex`**, **`cursor`** or **`opencode`** for those agents. Use your agent's exact identifier from the [supported-agent list](https://github.com/vercel-labs/skills/blob/main/docs/agents.md); do not assume every AI app is supported. Specifying the agent avoids automatic selection of an unintended host. Review any proposed overwrite before accepting.

- Default: current-project installation. Add **`-g`** for user-wide installation across projects. Do not add it if you want project isolation.
- `--copy` requests copied files rather than agent-specific symlinks. Current installer project destinations include `.claude/skills/` for Claude Code and shared `.agents/skills/` for Codex, Cursor and OpenCode. Shared loaders can see the same folder; agent selection is not a security boundary.
- To discover available skills without installing: `npx skills add ScriptSavvy/AustraliaVisaSkills --list`. Use `--list` alone, not with `--json`.
- This command uses the repository's current default branch, **not a release ZIP**. Contents may differ from an attached release. For a specific packaged release, choose Option B.
- It does not install the host agent, enable missing capabilities, or upload a skill to ChatGPT/Claude web or remote workers. Use those products' own supported import methods.

CLI discovery and whole-folder copying were checked on **14 November 2026**, using installer **1.8.1** in an isolated project. This is not an end-to-end test of each host's activation, applicant responses or policy accuracy. Native destinations described elsewhere in this guide are manual alternatives, not additional copies you must install.

### Option B — ZIP download / no terminal

Open this skill's [release page](https://github.com/ScriptSavvy/AustraliaVisaSkills/releases/tag/gsm-points) and download its attached **`gsm-points-preparation-v<version>.zip`**. Choose the skill ZIP under Assets, not GitHub's automatic Source code archives or another skill's release. Extract it and follow the manual instructions below. Keep the entire **`gsm-points-preparation/`** folder, including references, templates, any scripts, guides and licence files; SKILL.md alone is not enough.

After either option, start a fresh agent session and run the smoke check below with synthetic facts. Installed copies do not automatically update. Before updating or removing, preserve customisations and case records; use the same installation scope and avoid duplicate manual/CLI copies. `npx skills list` (or `npx skills list -g` for user scope) checks installer discovery, not correct host behaviour.

Installer command/source basis: [Vercel Labs skills](https://github.com/vercel-labs/skills) and its [CLI reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md), checked 14 November 2026. No immigration-source verification dates were advanced.

No mandatory script, package, API key or plugin is required. Document inspection and official-source retrieval depend on your agent's capabilities. Python 3 is optional for the arithmetic helper.

## Portable manual method
1. Extract the ZIP. Keep `gsm-points-preparation/SKILL.md`, references, templates and guides together.
2. Place the folder where your agent can access it. Do not install the outer `GSM` wrapper or double-nest the inner folder.
3. Ask: “Read gsm-points-preparation/SKILL.md and all its required references. Follow it for this task.”
4. For a chat interface, attach the Markdown files through its supported mechanism. A ZIP attachment alone does not prove the agent can read its contents.

This method does not promise persistent/native skill discovery. For native installation, follow your agent's current official skill documentation and active profile/workspace conventions rather than assuming another product's path. No native installations are claimed for this package.

## Smoke check
Ask: “Load gsm-points-preparation. Display its opening notice, state its scope and required reference files, then ask only the first relevant intake question. Do not assess me yet.”

It should not ask for a complete applicant history or promise an assessed score. If unavailable, check filename, folder nesting and host file-reading support. Reload/new session may be necessary.

Update only this folder, backing up customisations first. Installed copies do not automatically track repository changes. Remove/disable only this skill; do not delete applicant case records or the host's entire skills directory. See [USAGE.md](USAGE.md).

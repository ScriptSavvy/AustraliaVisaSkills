# Installation

## Choose CLI installation or a downloadable ZIP

Immigent® provides both options. Install only reusable skill files; no applicant documents are needed.

### Easiest option — Drag the ZIP into agent chat

For agents that support file attachments, opening ZIP files and installing skills:

1. Download this skill’s attached ZIP from the release page linked in Option B below. Choose the skill ZIP under Assets, not a Source code archive.
2. Drag the ZIP into your agent’s chat, or use its attachment button. You do not need to extract it first if the agent can open ZIPs.
3. Paste this request and approve only the intended installation permissions:

> Please inspect the attached ZIP and read its INSTALL.md. Install the complete `visitor-600-preparation` skill, including its references, templates and other supporting files, using this agent’s supported installation method for the current profile or workspace. Preserve the supplied files; do not rewrite or summarise them. Ask before replacing an existing installation. Verify that the skill is discoverable, then tell me its name, version if supplied, installation location and how to start using it. If persistent installation is unavailable, explain the limitation instead of claiming success.

Attaching or reading the ZIP is not the same as installing it. If your agent cannot open the ZIP or install skills, use the CLI or manual instructions below, or its supported skill-upload interface. Check your provider’s file-processing and retention settings; attach only the reusable skill ZIP, not applicant records.

### Option A — CLI for supported local agents

Requires **Node.js 22.20 or later**, including npm/npx, and internet access. `npx` downloads and runs the third-party **Vercel Labs skills** installer; review its source, prompts and permissions. It is separate from Immigent® and from your agent. Its telemetry/security-audit settings are described in the [installer documentation](https://github.com/vercel-labs/skills/blob/main/docs/troubleshooting.md#telemetry).

Run from the project where you want to use the skill. This example selects Claude Code and copies the complete folder:

```bash
npx skills add ScriptSavvy/AustraliaVisaSkills --skill visitor-600-preparation --agent claude-code --copy
```

Replace `claude-code` with **`codex`**, **`cursor`** or **`opencode`** for those agents. Use your agent's exact identifier from the [supported-agent list](https://github.com/vercel-labs/skills/blob/main/docs/agents.md); do not assume every AI app is supported. Specifying the agent avoids automatic selection of an unintended host. Review any proposed overwrite before accepting.

- Default: current-project installation. Add **`-g`** for user-wide installation across projects. Do not add it if you want project isolation.
- `--copy` requests copied files rather than agent-specific symlinks. Current installer project destinations include `.claude/skills/` for Claude Code and shared `.agents/skills/` for Codex, Cursor and OpenCode. Shared loaders can see the same folder; agent selection is not a security boundary.
- To discover available skills without installing: `npx skills add ScriptSavvy/AustraliaVisaSkills --list`. Use `--list` alone, not with `--json`.
- This command uses the repository's current default branch, **not a release ZIP**. Contents may differ from an attached release. For a specific packaged release, choose Option B.
- It does not install the host agent, enable missing capabilities, or upload a skill to ChatGPT/Claude web or remote workers. Use those products' own supported import methods.

CLI discovery and whole-folder copying were checked on **14 November 2026**, using installer **1.8.1** in an isolated project. This is not an end-to-end test of each host's activation, applicant responses or policy accuracy. Native destinations described elsewhere in this guide are manual alternatives, not additional copies you must install.

### Option B — ZIP download / no terminal

Open this skill's [release page](https://github.com/ScriptSavvy/AustraliaVisaSkills/releases/tag/subclass600) and download its attached **`visitor-600-preparation-v<version>.zip`**. Choose the skill ZIP under Assets, not GitHub's automatic Source code archives or another skill's release. For manual installation instead, extract it and follow the instructions below. Keep the entire **`visitor-600-preparation/`** folder, including references, templates, any scripts, guides and licence files; SKILL.md alone is not enough.

After either option, start a fresh agent session and run the smoke check below with synthetic facts. Installed copies do not automatically update. Before updating or removing, preserve customisations and case records; use the same installation scope and avoid duplicate manual/CLI copies. `npx skills list` (or `npx skills list -g` for user scope) checks installer discovery, not correct host behaviour.

Installer command/source basis: [Vercel Labs skills](https://github.com/vercel-labs/skills) and its [CLI reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md), checked 14 November 2026. No immigration-source verification dates were advanced.

Install the complete **visitor-600-preparation** folder, not the Subclass600 wrapper and not SKILL.md alone. No executable scripts or API keys are required. Your agent needs Markdown reading, document reading for reviews, and preferably official browsing.

## No-terminal method
1. Download the public skill ZIP and extract it.
2. Locate visitor-600-preparation/SKILL.md. Keep references and templates beside it.
3. Copy the entire inner folder into your host's supported skill directory, or use the manual fallback below.
4. Open a fresh chat/session and run the smoke-test prompt. Do not upload the PRIVATE maintenance archive to a public repository or an applicant host.

## Documentation-checked local paths
| Host | Personal / project destination | Invoke / limitations |
|---|---|---|
| Claude Code | `~/.claude/skills/visitor-600-preparation/` or `<project>/.claude/skills/visitor-600-preparation/` | `/visitor-600-preparation`; requires a local Claude Code environment, not a promise about Claude web uploads |
| Codex local CLI/IDE | `~/.agents/skills/visitor-600-preparation/` or `<project>/.agents/skills/visitor-600-preparation/` | `/skills` or mention `$visitor-600-preparation`; local discovery does not copy files to remote/cloud environments |
| Other hosts, including Hermes | Consult that host's current skill-loader documentation and active profile; copy the whole folder | Native installation was not tested. Manual reading works when the host can access all files. Do not assume SOUL.md is loaded. |

Official docs checked 2026-10-07: Claude Code https://code.claude.com/docs/en/skills ; Codex https://developers.openai.com/codex/skills (redirected to https://learn.chatgpt.com/docs/build-skills ). Paths are documentation-checked, not installation-tested. Recheck for your installed version.

`~` means your home folder, not this project's folder. Dot-folders are hidden: enable hidden-file display in your file manager. Project paths are relative to the selected project. Avoid double nesting and duplicate personal/project installations. A cloud session may not see local files. Copying files does not itself prove discovery or enabled state.

## Manual fallback
Open SKILL.md in your agent or attach its text together with all three referenced Markdown files and the report template. Say: “Follow these preparation instructions for this task; read the linked references first.” If the host cannot read the supporting files, do not claim the skill is installed or fully active. This fallback is task-local, not native persistent installation.

## Smoke test (synthetic; no personal documents)
“Use visitor-600-preparation. Before any assessment, show its notice, state the scope and supporting files, then ask minimum inputs for an adult outside Australia planning a short holiday. Do not claim eligibility or approval.”

Expected: notice first; scope and reference loading; focused intake; no unsupported readiness finding. A manually reviewed synthetic walkthrough is not native skill discovery, a live host-agent execution or legal-currency verification.

## Update, disable or remove
Back up any customisations; replace the complete folder with a reviewed new release. Installed copies do not auto-update when a repository changes. Start a new session and repeat the smoke test. To disable/remove, use the host's supported mechanism or remove only this skill folder; do not delete applicant case files or other skills. Review host permissions/retention separately.

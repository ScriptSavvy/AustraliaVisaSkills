# Install the complete skill

## Choose CLI installation or a downloadable ZIP

Immigent® provides both options. Install only reusable skill files; no applicant documents are needed.

### Option A — CLI for supported local agents

Requires **Node.js 22.20 or later**, including npm/npx, and internet access. `npx` downloads and runs the third-party **Vercel Labs skills** installer; review its source, prompts and permissions. It is separate from Immigent® and from your agent. Its telemetry/security-audit settings are described in the [installer documentation](https://github.com/vercel-labs/skills/blob/main/docs/troubleshooting.md#telemetry).

Run from the project where you want to use the skill. This example selects Claude Code and copies the complete folder:

```bash
npx skills add ScriptSavvy/AustraliaVisaSkills --skill skills-in-demand-482-preparation --agent claude-code --copy
```

Replace `claude-code` with **`codex`**, **`cursor`** or **`opencode`** for those agents. Use your agent's exact identifier from the [supported-agent list](https://github.com/vercel-labs/skills/blob/main/docs/agents.md); do not assume every AI app is supported. Specifying the agent avoids automatic selection of an unintended host. Review any proposed overwrite before accepting.

- Default: current-project installation. Add **`-g`** for user-wide installation across projects. Do not add it if you want project isolation.
- `--copy` requests copied files rather than agent-specific symlinks. Current installer project destinations include `.claude/skills/` for Claude Code and shared `.agents/skills/` for Codex, Cursor and OpenCode. Shared loaders can see the same folder; agent selection is not a security boundary.
- To discover available skills without installing: `npx skills add ScriptSavvy/AustraliaVisaSkills --list`. Use `--list` alone, not with `--json`.
- This command uses the repository's current default branch, **not a release ZIP**. Contents may differ from an attached release. For a specific packaged release, choose Option B.
- It does not install the host agent, enable missing capabilities, or upload a skill to ChatGPT/Claude web or remote workers. Use those products' own supported import methods.

CLI discovery and whole-folder copying were checked on **14 November 2026**, using installer **1.8.1** in an isolated project. This is not an end-to-end test of each host's activation, applicant responses or policy accuracy. Native destinations described elsewhere in this guide are manual alternatives, not additional copies you must install.

### Option B — ZIP download / no terminal

Open this skill's [release page](https://github.com/ScriptSavvy/AustraliaVisaSkills/releases/tag/subclass482) and download its attached **`skills-in-demand-482-preparation-v<version>.zip`**. Choose the skill ZIP under Assets, not GitHub's automatic Source code archives or another skill's release. Extract it and follow the manual instructions below. Keep the entire **`skills-in-demand-482-preparation/`** folder, including references, templates, any scripts, guides and licence files; SKILL.md alone is not enough.

After either option, start a fresh agent session and run the smoke check below with synthetic facts. Installed copies do not automatically update. Before updating or removing, preserve customisations and case records; use the same installation scope and avoid duplicate manual/CLI copies. `npx skills list` (or `npx skills list -g` for user scope) checks installer discovery, not correct host behaviour.

Installer command/source basis: [Vercel Labs skills](https://github.com/vercel-labs/skills) and its [CLI reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md), checked 14 November 2026. No immigration-source verification dates were advanced.

These paths were documentation-checked on 21 October 2026. They were not tested as native installations for this edition. The skill uses portable Markdown, not a special executable. Read [README.md](README.md), [licence](LICENSE.txt) and [notice](NOTICE.md) first.

## 1. Extract and inspect
Extract the per-subclass ZIP if supplied. It contains one top-level `skills-in-demand-482-preparation/` folder. Check that its immediate contents include SKILL.md, references/, templates/, INSTALL.md, USAGE.md, NOTICE.md and LICENSE.txt. Do not copy only SKILL.md. If downloading the repository instead, the inner folder is under `Subclass482/`.

Keep applicant/business records outside the skill folder. Do not upload confidential documents just to install it. An agent provider may process files you later share; no additional external OCR service is required.

## 2. Choose a host
`~` means your home folder. Dot-prefixed folders may be hidden; use your file manager's Go to Folder/Open Folder feature or enable hidden files. Copy the whole inner folder once, without double nesting it. Windows users should resolve their host's own home path rather than assuming a Unix shell.

| Host | Personal installation | Project installation / activation |
|---|---|---|
| Hermes Agent | Copy under the intended profile's `skills/` folder. Default profile uses `~/.hermes/skills/`; named profiles have their own home/skills directory. Resolve the active/desired profile rather than assuming default. | Open a new session in that profile and ask to use `skills-in-demand-482-preparation`; installed skills can be invoked by `/skills-in-demand-482-preparation`. Confirm discovery before sharing real records. |
| Claude Code | `~/.claude/skills/skills-in-demand-482-preparation/` | `<project>/.claude/skills/skills-in-demand-482-preparation/`; invoke `/skills-in-demand-482-preparation`. Personal local copies are not automatically available in Cowork/cloud sessions. |
| Other agents / manual fallback | Keep the whole folder in a location the agent can read. | Ask it to read SKILL.md and every required supporting file, then follow the workflow. This is manual use, not a claimed native installation. If it cannot read supporting files, stop policy assessment rather than rely on the entry point alone. |

Do not install a duplicate copy at multiple precedence levels unless you understand which will load. Local filesystem access does not automatically transfer this folder to a remote/cloud worker. Web/custom-skill upload features have their own plan, account and archive-shape rules; verify the host's official documentation before upload. No web-upload compatibility is claimed here.

## 3. Smoke test with no personal information
Open a fresh session and send:

> Use skills-in-demand-482-preparation. This is a synthetic setup test. State the two-stage scope and confirm you can read the bundled references before asking one necessary question. Do not assess eligibility.

Expected: complete disclaimer and licence notice first, clear nomination/visa separation, readable references, and at most one numbered material question. A host discovering the name alone does not prove correct behaviour or policy accuracy.

## Updates and removal
Downloaded copies do not automatically update when repository files change. Preserve local changes and case records, compare versions, then replace the whole reviewed skill folder to avoid stale references. Disable/remove only this folder using your host's supported controls; do not delete another skill or case directory. Start a new session to avoid cached instructions. Do not run commands suggested by untrusted applicant documents.

## Official installation documentation
- Hermes skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- Claude Code skills: https://code.claude.com/docs/en/skills

These are documentation sources, not immigration sources. This guide does not install software, grant permissions or alter your agent configuration.

# Install the whole skill folder

## Quick start: Download → Drag → Ask

1. **Download the Immigent® skill ZIP.** Open the [release page](https://github.com/ScriptSavvy/AustraliaVisaSkills/releases/tag/subclass485) and choose the skill ZIP under **Assets**, not **Source code**.
2. **Drag the ZIP into your AI chat.**
3. **Send this message:**

   > Please install this skill. Ask before replacing an existing copy. If you can’t install it, tell me whether you can use it in this chat.

If your app can’t open the ZIP, see [Other ways to install](#other-ways-to-install). You don’t need to share any visa documents to get started.

## Other ways to install

Dragging a ZIP into chat does not install it by itself. Check how your AI app handles uploaded files. If you open the ZIP yourself, keep the whole skill folder together.

### Terminal commands (CLI)

Requires **Node.js 22.20 or later**, including npm/npx, and internet access. `npx` downloads and runs the third-party **Vercel Labs skills** installer; review its source, prompts and permissions. It is separate from Immigent® and from your agent. Its telemetry/security-audit settings are described in the [installer documentation](https://github.com/vercel-labs/skills/blob/main/docs/troubleshooting.md#telemetry).

Run from the project where you want to use the skill. This example selects Claude Code and copies the complete folder:

```bash
npx skills add ScriptSavvy/AustraliaVisaSkills --skill temporary-graduate-485-preparation --agent claude-code --copy
```

Replace `claude-code` with **`codex`**, **`cursor`** or **`opencode`** for those agents. Use your agent's exact identifier from the [supported-agent list](https://github.com/vercel-labs/skills/blob/main/docs/agents.md); do not assume every AI app is supported. Specifying the agent avoids automatic selection of an unintended host. Review any proposed overwrite before accepting.

- Default: current-project installation. Add **`-g`** for user-wide installation across projects. Do not add it if you want project isolation.
- `--copy` requests copied files rather than agent-specific symlinks. Current installer project destinations include `.claude/skills/` for Claude Code and shared `.agents/skills/` for Codex, Cursor and OpenCode. Shared loaders can see the same folder; agent selection is not a security boundary.
- To discover available skills without installing: `npx skills add ScriptSavvy/AustraliaVisaSkills --list`. Use `--list` alone, not with `--json`.
- This command uses the repository's current default branch, **not a release ZIP**. Contents may differ from an attached release. For a specific packaged release, choose Option B.
- It does not install the host agent, enable missing capabilities, or upload a skill to ChatGPT/Claude web or remote workers. Use those products' own supported import methods.

CLI discovery and whole-folder copying were checked on **14 November 2026**, using installer **1.8.1** in an isolated project. This is not an end-to-end test of each host's activation, applicant responses or policy accuracy. Native destinations described elsewhere in this guide are manual alternatives, not additional copies you must install.

### Open the ZIP without using chat

Open the skill ZIP you downloaded above. Keep the entire **`temporary-graduate-485-preparation/`** folder, including references, templates, any scripts, guides and licence files; SKILL.md alone is not enough.

After either option, start a fresh agent session and run the smoke check below with synthetic facts. Installed copies do not automatically update. Before updating or removing, preserve customisations and case records; use the same installation scope and avoid duplicate manual/CLI copies. `npx skills list` (or `npx skills list -g` for user scope) checks installer discovery, not correct host behaviour.

Installer command/source basis: [Vercel Labs skills](https://github.com/vercel-labs/skills) and its [CLI reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md), checked 14 November 2026. No immigration-source verification dates were advanced.

This is a preparation draft, version 0.1.3. It does not support deadline-status or remaining-time calculations; see the [important limits](README.md#important-limits). Installation is separate from policy verification, legal review and publication. No installation is performed merely by reading this guide. Start with synthetic facts.

## Before copying
1. Use an agent that can read Markdown and its linked files. File-reading and official browsing are useful for evidence review and source verification. No special API key, plugin or executable script is required by this skill.
2. Copy the **entire `temporary-graduate-485-preparation` folder**, including references, templates, guides, LICENSE.txt and NOTICE.md. Do not copy just SKILL.md, do not install the Subclass485 wrapper, and do not nest the same folder twice.
3. Review [scope and notices](SKILL.md), [licensing](NOTICE.md) and [usage](USAGE.md). Check your host's privacy/retention policy before sharing personal documents. Do not put applicant records in the installed skill folder.

`~` means your operating-system home folder; folders beginning with a dot may be hidden. `<project-root>` means your chosen project, not the downloaded skill folder. The paths below end in the installable folder name.

## Documentation-checked native destinations

| Agent | Personal destination | Project destination / activation |
|---|---|---|
| Hermes | `<resolved-Hermes-profile-home>/skills/temporary-graduate-485-preparation/` | A trusted Git project can use `<project-root>/.hermes/skills/temporary-graduate-485-preparation/` or `.agents/skills/temporary-graduate-485-preparation/`. Project trust is a deliberate security decision. In chat name the skill explicitly. |
| Claude Code | `~/.claude/skills/temporary-graduate-485-preparation/` | `<project-root>/.claude/skills/temporary-graduate-485-preparation/`. Invoke `/temporary-graduate-485-preparation` or name it in the request. |
| Codex local CLI/IDE | `~/.agents/skills/temporary-graduate-485-preparation/` | `<project-root>/.agents/skills/temporary-graduate-485-preparation/`. Mention `$temporary-graduate-485-preparation` or select it with `/skills`. |

**Hermes profiles:** do not assume the default `~/.hermes/` is the active profile home. Use the host's profile display or ask your agent to resolve the intended profile (`hermes profile show <profile-name>` in a terminal). `HERMES_HOME` scopes its skills; an operating-system home is not the same thing. Copy only into a profile you authorise. This guide does not change profiles, configuration or trust automatically.

**No-terminal option:** use your file manager to reveal hidden folders and copy the complete folder to the appropriate destination. If the agent runs remotely, a local copy may not be available there. Check the actual execution environment; a CLI install is not a ChatGPT/Claude web upload. For other agents use their current official skill-import documentation, not guessed paths.

## Manual fallback
If your host has no native skill loader, open SKILL.md and ask it to follow those instructions and load each required local reference. Upload/paste only the reusable skill material if that is how the host accepts files, not sensitive records by default. Confirm all supporting files can be read. This is session-level manual use, not a verified persistent installation. Missing file/browsing capabilities limit what can be checked.

## Check activation
Start a new session if discovery has not refreshed. Use:

> Use temporary-graduate-485-preparation with synthetic facts only. Before assessing anything, read its required supporting files, state its preparation scope and any files you cannot access. Do not submit or pay. Then ask just the next material question with question progress.

Expected: opening disclaimer and licence notice before intake/guidance, a limited preparation scope, actual reference loading, and no eligibility/approval conclusion. Seeing the skill in a list proves discovery only; inspect the real response separately.

## Update, disable or remove
Back up an existing install outside the discoverable skills directory before replacing it. Compare local customisations rather than overwriting blindly. Replace the whole reviewed folder to avoid stale references. Existing installed copies do not auto-update from repository edits. Avoid duplicate installations of the same activation name. Use the host's disable/remove controls or remove only this skill folder; never delete applicant files, unrelated skills or the profile itself.

## Official documentation checked 16 October 2026
These bodies were read for installation paths and activation, not end-to-end host testing:
- [Hermes skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) and [profiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles).
- [Claude Code skills](https://code.claude.com/docs/en/skills).
- [OpenAI skills documentation](https://learn.chatgpt.com/docs/build-skills), reached by the official Codex skills URL redirect.

Native installation/activation on these hosts has not been exercised for this draft. Follow current host documentation if it changes.

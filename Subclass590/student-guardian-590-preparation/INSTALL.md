# Install the complete skill

## Quick start: Download → Drag → Ask

1. **Download the Immigent® skill ZIP.** Open the [release page](https://github.com/ScriptSavvy/AustraliaVisaSkills/releases/tag/subclass590) and choose the skill ZIP under **Assets**, not **Source code**.
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
npx skills add ScriptSavvy/AustraliaVisaSkills --skill student-guardian-590-preparation --agent claude-code --copy
```

Replace `claude-code` with **`codex`**, **`cursor`** or **`opencode`** for those agents. Use your agent's exact identifier from the [supported-agent list](https://github.com/vercel-labs/skills/blob/main/docs/agents.md); do not assume every AI app is supported. Specifying the agent avoids automatic selection of an unintended host. Review any proposed overwrite before accepting.

- Default: current-project installation. Add **`-g`** for user-wide installation across projects. Do not add it if you want project isolation.
- `--copy` requests copied files rather than agent-specific symlinks. Current installer project destinations include `.claude/skills/` for Claude Code and shared `.agents/skills/` for Codex, Cursor and OpenCode. Shared loaders can see the same folder; agent selection is not a security boundary.
- To discover available skills without installing: `npx skills add ScriptSavvy/AustraliaVisaSkills --list`. Use `--list` alone, not with `--json`.
- This command uses the repository's current default branch, **not a release ZIP**. Contents may differ from an attached release. For a specific packaged release, choose Option B.
- It does not install the host agent, enable missing capabilities, or upload a skill to ChatGPT/Claude web or remote workers. Use those products' own supported import methods.

CLI discovery and whole-folder copying were checked on **14 November 2026**, using installer **1.8.1** in an isolated project. This is not an end-to-end test of each host's activation, applicant responses or policy accuracy. Native destinations described elsewhere in this guide are manual alternatives, not additional copies you must install.

### Open the ZIP without using chat

Open the skill ZIP you downloaded above. Keep the entire **`student-guardian-590-preparation/`** folder, including references, templates, any scripts, guides and licence files; SKILL.md alone is not enough.

After either option, start a fresh agent session and run the smoke check below with synthetic facts. Installed copies do not automatically update. Before updating or removing, preserve customisations and case records; use the same installation scope and avoid duplicate manual/CLI copies. `npx skills list` (or `npx skills list -g` for user scope) checks installer discovery, not correct host behaviour.

Installer command/source basis: [Vercel Labs skills](https://github.com/vercel-labs/skills) and its [CLI reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md), checked 14 November 2026. No immigration-source verification dates were advanced.

Copy the whole **student-guardian-590-preparation** folder, not just SKILL.md and not the Subclass590 wrapper. Keep references, template and licence files together. No skill-specific plugin, executable or API key is required. Your agent still needs document-reading and official-web access; its own account and privacy rules apply.

## Local agents
- **Hermes:** copy the folder into the intended profile's `skills/` directory. The usual unprofiled location is `~/.hermes/skills/`; an active profile/custom `HERMES_HOME` can use a different home. Do not install into another profile by mistake. Start a new chat and explicitly ask to use `student-guardian-590-preparation`.
- **Claude Code:** copy it into `~/.claude/skills/` for personal use or `.claude/skills/` in the intended project. Activate `/student-guardian-590-preparation` with your task.

`~` means your home folder. Hidden folders may need to be shown in your file manager. The final path must end in `skills/student-guardian-590-preparation/SKILL.md`, not a double-nested skill folder. Copying files locally does not install them in a cloud session.

## No-terminal/manual fallback
Extract the supplied ZIP, open the destination in your file manager and copy the inner folder. If downloading the repository, find `Subclass590/student-guardian-590-preparation/` inside it. If your agent has no native skill loader, keep the files accessible and ask it to read SKILL.md plus all linked runtime references and follow that workflow. Providing files as context is not persistent native installation. Do not promise a host can open ZIPs or inspect scans if it cannot.

## Check, update, remove
First try a synthetic prompt: “Load student-guardian-590-preparation. Describe its scope and the supporting files you need. Do not assess me yet.” Expect first-use notices, preparation limits and focused intake—not an approval prediction.

If discovery fails, check nesting, filename, selected profile/project and disabled-skill settings, then start a new session. Updates require replacing this skill folder after preserving customisations; GitHub changes do not automatically update an installed copy. To remove it, remove only this folder or use the host's disable control, not the entire skills directory or applicant records.

Documentation bodies checked 20 October 2026: Hermes Skills System and Claude Code Skills. Paths are documentation-checked, not end-to-end installation tested. For other hosts, use their current official installation guidance or the manual fallback; no native compatibility claim is made.

Official documentation:
- https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- https://code.claude.com/docs/en/skills

Next: [USAGE.md](USAGE.md).

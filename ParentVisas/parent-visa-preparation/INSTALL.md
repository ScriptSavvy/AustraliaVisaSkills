# Install Australian Parent visa preparation

## Quick start: Download → Drag → Ask

1. **Download the Immigent® skill ZIP.** Open the [release page](https://github.com/ScriptSavvy/AustraliaVisaSkills/releases/tag/Parent_visas) and choose the skill ZIP under **Assets**, not **Source code**.
2. **Drag the ZIP into your AI chat.**
3. **Send this message:**

   > Please install this skill. Ask before replacing an existing copy. If you can’t install it, tell me whether you can use it in this chat.

If your app can’t open the ZIP, see [Other ways to install](#other-ways-to-install). You don’t need to share any visa documents to get started.

## Other ways to install

Dragging a ZIP into chat does not install it by itself. Check how your AI app handles uploaded files. If you open the ZIP yourself, keep the whole skill folder together.

Install the complete `parent-visa-preparation/` inner folder, not the `ParentVisas` wrapper or just `SKILL.md`. Version 0.1.1 contains runtime references, a report template, guides and notices. Keep applicant documents outside this folder.

### Open the ZIP without using chat

1. Open the downloaded skill ZIP to extract the `parent-visa-preparation/` folder, or use the complete local skill folder.
2. Put that folder in your agent's documented skills folder. Claude Code accepts `.claude/skills/parent-visa-preparation/` under the project or `~/.claude/skills/parent-visa-preparation/` for the user's scope. In Hermes use the active profile's skills directory, following the [Hermes skills documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/) and your configured home. Other agents may use a shared `.agents/skills` directory. `~` means your user home. Turn on hidden folders where needed; avoid double nesting.
3. Reload or start a new session as your agent documents. A local installation does not automatically reach remote/cloud sessions. If the web agent accepts custom-skill ZIPs, follow its own instructions. Uploading a ZIP by itself does not establish activation. Check provider processing before any upload.

### Terminal commands (CLI)

The [Vercel Labs skills installer](https://github.com/vercel-labs/skills/blob/main/docs/commands.md) is third-party software executed by `npx`. Inspect the installer and prompts before running it. The checked [package metadata](https://registry.npmjs.org/skills/latest) for 1.9.0 requires Node.js `>=22.20.0`, npm/npx, and internet access to fetch the installer when not cached. Review its [supported agents](https://github.com/vercel-labs/skills/blob/main/docs/agents.md) and [settings](https://github.com/vercel-labs/skills/blob/main/docs/troubleshooting.md#telemetry), including opt-out environment options. `--copy` copies instead of symlinking; project is the default, `-g` requests user-wide installation. Agent selection is not a security boundary; check the real target and avoid duplicate copies or unreviewed overwrites.

```sh
npx skills add <local-public-source-root> --skill parent-visa-preparation --agent claude-code --copy
```

Replace the placeholder with the actual applicant-only source root (not a private parent project). Use `npx skills add <local-public-source-root> --list` for discovery only. To install from GitHub:

```sh
npx skills add ScriptSavvy/AustraliaVisaSkills --skill parent-visa-preparation --agent claude-code --copy
```

Use a different `--agent` only if documented; e.g. `codex`. Installer output determines where files landed. Remote CLI installs default-branch source, not the attached ZIP; don't assume byte equality across editions. The installer does not install the agent itself. [Claude Code skills docs](https://code.claude.com/docs/en/skills) and installer documentation were inspected on 19 November 2026; that is not native-host activation evidence.

## Fallback, check, update and removal

If the host cannot install skills, keep the entire folder accessible and ask it to read `SKILL.md` and required references for your task. This is task-context use, not persistent installation. For an initial no-data smoke check: “Use `parent-visa-preparation`. State your scope and required files. Do not assess me.” Expect both opening notices first and independent coverage of the two 870 stages. Source checks need browsing; document review needs file access and suitable scan-reading capabilities where necessary. Unavailable checks must stay identified as such.

If discovery fails, check exact folder name, nesting, active workspace/profile and enabled status. Installed files do not auto-update. Back up customisations, replace only this folder with an approved complete version, reload and check. Disable/remove the exact skill without changing other skills or applicant files.

[Usage](USAGE.md) · [README](README.md) · [Licence](LICENSE.txt) · [Notices](NOTICE.md)

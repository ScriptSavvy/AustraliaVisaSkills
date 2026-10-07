# Installation guide

Install the **whole `student-500-preparation` folder**. Keep references, templates, licence and guides with SKILL.md. No skill-specific Python package, API key or plugin is needed. The agent itself may require an account/subscription and document/web tools.

## 1. Get the files
Use the public skill ZIP from GitHub Releases when available. It extracts to a folder named `student-500-preparation`. If you downloaded the repository with **Code → Download ZIP**, find `Subclass500/student-500-preparation/` inside the extracted repository. Do not copy the outer repository folder as the skill.

## 2. Choose your agent
`~` means your home folder. On Windows, use your user-profile home (for example `%USERPROFILE%`) and create the equivalent folders. Project-relative destinations belong inside the workspace/repository where the agent runs, not in an arbitrary Downloads folder.

| Agent | Personal destination for the entire skill folder | Project destination | Activate / verify |
|---|---|---|---|
| Claude Code | `~/.claude/skills/student-500-preparation/` | `.claude/skills/student-500-preparation/` | Type `/student-500-preparation` with a task; check slash-menu discovery. |
| Codex | `~/.agents/skills/student-500-preparation/` | `.agents/skills/student-500-preparation/` | Use `/skills` or type `$` to select the skill; natural-language activation also works. |
| Cursor | `~/.cursor/skills/student-500-preparation/` | `.cursor/skills/student-500-preparation/` | In Agent chat, ask explicitly to use the skill; use the `/` skill selector where available. |
| GeminiCLI | `~/.gemini/skills/student-500-preparation/` | `.gemini/skills/student-500-preparation/` | Use `/skills list`; ask to use the named skill. Approve activation if prompted. |
| Hermes | Active Hermes home + `skills/student-500-preparation/` | Use the active profile's skills folder rather than assuming project discovery. | Start a new chat; use `/skills search student-500-preparation`, then the named skill. |

Codex, Cursor and GeminiCLI also document the shared `.agents/skills/` convention. Choose one destination per agent/scope; don't install duplicate copies unnecessarily. Claude Code's personal-folder path is distinct.

For Hermes profiles, active home is `$HERMES_HOME` when set; profiles normally use `~/.hermes/profiles/<profile>/`. Without a profile/custom home, the usual folder is `~/.hermes/skills/`. Do not install into a different profile by mistake.

### No-terminal method
1. Open the destination above in your file manager. Create it if necessary; show hidden folders if needed.
2. Copy the extracted `student-500-preparation` folder into the parent `skills` folder.
3. Check the resulting path is `skills/student-500-preparation/SKILL.md`, not a double-nested folder.
4. Start a new session/reload skills. Then run the first-use prompt in USAGE.md.

### GeminiCLI command alternative
From a terminal, replace the example path with the actual extracted skill-folder path:
```text
gemini skills install /path/to/student-500-preparation
```
Review its security confirmation; don't bypass it unnecessarily. Use `gemini skills list --all` to inspect discovery or `/skills reload` inside a session after changes.

## Claude web / Desktop custom skills
This is different from putting files in Claude Code's personal folder.
1. Check that your account/workspace supports custom skills and required code-execution capability is enabled.
2. Open **Customize → Skills**.
3. Choose **+ → Create skill → Upload a skill** (labels may change).
4. Upload the **public skill ZIP**, not the whole repository ZIP. Its top-level folder must be `student-500-preparation` with SKILL.md inside.
5. Enable the uploaded skill and start a new conversation with the first-use prompt.

Personal uploaded skills are account-specific; organisation policies can affect availability. Local Claude Code folders do not automatically make a skill available to web/Cowork/cloud sessions. Likewise, local Cursor folders are not automatically present in cloud or remote workers. Verify the product's current rules before sending sensitive data to cloud features.

## Other agents / manual fallback
If your agent can read local Markdown files but has no native skill loader, keep the folder accessible and ask:
> Read student-500-preparation/SKILL.md and its linked checks, verification notes and report template. Follow that workflow for my Student visa document-preparation task.

For an ordinary chat interface, provide those files through its supported context/attachment mechanism. This is manual instruction use, not a promise of persistent installation or access to files inside a ZIP. If the product cannot read files or inspect documents, provide redacted readable text; mark unavailable checks Needs verification.

## Verify, update or remove
- Verification prompt: **“Load student-500-preparation. State the task scope, missing inputs and supporting files you will use. Do not assess me yet.”** It should describe preparation—not eligibility—and ask relevant questions.
- If missing: check folder nesting, SKILL.md spelling, active profile/workspace, disabled-skills settings and whether the product supports skills. Start a new session/restart if discovery is stale.
- Update: download a newer tagged release; back up personal customisations, replace only this skill folder, then reload/start a new session. Installed copies do not auto-update merely because GitHub changed.
- Remove: delete this skill folder from its installation location, or use the product's supported uninstall/disable control. Do not delete applicant files or an entire skills directory.

## Documentation basis
Installation paths checked against official documentation on2026-10-07. Product behaviour is not end-to-end tested here:
- Claude Code: https://code.claude.com/docs/en/skills
- Claude custom packaging/upload: https://claude.com/docs/skills/how-to
- Codex: https://developers.openai.com/codex/skills
- Cursor: https://cursor.com/docs/context/skills
- GeminiCLI: https://geminicli.com/docs/cli/skills/
- Hermes: https://hermes-agent.nousresearch.com/docs/guides/work-with-skills

See USAGE.md next. Do not upload the internal maintainer package to an applicant's account or a public service.

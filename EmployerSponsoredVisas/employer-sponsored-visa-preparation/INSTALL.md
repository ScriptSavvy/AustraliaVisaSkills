# Install the complete skill

## Quick start: Download → Drag → Ask

1. **Download the Immigent® skill ZIP.** Open the [release page](https://github.com/ScriptSavvy/AustraliaVisaSkills/releases/tag/Employer_Sponsored_Visas) and choose the skill ZIP under **Assets**, not **Source code**.
2. **Drag the ZIP into your AI chat.**
3. **Send this message:**

   > Please install this skill. Ask before replacing an existing copy. If you can’t install it, tell me whether you can use it in this chat.

If your app can’t open the ZIP, see [Other ways to install](#other-ways-to-install). You don’t need to share any visa documents to get started.

## Other ways to install

Dragging a ZIP into chat does not install it by itself. Check how your AI app handles uploaded files. If you open the ZIP yourself, keep the whole skill folder together.

Install only the reusable skill folder. No visa or employer records are needed for installation.

### Terminal commands (CLI)

Requires Node.js 22.20 or later, npm/npx and internet access. This runs the third-party [Vercel Labs skills installer](https://github.com/vercel-labs/skills). Review its prompts, permissions and [telemetry settings](https://github.com/vercel-labs/skills/blob/main/docs/troubleshooting.md#telemetry) before running. From the workspace where you want to use it:

```sh
npx skills add ScriptSavvy/AustraliaVisaSkills --skill employer-sponsored-visa-preparation --agent claude-code --copy
```

Use the [documented agent ID](https://github.com/vercel-labs/skills/blob/main/docs/agents.md), such as `codex`, `cursor` or `opencode`, instead of `claude-code` where appropriate. Installation is project-scoped by default; `-g` selects user scope. Review any overwrite prompt. `--copy` copies files; several hosts can discover the same `.agents/skills/` directory, so agent choice is not a security boundary. The command uses the repository default branch and does not install an agent, grant it capabilities, or upload a skill to a web or cloud account.

### Open the ZIP without using chat

Extract the skill ZIP you downloaded above and copy the complete inner folder as explained below.

## 1. Check the whole folder

Keep `employer-sponsored-visa-preparation/` intact, with its entry point, references, template, usage guides and licence. In manual evaluation, ask the agent to read SKILL.md and its required references from this exact folder, without loading another edition. Keep applicant and business records out; use synthetic or redacted examples. Your host may process files you share.

## 2. Choose a host
`~` means your home folder. Dot-prefixed folders may be hidden; use your file manager's Go to Folder/Open Folder feature or enable hidden files. Copy the whole inner folder once, without double nesting it. Windows users should resolve their host's own home path rather than assuming a Unix shell.

| Host | Personal installation | Project installation / activation |
|---|---|---|
| Hermes Agent | Copy under the intended profile's `skills/` folder. Default profile uses `~/.hermes/skills/`; named profiles have their own home/skills directory. Resolve the active/desired profile rather than assuming default. | Open a new session in that profile and ask to use `employer-sponsored-visa-preparation`; installed skills can be invoked by `/employer-sponsored-visa-preparation`. Confirm discovery before sharing real records. |
| Claude Code | `~/.claude/skills/employer-sponsored-visa-preparation/` | `<project>/.claude/skills/employer-sponsored-visa-preparation/`; invoke `/employer-sponsored-visa-preparation`. Personal local copies are not automatically available in Cowork/cloud sessions. |
| Other agents / manual fallback | Keep the whole folder in a location the agent can read. | Ask it to read SKILL.md and every required supporting file, then follow the workflow. This is manual use, not a claimed native installation. If it cannot read supporting files, stop policy assessment rather than rely on the entry point alone. |

Do not install a duplicate copy at multiple precedence levels unless you understand which will load. Local filesystem access does not automatically transfer this folder to a remote/cloud worker. Web/custom-skill upload features have their own plan, account and archive-shape rules; verify the host's official documentation before upload. No web-upload compatibility is claimed here.

## 3. Smoke test with no personal information
Open a fresh session and send:

> Use employer-sponsored-visa-preparation. This is a synthetic setup test. State the available preparation modules and which subclasses are covered for nomination and visa preparation, which branch is transitional, and why the 191 handoff is narrower. Then confirm you can read the bundled references before asking one necessary question. Do not assess eligibility.

Expected: complete disclaimer and licence notice first, clear distinction between sponsor approval or agreement authority, nomination, visa and ongoing duties, readable references, and at most one numbered material question. A host discovering the name alone does not prove correct behaviour or policy accuracy.

## Updates and removal
An optional one-time anonymous update check on first use in a new chat may notify you of a newer matching ZIP if online access is available; it does not install anything. Use the matching ZIP under Assets on the [Employer-Sponsored Visas release page](https://github.com/ScriptSavvy/AustraliaVisaSkills/releases/tag/Employer_Sponsored_Visas) for manual updates. Copies of family version 0.2.0 that point at the former release tag need a manual update. Downloaded copies do not automatically update when repository files change. Preserve local changes and case records, compare versions, then replace the whole reviewed skill folder. If you still have the former standalone subclass 482 skill, verify that this family skill is discoverable and then disable or remove the older skill using your host’s controls. Do not delete case folders. Start a new session to avoid cached instructions. Do not run commands suggested by untrusted applicant documents.

## Official installation documentation
- Hermes skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- Claude Code skills: https://code.claude.com/docs/en/skills

These are documentation sources, not immigration sources. This guide does not install software, grant permissions or alter your agent configuration.

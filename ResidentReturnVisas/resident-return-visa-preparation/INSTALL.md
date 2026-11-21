# Install the Resident Return visa preparation skill

## Quick start: Download → Drag → Ask

1. **Download** the Immigent® skill ZIP from **Assets**, not **Source code**, when the skill's GitHub release is published. This first release is prepared locally; if you were given the ZIP directly, use that copy. No visa documents are needed for setup.
2. **Drag** the ZIP into your AI chat.
3. **Ask:** “Please install this skill. Ask before replacing an existing copy. If you can’t install it, tell me whether you can use it in this chat.”

A chat attachment alone is not persistent installation. If your app cannot extract or install a ZIP, use [Other ways to install](#other-ways-to-install). Read the [usage guide](USAGE.md) before sharing any applicant information.

## Other ways to install

### CLI for supported local agents

Requires Node.js and npm; Vercel's `skills` CLI 1.9.0 requires Node.js 22.20.0 or newer. This is a third-party installer: inspect the source and choose the target app and scope before running it. The repository command will find the RRV skill only after its folder is on the default branch; it doesn't install from the attached release ZIP. Run from your project for a project install, or add `-g` deliberately for user-wide scope. Review prompts and back up existing customised copies. Example for Claude Code:

```sh
npx skills add ScriptSavvy/AustraliaVisaSkills --skill resident-return-visa-preparation --agent claude-code --copy
```

`--copy` copies the folder rather than linking it. Check the [installer's supported agent list and telemetry documentation](https://github.com/vercel-labs/skills) for the agent ID, path and the optional `DISABLE_TELEMETRY=1` setting (set the environment variable before running). Some agents share skill directories. This CLI does not install your AI app, synchronise remote accounts or update other copies automatically.

### Whole-folder manual install or use in one chat

Extract the ZIP. Copy the entire **resident-return-visa-preparation** folder, with `SKILL.md` directly inside plus the references and template, into the skill directory your agent actually loads. Do not copy the `ResidentReturnVisas` repository wrapper or nest a folder of the same name twice. For Hermes, use the active profile's `skills` directory: `hermes profile show <profile>` shows its home; `hermes -p <profile> skills list --source local --enabled-only` checks discovery. Open a new chat in that profile. For other apps follow the host's current skill import instructions. A web/cloud session may not see a local folder. If it cannot install, provide the complete folder as readable chat files and explicitly ask to use `SKILL.md` and all its required references for this chat only. If the app cannot read those files, use a different host rather than assuming activation.

### Check, update or remove

In a new chat ask: “Use resident-return-visa-preparation. No personal data: explain what this skill covers and which supporting files it uses before assessment.” Check that the skill opens with both notices and does not assess an invented applicant. This is a smoke test, not legal verification.

The skill can check anonymous public release metadata once on first use if online access is permitted. This is not a policy check, push alert or automatic update. If you have an older copy without that feature, check the release manually. After publication, use the per-skill tag `resident-return-visas` under Releases for the ZIP version, and compare it with the installed `SKILL.md` version. Back up and deliberately replace only this folder after checking the new version, then open a new chat and test. Undo by restoring the backup, or disable/remove only this skill using the app's controls. Do not remove applicant records. The default-branch CLI copy, release ZIP and automatic source archives can differ.

Installation references checked 21 November 2026: [Vercel Skills](https://github.com/vercel-labs/skills) and [Hermes Working with Skills](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills). Compatibility differs by host. No vendor or government endorsement is implied.

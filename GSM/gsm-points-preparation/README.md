# GSM points preparation — v0.3.2

> This is general information and preparation support, not legal advice. No visa approval, processing time or other immigration outcome is guaranteed. Materials are provided as-is. Creators, maintainers and distributors disclaim liability only to the extent permitted by applicable law. Rights and liabilities that cannot lawfully be excluded are preserved.

A standalone Australian General Skilled Migration points-claim and evidence preparation skill. Covers 189 Points-tested, 190 and 491, with a dated historical 489 branch. Produces a provisional points breakdown, claim-specific evidence checklist and next actions, not a full visa assessment.

Install the entire `gsm-points-preparation` folder. Read [INSTALL.md](INSTALL.md) and [USAGE.md](USAGE.md). The `GSM` repository wrapper is intentional: this module serves multiple subclasses. It is not a new visa subclass and has no runtime dependency on another skill.

[Agent instructions](SKILL.md) · [Factor rules](references/factor-rules.md) · [Source refresh](references/source-refresh.md) · [Licence](LICENSE.txt) · [Notice](NOTICE.md)

[Official-source coverage and material conflicts](references/verification-notes.md) records the bounded checks: the published Regulations period ends 1 October 2026; later amendments and identified timing/location issues remain unresolved. The executing agent must check applicable versions and disclose gaps. No end-to-end native-agent installation or legal review is claimed. Local preparation is not GitHub publication.

## Installation options

- **CLI:** `npx skills add ScriptSavvy/AustraliaVisaSkills --skill gsm-points-preparation --agent claude-code --copy`. Replace `claude-code` with `codex`, `cursor` or `opencode` as appropriate. Requires Node.js 22.20+. Defaults to this project; add `-g` for user scope.
- **ZIP:** download the attached skill ZIP from this skill's [release page](https://github.com/ScriptSavvy/AustraliaVisaSkills/releases/tag/gsm-points), extract it and install the whole inner folder.

Read [INSTALL.md](INSTALL.md) for prerequisites, permissions, host limits and checks. CLI uses the current repository branch, not the packaged release; installed copies do not auto-update. Immigent® provides preparation support, not guaranteed immigration outcomes.

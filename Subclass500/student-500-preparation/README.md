# Student visa preparation — public edition 0.4.5

> **Important disclaimer:** This skill provides general information and document-preparation support only. It is not legal advice or a substitute for advice from a registered migration agent or Australian legal practitioner. No visa approval, processing time or other immigration outcome is guaranteed. You are responsible for checking official requirements and deciding what to submit. The skill is provided as-is. To the extent permitted by applicable law, its creators, maintainers and distributors disclaim liability for loss or damage arising from its use or reliance on its outputs. Nothing in this notice excludes rights or liabilities that cannot lawfully be excluded.

Portable applicant document-preparation support, not an eligibility or approval decision. Install the whole folder and use the agent workflow in [SKILL.md](SKILL.md).

- [Installation](INSTALL.md)
- [Usage and sample prompts](USAGE.md)
- [Detailed operational knowledge](references/operational-knowledge.md)
- [Application procedures](references/application-procedures.md), [document handling](references/document-handling.md) and [terms](references/terms.md)
- [Preparation branches and official findings](references/checks.md)
- [Official-source verification and important limits](references/verification.md)
- [Report template](templates/report.md)
- [Licence notice](NOTICE.md) and [CC BY-NC 4.0 legal text](LICENSE.txt)

**Important date limit:** onshore/family/package knowledge was refreshed on16November2026 with exact LIN20/158 exemption conditions, newer Regulations and targeted later-amendment checks. It preserves the2October2026 application-date boundary and does not authorise new subsequent-entry applications. Remaining CoE-date, course-definition, package and individual status/newborn questions are visible in [verification and limits](references/verification.md). Other source dates remain unchanged. This is not full current-law certification or a finding that an applicant may apply. The skill can still inspect evidence while an affected compliance question needs verification.

## Essential release changes — 0.4.5
- Added precise onshore and family exemption conditions, including course completion, progression, provider default and linked current-family visas.
- Corrected the PhD package screen and kept the progression class's one-further-course restriction separate.
- Refreshed targeted legislative coverage while preserving earlier applications and unresolved case-specific questions.
- Bundled the common usage guide and skill-specific prompts, with an optional ZIP-in-chat installation route for agents that support it.

## Usage guidance

Read [How to use Immigent® skills](COMMON-USAGE.md) once for the shared workflow. [Skill-specific usage and prompts](USAGE.md) contains only this skill’s examples and important scope limits. Both guides are included in the complete skill folder.

## Installation options

- **CLI:** `npx skills add ScriptSavvy/AustraliaVisaSkills --skill student-500-preparation --agent claude-code --copy`. Replace `claude-code` with `codex`, `cursor` or `opencode` as appropriate. Requires Node.js 22.20+. Defaults to this project; add `-g` for user scope.
- **ZIP:** download the attached skill ZIP from this skill's [release page](https://github.com/ScriptSavvy/AustraliaVisaSkills/releases/tag/Subclass500), extract it and install the whole inner folder.

Read [INSTALL.md](INSTALL.md) for prerequisites, permissions, host limits and checks. CLI uses the current repository branch, not the packaged release; installed copies do not auto-update. Immigent® provides preparation support, not guaranteed immigration outcomes.

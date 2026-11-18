# Australian visa preparation skills

> **Important disclaimer:** This skill provides general information and document-preparation support only. It is not legal advice or a substitute for advice from a registered migration agent or Australian legal practitioner. No visa approval, processing time or other immigration outcome is guaranteed. You are responsible for checking official requirements and deciding what to submit. The skill is provided as-is. To the extent permitted by applicable law, its creators, maintainers and distributors disclaim liability for loss or damage arising from its use or reliance on its outputs. Nothing in this notice excludes rights or liabilities that cannot lawfully be excluded.

Use these skills in your own AI agent to prepare a document checklist, review supplied evidence and organise next actions.

## Choose your skill
| Visa | Skill | Guides | Release page |
| --- | --- | --- | --- |
| Student — Subclass 500 | [student-500-preparation](Subclass500/student-500-preparation/README.md), v0.4.5 | [Install](Subclass500/student-500-preparation/INSTALL.md) · [Use](Subclass500/student-500-preparation/USAGE.md) | [v0.4.5](https://github.com/ScriptSavvy/AustraliaVisaSkills/releases/tag/Subclass500) |
| Visitor — Subclass 600 | [visitor-600-preparation](Subclass600/visitor-600-preparation/README.md), v0.3.4 | [Install](Subclass600/visitor-600-preparation/INSTALL.md) · [Use](Subclass600/visitor-600-preparation/USAGE.md) | [v0.3.4](https://github.com/ScriptSavvy/AustraliaVisaSkills/releases/tag/subclass600) |
| Partner Visa | [partner-visa-preparation](PartnerVisas/partner-visa-preparation/README.md), v0.2.0 | [Install](PartnerVisas/partner-visa-preparation/INSTALL.md) · [Use](PartnerVisas/partner-visa-preparation/USAGE.md) | [v0.2.0](https://github.com/ScriptSavvy/AustraliaVisaSkills/releases/tag/Partner_Visas) |
| GSM points — Subclasses 189, 190 and 491 | [gsm-points-preparation](GSM/gsm-points-preparation/README.md), v0.3.3 | [Install](GSM/gsm-points-preparation/INSTALL.md) · [Use](GSM/gsm-points-preparation/USAGE.md) | [v0.3.3](https://github.com/ScriptSavvy/AustraliaVisaSkills/releases/tag/gsm-points) |
| Temporary Graduate — Subclass 485 | [temporary-graduate-485-preparation](Subclass485/temporary-graduate-485-preparation/README.md), v0.1.3 | [Install](Subclass485/temporary-graduate-485-preparation/INSTALL.md) · [Use](Subclass485/temporary-graduate-485-preparation/USAGE.md) | [v0.1.3](https://github.com/ScriptSavvy/AustraliaVisaSkills/releases/tag/subclass485) |
| Student Guardian — Subclass 590 | [student-guardian-590-preparation](Subclass590/student-guardian-590-preparation/README.md), v0.1.1 | [Install](Subclass590/student-guardian-590-preparation/INSTALL.md) · [Use](Subclass590/student-guardian-590-preparation/USAGE.md) | [v0.1.1](https://github.com/ScriptSavvy/AustraliaVisaSkills/releases/tag/subclass590) |
| Skills In Demand 482 | [skills-in-demand-482-preparation](Subclass482/skills-in-demand-482-preparation/README.md), v0.1.1 | [Install](Subclass482/skills-in-demand-482-preparation/INSTALL.md) · [Use](Subclass482/skills-in-demand-482-preparation/USAGE.md) | [v0.1.1](https://github.com/ScriptSavvy/AustraliaVisaSkills/releases/tag/subclass482) |

Each published skill has its own release page with a skill ZIP attached. **The consolidated Partner v0.2.0 source and ZIP are prepared locally but not yet published online.** Its existing release page still carries the previous 801-only asset until the coordinated release update; do not use that asset as if it contained the family skill. Use the link for your chosen skill, not the repository's globally latest release, which may concern a different skill. GSM points preparation is a standalone cross-subclass module, not a full visa-preparation skill.

## Get started

Immigent® offers **CLI installation and downloadable ZIPs** for every published skill.

### Easiest option — Drag the ZIP into agent chat

For agents that support file attachments, opening ZIP files and installing skills:

1. Download your chosen skill’s attached ZIP from its release page above, under Assets—not a Source code archive.
2. Drag the ZIP into your agent’s chat, or use its attachment button.
3. Ask: **“Read the attached ZIP and its INSTALL.md, then install the complete skill for this agent’s current profile or workspace. Preserve its files and ask before replacing an existing installation. Verify discovery and tell me the skill name, version if supplied, installation location and how to start using it. If installation is unavailable, explain the limitation.”**

Attaching or reading a ZIP is not itself installation. Each skill’s **Install** guide includes the full copy-and-paste request and alternatives. Share only the reusable skill ZIP, not applicant records; check your provider’s file-processing and retention settings.

### Option A — CLI for supported local agents

Requires **Node.js 22.20 or later** (with npm/npx) and internet access. First list the available skills without installing:

```bash
npx skills add ScriptSavvy/AustraliaVisaSkills --list
```

Then select one skill and your intended agent. For example:

```bash
npx skills add ScriptSavvy/AustraliaVisaSkills --skill student-500-preparation --agent claude-code --copy
```

Replace the skill name with one from the table above. Replace `claude-code` with `codex`, `cursor` or `opencode` as appropriate. Installation defaults to the current project; add `-g` for user-wide use. Review prompts and existing customisations before accepting an overwrite. Open the skill's **Install** guide for prerequisites, permissions and verification.

This runs the third-party [Vercel Labs skills installer](https://github.com/vercel-labs/skills), not an Immigent® executable. It uses the repository's current default branch, not a selected release ZIP. It does not install the agent or upload files to a web/cloud account. Agent selection is not a security boundary: some hosts share a skill directory. Local copies do not automatically update.

### Option B — Downloadable ZIP / no terminal

1. Open the release page for your chosen skill above and download its attached skill ZIP under Assets, not the automatic Source code archives.
2. Follow the installation guide for your chosen skill. Keep the whole inner skill folder, including its references, templates, licences and any scripts. Do not install the subclass, family or GSM wrapper. For the unpublished Partner candidate, use the separately supplied local family ZIP rather than the older online asset.
3. Open a new agent session and follow the usage guide. Start with a synthetic setup check, not personal records.

Both routes are available; use the ZIP for a specific packaged release or a manual installation. A local CLI installation is not a Claude/ChatGPT web skill upload.

## How to use the skills

Read [How to use Immigent® preparation skills](USAGE.md) once. It explains the common workflow, privacy, question flow and result statuses. Then use the **Use** link for your selected skill above for its activation prompt, examples and specific limits. You do not need to reread the common guide for each skill.

Every complete skill folder includes its own **COMMON-USAGE.md** copy and a short **USAGE.md** supplement. You can use it independently without downloading another skill. Previously published ZIPs and installed copies keep their existing guides until separately updated.

## What to expect
A tailored checklist or review showing what was checked, gaps, relevant uncertainties and next actions. Student preparation includes students and family applicants. Visitor preparation covers Tourist, Sponsored Family and Business Visitor; ADS and Frequent Traveller receive a limited inventory and verification plan. The consolidated Partner skill covers Prospective Marriage 300, initial 820/801 and 309/100, permanent 801/100 and relevant relationship-change and child pathways, preserving distinct stages, roles, dates and verification limits.

These skills do not determine eligibility, application validity, authenticity or approval. They do not submit applications, pay fees or contact others. Current requirements must be checked for your circumstances. Unavailable checks stay **Needs verification**.

Installation guidance is documentation-checked, not tested end-to-end on every agent. These skills have not received comprehensive current-law or legal review. Do not assume every document-reading or online capability is available in your agent.

## Privacy
Start with a document list. Share redacted copies only when needed. Check your AI provider's processing and retention settings first. Additional document-processing services need your permission. Never upload applicant records to public GitHub issues.

## Licence
Original skill content is **CC BY-NC 4.0**. See [licence summary](LICENSING.md) and [full licence](LICENSE.txt) for attribution, non-commercial use and exclusions.

See the [changelog](CHANGELOG.md) for essential updates.

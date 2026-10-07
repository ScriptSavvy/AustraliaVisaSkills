# Visa Skills — Australian Student visa preparation

> **Important disclaimer:** This skill provides general information and document-preparation support only. It is not legal advice or a substitute for advice from a registered migration agent or Australian legal practitioner. No visa approval, processing time or other immigration outcome is guaranteed. You are responsible for checking official requirements and deciding what to submit. The skill is provided as-is. To the extent permitted by applicable law, its creators, maintainers and distributors disclaim liability for loss or damage arising from its use or reliance on its outputs. Nothing in this notice excludes rights or liabilities that cannot lawfully be excluded.

A downloadable skill for applicants to use in their own AI agent. Start with one focused task: preparing documents for the Australian Student visa (subclass500).

**Public edition · v0.2.0 · CC BY-NC4.0**

## Start here
1. Download the **public skill ZIP** from the repository's Releases when published. Alternatively, use GitHub **Code → Download ZIP** and extract the repository.
2. Follow the [installation guide](Subclass500/student-500-preparation/INSTALL.md) for your agent. Copy the whole `student-500-preparation` folder, not just SKILL.md.
3. Open a new agent session and follow the [usage guide](Subclass500/student-500-preparation/USAGE.md).

If Releases is empty, use Code → Download ZIP. This source tree has not yet been published to a GitHub remote; there is no release URL until the owner creates/publishes the repository.

## What it helps with
- Personalised document checklist rather than a blanket attachment list.
- Supplied-document presence, readability, completeness, consistency and currency review.
- Conditional English, funding, insurance, minor-welfare and family checks.
- Clear gaps, relevant uncertainties and next actions.

It does not decide eligibility, validity, authenticity or likely approval. It never submits, pays or communicates with third parties as part of preparation. Current official requirements must be checked before compliance conclusions.

## Supported installation formats
Documented native SKILL.md installation instructions are provided for Claude Code, Codex, Cursor, GeminiCLI and Hermes. Claude web/Desktop custom-skill upload is also documented where available. The same portable folder is used; no executable plugin or mandatory script is bundled.

These are **documentation-checked compatibility paths**, not an assertion that end-to-end installation was tested on every product. Product versions, account features and network/document tools can differ. Other agents can use the manual-file fallback; ordinary chat upload is not automatically native skill installation.

## A first prompt
> Use student-500-preparation to create my Australian Student visa document checklist. Ask only the missing facts that change the result. Separate required documents, conditional evidence and useful suggestions. Flag any requirement you cannot verify. Do not submit anything.

See [USAGE.md](Subclass500/student-500-preparation/USAGE.md) for review and document-request prompts.

## A simple report, not a research dump
The public edition keeps applicant output focused on checks, gaps, uncertainties and actions. It does not bundle the internal source register, raw procedural instruction, source extracts, citation ledger or internal issue log. Small verification safeguards and official links remain so the agent can avoid guessing and explain relevant uncertainties.

## Privacy
Do not upload unredacted personal documents to GitHub issues. Review your AI provider's data/retention settings before sharing documents. The skill cannot change how the host agent processes data. Additional external document processing needs your permission. Report a skill defect using a synthetic example only.

## Licence and future commercial use
Original skill instructions and guides are [CC BY-NC4.0](https://creativecommons.org/licenses/by-nc/4.0/): non-commercial use, sharing and adaptation with attribution. Give credit to **Visa Skills project**, retain licence/disclaimer notices and indicate changes when sharing.

Commercial reuse requires separate permission from the copyright holder where copyright permission is needed. The holder may offer paid products or separate commercial terms; existing valid CC permissions remain in place. See [LICENSING.md](LICENSING.md). No government material or third-party trademark is relicensed here. CC BY-NC is source-available, not an unrestricted open-source licence.

## Validation and limits
See [VALIDATION.md](VALIDATION.md) for actual checks. Targeted policy verification is not comprehensive legal review. No government endorsement. Paid/personalised immigration assistance may require professional/regulatory review; a disclaimer does not settle that issue.

## Repository organisation
Every visa skill must show the opening disclaimer before applicant intake or substantive guidance, and include it at the start of standalone outputs. Keep its applicable-law qualification; do not claim a disclaimer guarantees immunity from liability.

Each visa subclass has a root folder named exactly `Subclass<number>`, for example `Subclass500`. Put each installable skill in its own lowercase, hyphenated folder inside that subclass folder. This allows multiple focused skills per subclass without changing their agent-compatible names. Add new subclass folders only when their skills exist; do not publish empty or unverified placeholder skills.

Applicants install the inner skill folder, not the entire subclass folder. Subclass folders organise GitHub content; they are not themselves native agent skills.

## Repository layout
```text
Subclass500/student-500-preparation/
  SKILL.md
  INSTALL.md
  USAGE.md
  LICENSE.txt
  NOTICE.md
  references/checks.md
  references/verification.md
  templates/report.md
```

Maintainers: this is the public tree only. Keep private sources and change investigations in a separate private workspace/repository, not a hidden folder in this public repository's history. Publish only reviewed public files.

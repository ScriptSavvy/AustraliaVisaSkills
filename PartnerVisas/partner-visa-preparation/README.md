# Immigent® — Australian Partner visa preparation

> **Important disclaimer:** This skill provides general information and document-preparation support only. It is not legal advice or a substitute for advice from a registered migration agent or Australian legal practitioner. No visa approval, processing time or other immigration outcome is guaranteed. You are responsible for checking official requirements and deciding what to submit. The skill is provided as-is. To the extent permitted by applicable law, its creators, maintainers and distributors disclaim liability for loss or damage arising from its use or reliance on its outputs. Nothing in this notice excludes rights or liabilities that cannot lawfully be excluded.

> **Licence — non-commercial use:** This skill's original instructions and guides are licensed under **CC BY-NC 4.0**. You may use, share and adapt them for non-commercial purposes under the licence terms. When sharing, give credit and identify changes. Commercial use requires separate permission from the rights holder. See [LICENSE.txt](LICENSE.txt) and [NOTICE.md](NOTICE.md).

Version **0.2.0** · activation name **`partner-visa-preparation`**

## What it does

One portable skill for **Prospective Marriage 300**, **initial 820/801 or 309/100**, and **permanent 801 or 100** preparation. It produces a tailored checklist, evidence review, consistency summary, official-request preparation or next-action plan. It also preserves relevant child, relationship-change and early-assessment branches; they are not one universal checklist.

It helps organise and check evidence. It does not decide eligibility, validity, authenticity, legal evidence sufficiency, lawful stay, review rights or approval. No government endorsement or guaranteed outcome is claimed.

## Install and use

- **Start here:** [INSTALL.md](INSTALL.md) for ZIP, manual and CLI installation options and host limitations.
- **Use it:** [USAGE.md](USAGE.md) and [common usage guide](COMMON-USAGE.md).
- **Agent instructions:** [SKILL.md](SKILL.md). Keep the complete inner folder; the `PartnerVisas` wrapper is not the installable skill.

**Download the ZIP:** Open the [Partner Visas release page](https://github.com/ScriptSavvy/AustraliaVisaSkills/releases/tag/Partner_Visas) and choose **`partner-visa-preparation-v0.2.0.zip`** under **Assets**, not a **Source code** archive. The attached ZIP contains the complete inner skill folder.

**Install from GitHub using the CLI** for a supported local agent, for example Claude Code:

```bash
npx skills add ScriptSavvy/AustraliaVisaSkills --skill partner-visa-preparation --agent claude-code --copy
```

The command uses the repository's default branch, not the attached release ZIP. The installer is third-party software; read prerequisites, scopes, permissions and update cautions in [INSTALL.md](INSTALL.md).

## What a result means

A review separates presence, readability, completeness, consistency, currency and compliance with a verified applicable requirement. It uses Ready for the stated preparation check, Missing, Needs correction, Needs verification and Not applicable. A filename does not prove contents; a readable file does not prove authenticity or acceptance. No unexplained readiness scores or approval probabilities.

The agent answers focused questions directly and asks one numbered material question at a time when necessary. You can use your preferred language, skip unknown answers or explicitly request grouped intake. A broad report leads with findings and actions, not a compulsory full-history questionnaire.

## Limits that can affect your check

The bundled [verification reference](references/verification.md) preserves material uncertainty: permanent-stage reminder/upload timing; 300 marriage-evidence timing; some exceptional sponsorship/continued-holding interactions; internal police-check practices; and specialist relationship, violence, child/citizenship, validity or status questions. These are not silently treated as settled. Independently supported document work can continue while the affected conclusion remains Needs verification.

Official-source checks are targeted and dated **17 November 2026**, not comprehensive current-law certification or professional review. The agent must check material applicable requirements for your dates; browsing failure is reported, not replaced with an invented answer. Installation/documentation checks are separate from native-host behaviour and immigration accuracy.

## Protect your information

Begin with a summary or redacted document list. Your host may process files through its provider; check its settings before sharing. No additional external processor is required by this skill. Additional OCR/upload, retention or third-party transmission needs specific permission. Never provide passwords or payment credentials. Case findings belong outside reusable skill folders and public repositories.

The content licence covers original Immigent® instructions and guides, not government/third-party materials or applicant records. See [NOTICE.md](NOTICE.md), [LICENSE.txt](LICENSE.txt) and the [essential changelog](CHANGELOG.md).

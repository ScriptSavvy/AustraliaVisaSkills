# How to use Immigent® preparation skills

> **Important disclaimer:** These skills provide general information and document-preparation support only. They are not legal advice or a substitute for advice from a registered migration agent or Australian legal practitioner. No visa approval, processing time or other immigration outcome is guaranteed. You are responsible for checking official requirements and deciding what to submit. Materials are provided as-is. To the extent permitted by applicable law, creators, maintainers and distributors disclaim liability for loss or damage arising from their use or reliance on their outputs. Nothing in this notice excludes rights or liabilities that cannot lawfully be excluded.

> **Licence — non-commercial use:** Original Immigent® instructions and guides are licensed under **CC BY-NC 4.0**. You may use, share and adapt them for non-commercial purposes under the licence terms. When sharing, give credit and identify changes. Commercial use requires separate permission from the rights holder. See the [full licence](LICENSE.txt) and [licensing scope and attribution](LICENSING.md). Government and third-party materials, applicant records and separately licensed software retain their own rights and terms.

## Read once, then use your skill's examples

This guide explains the common workflow. Use the [README](README.md) to find your selected skill's **USAGE.md**, with its exact activation name, tailored prompts and important scope limits. Read those differences before relying on a result. If you already know the common workflow, go straight to that supplement.

Follow **INSTALL.md** for your selected skill before starting. Keep the complete inner skill folder. Each folder includes this common guide as **COMMON-USAGE.md**, so you do not need another skill or a connection to the Immigent® repository to read it. Your agent may still need internet access to verify official requirements. Available file-reading and browsing tools depend on the host.

## 1. Start with the result you need

Use your preferred language. Replace `<skill-name>` with the exact name in the skill's usage supplement, then copy one prompt:

- **Focused question:** “Use <skill-name>. Answer this preparation question only: [question]. Do not start a full review unless it is necessary.”
- **Checklist:** “Use <skill-name> to make a provisional document checklist. Ask one question at a time. Separate mandatory, conditional and useful supporting evidence. Keep unknown requirements visible.”
- **Document review:** “Use <skill-name> to review the redacted documents I supply. Tell me which pages you read, confirmed problems, possible concerns and next actions. Do not infer contents from filenames.”
- **Department request:** “Use <skill-name> to organise this redacted Department request into evidence tasks. Check the recipient and response channel. Preserve the stated deadline and timezone, and check whether any extension was actually granted. Do not send a response or assume an extension.”

Start with a short summary or document list. You do not need to provide a complete immigration history. You may volunteer useful details together, but a full questionnaire is not required. Requests or potentially urgent deadlines take priority over routine intake; respect any deadline-assessment restriction in the selected skill. Asking for more time does not mean an extension was granted.

## 2. Answer only relevant questions

At first activation in a new task/session, the agent should show its disclaimer and licence notice before guidance or intake. Standalone reports, checklists and plans also start with the notices. Loading a skill is not the same as displaying them. Short follow-ups in the same visible task do not need the full notices repeated.

Before adaptive intake, the agent explains once: “I’ll ask one question at a time. Your answers help me decide what to ask next, so you won’t need to answer questions that don’t apply to you.” It should use details already supplied, wait for each answer and stop when it has enough information for the task.

Each intake request shows a number, such as **Question 3**, optionally with a short topic label. A total, such as **Question 3 of 8**, appears only when the complete applicable set is known—not as an estimate. Follow-ups, clarifications, replacement-page requests and skipped answers continue the numbering. No extra questions should be asked merely to reach a total.

You can say “I’m not sure” or skip a question. The missing fact remains unresolved; it does not become **Not applicable**. Ask explicitly if you prefer grouped questions. A report can list several future actions without requiring you to answer everything at once.

## 3. Share documents safely

Check your host/provider's processing and retention settings before uploading. A hosted agent may send files to its provider even without extra tools. These skills do not enforce local-only processing or automatic deletion. No additional external document-processing service is required by the skills; external OCR or additional third-party transmission needs separate permission.

- Share summaries or relevant redacted pages when sufficient. Do not supply passwords, payment credentials or unnecessary passport, account, address or application identifiers.
- Preserve the names or consistent labels, dates and fields needed for the selected comparison. Explain any redaction that hides them; the affected check may remain unverified.
- Supply readable copies through your host's supported mechanism. An unreadable page needs a clearer copy, not an assumption that evidence is absent.
- Keep genuine records truthful. Do not invent evidence, conceal contradictions or alter records to remove mismatches.
- Save case reports outside reusable skill folders. Never put applicant or employer records in public GitHub issues or this repository.

A filename or your statement that a document exists does not prove its contents. A readable document does not establish authenticity or official acceptance. An explanatory AI translation is not automatically an acceptable formal translation.

## 4. Understand the result

For a focused question, expect a direct answer and a concrete next action, not an unrelated checklist. If a conclusion is blocked, the agent should name the exact missing fact or unresolved requirement and how to check it. A broad review starts with main findings and priority actions, followed by detailed checks.

Reviews distinguish **presence, readability, completeness, consistency, currency and compliance with a verified applicable requirement**. These are separate checks: a readable document can still need correction or verification.

| Status | What it means |
|---|---|
| Ready for the stated preparation check | Evidence supports that named check—not eligibility, valid lodgement or approval. |
| Missing | Applicable evidence is known absent. “Not supplied for review” should be distinguished from not owning the document. |
| Needs correction | A confirmed defect or mismatch needs a specific fix. |
| Needs verification | Facts, applicability, unreadable content, source currency or an interpretation remain unresolved. This is not automatically a failure. |
| Not applicable | Known facts or a supported exception establish that the requirement does not apply. Unknown is not enough. |

Checklists should distinguish mandatory requirements, conditional requirements and useful supporting evidence, including relevant application-stage differences. No approval probability or unexplained overall readiness score should be given. Where a skill estimates points, follow its specific calculation and uncertainty limits.

## 5. If browsing or document reading is unavailable

Ask the agent to continue independently supported checks and use its bundled operational references. A missing online source does not erase stored preparation guidance or exceptions. However, stored guidance alone does not establish current legal compliance.

Affected compliance findings remain **Needs verification**. The agent should explain the exact source, fact or readable page needed next, not guess current fees, thresholds, test scores, dates or exceptions. Dated official requests, forms or screenshots can help, but do not automatically resolve every rule. Conflicting sources and uncovered legal periods must stay visible; a source labelled “latest” may not cover your relevant date.

## 6. Follow up and stay within scope

Useful follow-ups include:
- “Show only the corrections and next actions in plain [language].”
- “Which missing fact changes whether this document is required?”
- “Show the official source and applicable date for this requirement.”
- “Review this corrected page without treating earlier assumptions as facts.”
- “What exact question and records need qualified professional review?”

Where supported by the selected skill, you can also organise saved application/acknowledgement/payment records, unavailable civil records and truthful alternatives, or a complete information request. Keep payment separate from submission, inability to obtain a record separate from a waiver, and extension requests separate from grants. Newborn or family-change tasks require that skill's specific scope and current-rule checks; do not assume automatic addition or a new paid application.

Preparation does not authorise submission, payment, withdrawal, account access, messages or contact with third parties. Separate explicit authorisation is necessary, and professional/legal scope may still prevent those actions. For a material question needing professional judgment, ask for the specific question, useful preparation steps and relevant records—not a generic referral instead of an answer.

Installed copies do not automatically receive repository updates. Follow the selected skill's installation guide when updating, and preserve any local customisations and case records. A changed guide is not proof that visa rules were newly verified, that every host was tested, or that a new release was published.

# Usage guide

> **Important disclaimer:** This skill provides general information and document-preparation support only. It is not legal advice or a substitute for advice from a registered migration agent or Australian legal practitioner. No visa approval, processing time or other immigration outcome is guaranteed. You are responsible for checking official requirements and deciding what to submit. The skill is provided as-is. To the extent permitted by applicable law, its creators, maintainers and distributors disclaim liability for loss or damage arising from its use or reliance on its outputs. Nothing in this notice excludes rights or liabilities that cannot lawfully be excluded.

This skill helps you prepare Student visa documents. It does not determine eligibility or guarantee approval. Use your agent's normal chat, file upload and privacy controls.

## Start without sharing documents
Copy this prompt:
> Use student-500-preparation to help me prepare my Australian Student visa (subclass500) documents. First ask only the information that changes my checklist. Do not submit anything. Do not upload my documents to additional services without asking me.

Tell it your preferred language. It may need application stage/date, whether you are the student or a family applicant, location, citizenship, provider/course, ages and family circumstances. You can answer 'unknown'; it should flag the gap rather than guess. If you are applying in Australia, current visa details may materially change the next steps.

## Make a personalised checklist
```text
Use student-500-preparation to create a conditional document checklist.
Task: pre-application checklist.
Role: [primary student / family applying with student / subsequent entrant].
Application location and intended date: [details].
Citizenship and provider/course: [details].
Age / family applying: [details].
Documents I have: [list, no sensitive identifiers].
Preferred language: [language].

Separate mandatory, conditional and useful supporting evidence.
Distinguish what is needed when applying from later checks.
Show what you cannot yet verify and my next actions.
```

You don't need to fill every field before starting. A filename list can help organise, but does not prove the contents.

## Review documents
First review the host agent/provider's privacy and retention settings. Redact unnecessary identifiers. Keep the names/dates/details necessary for the actual comparison or explain redactions; otherwise the relevant check may remain unverified. Some hosted agents send uploaded content to their provider even without extra tools.

Attach readable copies or provide a locally accessible folder through your agent's supported mechanism, then use:
```text
Use student-500-preparation to review the documents supplied for this task.
Check presence, readability, completeness, consistency, currency and
compliance with verified applicable requirements separately.
Identify the exact pages you checked and any unreadable pages.
Explain confirmed problems separately from possible concerns.
Tell me what to correct, what to verify and what to do next.
Do not submit anything, contact anyone or send files to additional services.
```

The agent should request better scans instead of claiming unreadable pages contain no evidence. It cannot authenticate documents.

## Organise a response to a document request
Share a redacted request and relevant evidence. Keep the stated deadline/timezone visible:
> Use student-500-preparation to organise a response to this Department document request. Extract each requested item and the stated deadline. Match my supplied evidence, identify gaps and suggest a preparation plan. Do not send the response. Ask if the deadline or request meaning is unclear.

Preparation does not authorise lodgement, payment, contact or communication.

## Understand the result
| Status | Meaning |
|---|---|
| Ready for the stated preparation check | Evidence supports that specific check, not visa approval. |
| Missing | An applicable item is known absent; not-supplied evidence should be labelled separately. |
| Needs correction | A confirmed defect/mismatch needs a concrete fix. |
| Needs verification | Applicability, contents, a source or a professional question is unresolved. |
| Not applicable | Known facts or checked exception support this conclusion. |

A document can be readable but still need verification of currency or compliance. A family member may have different requirements from the student. No single overall readiness score is used.

## If the agent cannot browse
Ask it to continue supported presence/readability/consistency checks. Current rule compliance should remain Needs verification. You may provide dated official checklist/form/request screenshots, but they do not automatically resolve every requirement. Never ask it to guess current fees, test scores, funds thresholds or exceptions.

## Helpful follow-ups
- “Show only the corrections and next actions in plain [language].”
- “Which missing facts change whether this document is required?”
- “Show the official source for this requirement.”
- “Recheck these dates against the insurance and welfare periods.”
- “What specific question and evidence should I take to a qualified adviser?”
- “Review this corrected document without treating earlier unchecked assumptions as facts.”

## Limits and safe use
Do not ask for invented financial evidence, hidden contradictions or fabricated Genuine Student answers. Keep truthful facts. Statutory bars/waivers, disputed custody, health/character interpretation or refusal/cancellation issues may need a registered migration agent or Australian legal practitioner. Ask for a specific referral question, not a guessed conclusion.

The report stays simple: what was checked, corrections, relevant uncertainties and actions. It need not reproduce the maintainer's research. You can request official links or more explanation at any time.

Use your own private case location if saving a report. Never put applicant documents in this skill repository or GitHub issues. The public skill is licensed for non-commercial use; paid client work or commercial redistribution may need separate permission. Licence: see NOTICE.md and LICENSE.txt.

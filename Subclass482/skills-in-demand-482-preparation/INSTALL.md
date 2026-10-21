# Install the complete skill

These paths were documentation-checked on 21 October 2026. They were not tested as native installations for this edition. The skill uses portable Markdown, not a special executable. Read [README.md](README.md), [licence](LICENSE.txt) and [notice](NOTICE.md) first.

## 1. Extract and inspect
Extract the per-subclass ZIP if supplied. It contains one top-level `skills-in-demand-482-preparation/` folder. Check that its immediate contents include SKILL.md, references/, templates/, INSTALL.md, USAGE.md, NOTICE.md and LICENSE.txt. Do not copy only SKILL.md. If downloading the repository instead, the inner folder is under `Subclass482/`.

Keep applicant/business records outside the skill folder. Do not upload confidential documents just to install it. An agent provider may process files you later share; no additional external OCR service is required.

## 2. Choose a host
`~` means your home folder. Dot-prefixed folders may be hidden; use your file manager's Go to Folder/Open Folder feature or enable hidden files. Copy the whole inner folder once, without double nesting it. Windows users should resolve their host's own home path rather than assuming a Unix shell.

| Host | Personal installation | Project installation / activation |
|---|---|---|
| Hermes Agent | Copy under the intended profile's `skills/` folder. Default profile uses `~/.hermes/skills/`; named profiles have their own home/skills directory. Resolve the active/desired profile rather than assuming default. | Open a new session in that profile and ask to use `skills-in-demand-482-preparation`; installed skills can be invoked by `/skills-in-demand-482-preparation`. Confirm discovery before sharing real records. |
| Claude Code | `~/.claude/skills/skills-in-demand-482-preparation/` | `<project>/.claude/skills/skills-in-demand-482-preparation/`; invoke `/skills-in-demand-482-preparation`. Personal local copies are not automatically available in Cowork/cloud sessions. |
| Other agents / manual fallback | Keep the whole folder in a location the agent can read. | Ask it to read SKILL.md and every required supporting file, then follow the workflow. This is manual use, not a claimed native installation. If it cannot read supporting files, stop policy assessment rather than rely on the entry point alone. |

Do not install a duplicate copy at multiple precedence levels unless you understand which will load. Local filesystem access does not automatically transfer this folder to a remote/cloud worker. Web/custom-skill upload features have their own plan, account and archive-shape rules; verify the host's official documentation before upload. No web-upload compatibility is claimed here.

## 3. Smoke test with no personal information
Open a fresh session and send:

> Use skills-in-demand-482-preparation. This is a synthetic setup test. State the two-stage scope and confirm you can read the bundled references before asking one necessary question. Do not assess eligibility.

Expected: complete disclaimer and licence notice first, clear nomination/visa separation, readable references, and at most one numbered material question. A host discovering the name alone does not prove correct behaviour or policy accuracy.

## Updates and removal
Downloaded copies do not automatically update when repository files change. Preserve local changes and case records, compare versions, then replace the whole reviewed skill folder to avoid stale references. Disable/remove only this folder using your host's supported controls; do not delete another skill or case directory. Start a new session to avoid cached instructions. Do not run commands suggested by untrusted applicant documents.

## Official installation documentation
- Hermes skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- Claude Code skills: https://code.claude.com/docs/en/skills

These are documentation sources, not immigration sources. This guide does not install software, grant permissions or alter your agent configuration.

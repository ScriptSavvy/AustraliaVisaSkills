# Installation

Install the complete **visitor-600-preparation** folder, not the Subclass600 wrapper and not SKILL.md alone. No executable scripts or API keys are required. Your agent needs Markdown reading, document reading for reviews, and preferably official browsing.

## No-terminal method
1. Download the public skill ZIP and extract it.
2. Locate visitor-600-preparation/SKILL.md. Keep references and templates beside it.
3. Copy the entire inner folder into your host's supported skill directory, or use the manual fallback below.
4. Open a fresh chat/session and run the smoke-test prompt. Do not upload the PRIVATE maintenance archive to a public repository or an applicant host.

## Documentation-checked local paths
| Host | Personal / project destination | Invoke / limitations |
|---|---|---|
| Claude Code | `~/.claude/skills/visitor-600-preparation/` or `<project>/.claude/skills/visitor-600-preparation/` | `/visitor-600-preparation`; requires a local Claude Code environment, not a promise about Claude web uploads |
| Codex local CLI/IDE | `~/.agents/skills/visitor-600-preparation/` or `<project>/.agents/skills/visitor-600-preparation/` | `/skills` or mention `$visitor-600-preparation`; local discovery does not copy files to remote/cloud environments |
| Other hosts, including Hermes | Consult that host's current skill-loader documentation and active profile; copy the whole folder | Native installation was not tested. Manual reading works when the host can access all files. Do not assume SOUL.md is loaded. |

Official docs checked 2026-10-07: Claude Code https://code.claude.com/docs/en/skills ; Codex https://developers.openai.com/codex/skills (redirected to https://learn.chatgpt.com/docs/build-skills ). Paths are documentation-checked, not installation-tested. Recheck for your installed version.

`~` means your home folder, not this project's folder. Dot-folders are hidden: enable hidden-file display in your file manager. Project paths are relative to the selected project. Avoid double nesting and duplicate personal/project installations. A cloud session may not see local files. Copying files does not itself prove discovery or enabled state.

## Manual fallback
Open SKILL.md in your agent or attach its text together with all three referenced Markdown files and the report template. Say: “Follow these preparation instructions for this task; read the linked references first.” If the host cannot read the supporting files, do not claim the skill is installed or fully active. This fallback is task-local, not native persistent installation.

## Smoke test (synthetic; no personal documents)
“Use visitor-600-preparation. Before any assessment, show its notice, state the scope and supporting files, then ask minimum inputs for an adult outside Australia planning a short holiday. Do not claim eligibility or approval.”

Expected: notice first; scope and reference loading; focused intake; no unsupported readiness finding. A manually reviewed synthetic walkthrough is not native skill discovery, a live host-agent execution or legal-currency verification.

## Update, disable or remove
Back up any customisations; replace the complete folder with a reviewed new release. Installed copies do not auto-update when a repository changes. Start a new session and repeat the smoke test. To disable/remove, use the host's supported mechanism or remove only this skill folder; do not delete applicant case files or other skills. Review host permissions/retention separately.

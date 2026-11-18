# Installation — Partner visa preparation

## What to install

Install the whole **`partner-visa-preparation/`** folder, including SKILL.md, references, template, guides and licence. Do not install the `PartnerVisas` wrapper, only SKILL.md, research documents or applicant records. The activation name is **`partner-visa-preparation`**, version **0.2.0**.

Use the complete inner folder from the repository or the versioned skill ZIP from the [Partner Visas release page](https://github.com/ScriptSavvy/AustraliaVisaSkills/releases/tag/Partner_Visas).

## Option A — copy the local folder without a terminal

1. Locate `PartnerVisas/partner-visa-preparation/` in the local public-source tree.
2. Use your agent's current documented skills installation method and copy the entire inner folder. Enable hidden folders in your file manager where needed. Avoid double nesting such as `partner-visa-preparation/partner-visa-preparation/SKILL.md`.
3. Confirm the installation is in the intended project or user/profile scope. Back up customisations first and ask before replacing an existing installation. Do not leave two versions of the Partner skill active in the same scope.
4. Start a fresh session or reload as documented, then run the smoke check below. File copying and menu discovery are not proof of correct visa guidance.

| Host / installation route | Project destination | User-wide destination / scope | Evidence and limit |
|---|---|---|---|
| Claude Code manual | `.claude/skills/partner-visa-preparation/` | `~/.claude/skills/partner-visa-preparation/` | Current official skills documentation inspected 17 November 2026; no native activation promised. |
| Vercel installer for Codex | `.agents/skills/partner-visa-preparation/` | `~/.agents/skills/partner-visa-preparation/` | Installer's current supported-agent table inspected 17 November 2026. This is the installer's destination, not a fresh independent verification of every Codex host/account loader. |
| Other supported local agents | Use the installer's documented destination for the selected exact agent ID | Review its documented scope and any shared folders | Do not assume selecting an agent isolates it from other loaders sharing the same directory. |
| Hermes or another native host | Use that host's documented active skills folder | Check the intended profile/home or workspace, not just the running session's default | Follow current host documentation/settings. No host-specific CLI command or installation is implied by this guide. |

`~` means your home folder; on Windows use the equivalent user-profile home. Project paths are inside the actual agent workspace. Local files do not automatically reach web/custom-skill accounts, remote workers or cloud sessions. Product/account policies can restrict discovery, tools, file access and uploads.

## Option B — CLI for supported local agents

This route requires **Node.js 22.20.0 or later**, npm/npx and internet access, according to the inspected installer package metadata. `npx` downloads/runs the third-party **Vercel Labs skills** installer, separate from Immigent® and your agent. Review its source, permission prompts, telemetry settings and overwrites. Its documentation says setting `DISABLE_TELEMETRY=1` or `DO_NOT_TRACK=1` disables telemetry and security-audit requests; use your operating system's supported environment-setting method if you choose this. It does not install the host agent or clear immigration/professional requirements.

### Use a local source

From an isolated project or the intended agent workspace, substitute the actual local path to the **public-source repository root**:

```bash
npx skills add <local-public-source-root> --skill partner-visa-preparation --agent claude-code --copy
```

The angle-bracket path is a placeholder, not a literal command argument. Do not point the installer at a mixed research/applicant-record workspace. Review which exact skill it discovers before copying. Replace `claude-code` with a documented supported ID such as `codex` when appropriate; consult the current supported-agent list rather than assuming all apps are covered.

- Project installation is the default; add `-g` only if you deliberately want user-wide scope.
- `--copy` requests complete copied files rather than symlinks. Inspect the actual destination and avoid duplicate manual/CLI copies.
- To inspect discovery without installation, use `npx skills add <local-public-source-root> --list`. Do not assume a JSON listing flag exists.
- Do not use `--all` or bypass overwrite review just to install this one skill.

### Install from GitHub

For a supported local agent, the repository command is:

```bash
npx skills add ScriptSavvy/AustraliaVisaSkills --skill partner-visa-preparation --agent claude-code --copy
```

This command uses the repository's default branch, not an attached release ZIP. The files may differ; choose the attached skill ZIP if you need a specific packaged edition.

Installer documentation and package metadata inspected on **17 November 2026** identify version **1.9.0**, Node `>=22.20.0`, local-directory sources, `--skill`, `--agent`, `--copy`, `--list` and `-g`. Those checks are not native-host activation or applicant-response tests. Earlier successful copying of another skill does not test this edition.

## Option C — download the release ZIP

On the [Partner Visas release page](https://github.com/ScriptSavvy/AustraliaVisaSkills/releases/tag/Partner_Visas), choose **`partner-visa-preparation-v0.2.0.zip`** under **Assets**, not a **Source code** archive. Extract it to obtain one top-level **`partner-visa-preparation/`** folder containing all instructions, references, guides, template and notices. Follow the actual bundled version; do not replace files with a summary.

For agents supporting ZIP attachments and installation, attach only the reusable skill ZIP and say:

> Inspect the attached ZIP and read its INSTALL.md. Install the complete partner-visa-preparation folder for this agent's supported current profile/workspace. Preserve every supplied runtime file. Ask before replacing an installation, verify discovery and report the name, version and location. If persistent installation is unavailable, explain that limit rather than claiming success.

Attaching/reading a ZIP is not installation. If unsupported, extract and copy the whole folder manually. Check host/provider processing and retention before attachment; no applicant documents, credentials or case reports belong in the installer payload.

## Manual Markdown fallback

If native loading is unavailable, keep the complete folder accessible and ask:

> Read partner-visa-preparation/SKILL.md and every supporting reference required for my task. Follow it for my Partner-family preparation. State any file-reading or browsing limitation instead of inventing a check.

This is task-context use, not guaranteed persistent installation. For scans, the host needs suitable image/text tools. If it cannot inspect a document or browse, use relevant redacted readable text and keep affected checks Needs verification. No additional external processor or executable runtime script is required by this skill.

## Smoke check, updating and removal

Start a fresh session with no personal documents and ask:

> Use partner-visa-preparation. State your scope and the supporting files you need. Do not assess me yet.

Expected: the complete disclaimer and licence notice before guidance; correct family scope and applicable reference loading; no eligibility finding or unnecessary bulk questionnaire. Ask the host to confirm discovery/name/version/location separately from this response. This smoke prompt is not a claim that native execution has already been tested.

If discovery fails, inspect folder nesting, exact activation name, active workspace/profile, disabled skills and host support. Reload as documented. Installer discovery tools do not establish correct host behaviour.

Installed copies do not automatically update from repository edits. Back up customisations and keep case records outside the skill. For an authorised update, replace only the selected complete inner skill folder, verify its files and reload; do not silently merge conflicting editions. Disable/remove only this skill through the host control or its exact folder, preserving unrelated skills and applicant documents.

See [usage](USAGE.md), [README](README.md), [licence](LICENSE.txt) and [attribution](NOTICE.md).

## Documentation basis and limitations

- [Claude Code — skills](https://code.claude.com/docs/en/skills).
- [Vercel Labs skills — commands](https://github.com/vercel-labs/skills/blob/main/docs/commands.md), [supported agents](https://github.com/vercel-labs/skills/blob/main/docs/agents.md), [telemetry/settings](https://github.com/vercel-labs/skills/blob/main/docs/troubleshooting.md#telemetry), and [npm package metadata](https://registry.npmjs.org/skills/latest).

Claude Code documentation, installer commands/agents and package metadata were inspected on 17 November 2026. Codex's official documentation retrieval was blocked; the table labels its installer-derived basis rather than claiming that source was freshly verified. Telemetry settings should be checked from the linked responsible installer documentation before execution. Documentation inspection does not establish end-to-end compatibility, source/ZIP equality, immigration accuracy, professional review or publication.

# Install the complete skill

Copy the whole **student-guardian-590-preparation** folder, not just SKILL.md and not the Subclass590 wrapper. Keep references, template and licence files together. No skill-specific plugin, executable or API key is required. Your agent still needs document-reading and official-web access; its own account and privacy rules apply.

## Local agents
- **Hermes:** copy the folder into the intended profile's `skills/` directory. The usual unprofiled location is `~/.hermes/skills/`; an active profile/custom `HERMES_HOME` can use a different home. Do not install into another profile by mistake. Start a new chat and explicitly ask to use `student-guardian-590-preparation`.
- **Claude Code:** copy it into `~/.claude/skills/` for personal use or `.claude/skills/` in the intended project. Activate `/student-guardian-590-preparation` with your task.

`~` means your home folder. Hidden folders may need to be shown in your file manager. The final path must end in `skills/student-guardian-590-preparation/SKILL.md`, not a double-nested skill folder. Copying files locally does not install them in a cloud session.

## No-terminal/manual fallback
Extract the supplied ZIP, open the destination in your file manager and copy the inner folder. If downloading the repository, find `Subclass590/student-guardian-590-preparation/` inside it. If your agent has no native skill loader, keep the files accessible and ask it to read SKILL.md plus all linked runtime references and follow that workflow. Providing files as context is not persistent native installation. Do not promise a host can open ZIPs or inspect scans if it cannot.

## Check, update, remove
First try a synthetic prompt: “Load student-guardian-590-preparation. Describe its scope and the supporting files you need. Do not assess me yet.” Expect first-use notices, preparation limits and focused intake—not an approval prediction.

If discovery fails, check nesting, filename, selected profile/project and disabled-skill settings, then start a new session. Updates require replacing this skill folder after preserving customisations; GitHub changes do not automatically update an installed copy. To remove it, remove only this folder or use the host's disable control, not the entire skills directory or applicant records.

Documentation bodies checked 20 October 2026: Hermes Skills System and Claude Code Skills. Paths are documentation-checked, not end-to-end installation tested. For other hosts, use their current official installation guidance or the manual fallback; no native compatibility claim is made.

Official documentation:
- https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- https://code.claude.com/docs/en/skills

Next: [USAGE.md](USAGE.md).

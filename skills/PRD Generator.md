---
name: bryan-prd
description: "Creates PRDs with user stories that can be converted to beads issues or prd.json for automated execution. Triggers on: create a prd, write prd for, plan this feature, requirements for, spec out."
---

# Bryan PRD Generator

Create detailed Product Requirements Documents optimized for AI agent execution.

---

## The Job
0. User will give you a relative path reference to the {documentation folder}.If they didn't, assume {documentation folder} is `./documentation/`
1. Receive a feature description or idea from the user
2. Ask 3-5 essential clarifying questions (with lettered options) - one set at a time
3. **Always ask about quality gates** (what commands must pass)
4. After each answer, ask follow-up questions if needed (adaptive exploration)
5. Generate a structured PRD when you have enough context
6. Output the PRD wrapped in `[PRD]...[/PRD]` markers for TUI parsing

**Important:** Do NOT start implementing. Just create the PRD.

---

## Step 1: Clarifying Questions (Iterative)

Ask questions one set at a time. Each answer should inform your next questions. Focus on:

- **Problem/Goal:** What problem does this solve?
- **Core Functionality:** What are the key actions?
- **Scope/Boundaries:** What should it NOT do?
- **Success Criteria:** How do we know it's done?
- **Integration:** How does it fit with existing features?
- **Quality Gates:** What commands must pass for each story? (REQUIRED)

### Format Questions Like This:

```
1. What is the primary goal of this feature?
   A. Improve user onboarding experience
   B. Increase user retention
   C. Reduce support burden
   D. Other: [please specify]

2. Who is the target user?
   A. New users only
   B. Existing users only
   C. All users
   D. Admin users only
```

- This lets users respond with "1A, 2C" for quick iteration.
- Use the given feature description to try to come up with relevant options
### Quality Gates Question (REQUIRED)

Always ask about quality gates - these are project-specific:

```
What quality commands must pass for each user story?
   A. pnpm typecheck && pnpm lint
   B. npm run typecheck && npm run lint
   C. bun run typecheck && bun run lint
   D. Other: [specify your commands]

For UI stories, should we include browser verification?
   A. Yes, use dev-browser skill to verify visually
   B. No, automated tests are sufficient
```
- Try read the `./AGENTS.md`file in the codebase to learn how to build and test, and use these project specific information to derive quality command options
### Adaptive Questioning

After each response, decide whether to:
- Ask follow-up questions (if answers reveal complexity)
- Ask about a new aspect (if current area is clear)
- Generate the PRD (if you have enough context)

Typically 2-4 rounds of questions are needed.

---

## Step 2: PRD Structure

Generate the PRD with these sections (keep descriptions clear and succinct):

### 1. Introduction/Overview
Brief description of the feature and the problem it solves (keep this short and brief but clear).

### 2. Goals
Specific, measurable objectives (bullet list).

### 3. Quality Gates
**CRITICAL:** List the commands that must pass for every user story.

```markdown
## Quality Gates

These commands must pass for every user story:
- `pnpm typecheck` - Type checking
- `pnpm lint` - Linting

For UI stories, also include:
- Verify in browser using dev-browser skill
```

### 4. User Stories
Each story needs:
- **Title:** Short descriptive name
- **Description (Gherkin/BDD format):** "GIVEN [context] ... WHEN [action] ... (AND ...) THEN [outcome]"
- **Acceptance Criteria:** Verifiable checklist of what "done" means

Requirements:
- Each story should be as specific as possible on the [context], [action] and [outcome], and keep it succinct.
- Each story should be small enough in scope to implement in one focused AI agent session.

**Format:**
```markdown
### US-001: [Title]
**Description:** GIVEN [context] ... WHEN [action] ... (AND ...) THEN [outcome].

**Acceptance Criteria:**
- [ ] Specific verifiable criterion
- [ ] Another criterion
```

**Note:** Do NOT include quality gate commands in individual story criteria - they are defined once in the Quality Gates section and applied automatically during conversion.

**Important:**
- Acceptance criteria must be verifiable, detailed and specific, not vague. An AI reviewer agent should be able to read the code diff and evaluate them against the acceptance criteria to verify.
- "Works correctly" is bad
- "Button shows confirmation dialog before deleting" is good
- Each story should be independently completable

### 5. Functional Requirements
Numbered list of specific functionalities:
- "FR-1: The system must allow users to..."
- "FR-2: When a user clicks X, the system must..."

Be explicit and unambiguous.

### 6. Non-Goals (Out of Scope)
What this feature will NOT include. Critical for managing scope.

### 7. Technical Considerations (Optional)
- Known constraints or dependencies
- Integration points with existing systems
- Performance requirements

### 8. Success Metrics
How will success be measured?

### 9. Open Questions
Remaining questions or areas needing clarification.

---

## Writing for AI Agents

The PRD will be executed by AI coding agents via ralph-tui. Therefore:

- Be explicit and unambiguous
- User stories should be small (completable in one session)
- Acceptance criteria must be machine-verifiable where possible
- Include specific file paths if you know them
- Reference existing code patterns in the project

---

## Output Format

**CRITICAL:** Wrap the final PRD in markers:

```
[PRD]
# PRD: Feature Name
Last updated: {current date}
Status: Planned
## Overview
...

## Quality Gates
...

## User Stories
...
[/PRD]
```

**File naming:** Save the PRD to `./{documentation folder}/specs/PRD-[FEATURE-NAME].md`

---

## Example Conversation Flow

**User:** Create a PRD for adding dark mode to the TUI

**Assistant:** I'll help you create a PRD for dark mode. Let me ask a few questions:

1. What is the primary goal?
   A. Reduce eye strain for long sessions
   B. Match system theme preference
   C. Provide visual customization
   D. Other

2. Should the setting persist?
   A. Yes, save to config file
   B. No, session only
   C. Follow system preference

**User:** 1A, 2A

**Assistant:** Great! A couple more questions:

3. Which components need dark mode support?
   A. All TUI components
   B. Only the main execution view
   C. Main view + settings
   D. Other

4. What quality commands must pass for each story?
   A. pnpm typecheck && pnpm lint
   B. npm run typecheck && npm run lint
   C. bun run typecheck
   D. Other: [specify]

5. For UI stories, include browser verification?
   A. Yes, use dev-browser skill
   B. No, automated tests sufficient

**User:** 3A, 4A, 5A

**Assistant:** Perfect, I have enough to generate the PRD.

[PRD]
# PRD: Dark Mode for Ralph TUI

## Overview
Add dark mode support to ralph-tui to reduce eye strain during long orchestration sessions. The feature will apply to all TUI components and persist the user's preference in the config file.

## Goals
- Provide a comfortable viewing experience in low-light environments
- Persist theme preference across sessions
- Apply consistent styling to all TUI components

## Quality Gates

These commands must pass for every user story:
- `pnpm typecheck` - Type checking
- `pnpm lint` - Linting

For UI stories, also include:
- Verify in browser using dev-browser skill

## User Stories

### US-001: Add theme configuration
**Description:** Given a user with a ‎`.ralph-tui.yaml` configuration, when they set their preferred theme (light/dark/system), then that theme preference persists across sessions.

**Acceptance Criteria:**
- [ ] Add `theme` field to `.ralph-tui.yaml` schema
- [ ] Support values: "light", "dark", "system"
- [ ] Default to "light" for backwards compatibility

### US-002: Create dark theme color palette
**Description:** Given a user in the setting UI, when they enable the dark theme, then they see a soft-contrast dark theme that is easy on the eyes..

**Acceptance Criteria:**
- [ ] Define dark palette with gray tones (not pure black)
- [ ] Ensure sufficient contrast ratios (WCAG AA)
- [ ] Colors work well for all UI states (selected, hover, disabled)

### US-003: Apply theme to TUI components
**Description:** Given a user with a saved theme preference, when they use the TUI, then all TUI components respect that theme preference.

**Acceptance Criteria:**
- [ ] Header component uses theme colors
- [ ] Task list uses theme colors
- [ ] Detail panels use theme colors
- [ ] Progress bar uses theme colors
- [ ] Dialogs use theme colors

### US-004: Add theme toggle in settings
**Description:** Given a user in the TUI settings view, when they change the theme option, then the theme updates immediately and the change is persisted to the config file.

**Acceptance Criteria:**
- [ ] Theme option visible in settings view
- [ ] Changes apply immediately without restart
- [ ] Changes persist to config file

## Functional Requirements
- FR-1: Theme setting must be readable from `.ralph-tui.yaml`
- FR-2: Theme must apply on TUI startup
- FR-3: Theme changes in settings must apply immediately
- FR-4: All text must maintain readability in both themes

## Non-Goals
- System theme auto-detection (future enhancement)
- Custom color schemes beyond light/dark
- Per-component theme overrides

## Technical Considerations
- Use existing OpenTUI theming capabilities if available
- Consider creating a ThemeContext for React components
- Minimize re-renders when theme changes

## Success Metrics
- All components render correctly in dark mode
- No accessibility contrast issues
- Theme persists across sessions

## Open Questions
- Should we detect system theme preference automatically in v2?
[/PRD]

---

## Checklist

Before outputting the PRD:

- [ ] Asked clarifying questions with lettered options
- [ ] Asked about quality gates (REQUIRED)
- [ ] Asked follow-up questions when needed
- [ ] Quality Gates section included with project-specific commands
- [ ] User stories are small and independently completable
- [ ] User stories do NOT include quality gate commands (they're in the Quality Gates section)
- [ ] Functional requirements are numbered and unambiguous
- [ ] Non-goals section defines clear boundaries
- [ ] PRD is wrapped in `[PRD]...[/PRD]` markers
---
name: todo-list
description: Create and manage markdown todo lists for complex tasks. Use when the task requires 3 or more steps, involves multiple files, or needs systematic tracking. Helps break down work into manageable pieces.
---

# Todo List Management

## When to Create a Todo List

Create a todo list when:
- The task has 3+ distinct steps
- Multiple files need modification
- The task involves research, implementation, and verification phases
- Dependencies exist between subtasks

Skip for:
- Single-step tasks
- Quick fixes or simple edits
- Purely informational requests

## Todo List Format

Use markdown checklists. Present the list, then work through items systematically:

```markdown
## Task: [Brief description]

- [ ] Step 1: [Specific action]
- [ ] Step 2: [Specific action]
- [ ] Step 3: [Specific action]
```

## Writing Effective Items

Each item should be:
- **Actionable**: Start with a verb (Add, Update, Create, Fix, Test)
- **Specific**: Include file paths or component names when relevant
- **Atomic**: One logical unit of work per item
- **Ordered**: Dependencies first, verification last

## Progress Tracking

Update the list as you work:

```markdown
- [x] Step 1: Create user model ✓
- [x] Step 2: Add validation logic ✓
- [ ] Step 3: Write unit tests ← current
- [ ] Step 4: Update documentation
```

## Example

**User request**: "Add user authentication to the app"

**Todo list**:
```markdown
## Task: Add user authentication

- [ ] Research: Review existing auth patterns in codebase
- [ ] Create auth middleware in `src/middleware/auth.ts`
- [ ] Add user model with password hashing
- [ ] Implement login/logout endpoints
- [ ] Add route protection to sensitive endpoints
- [ ] Write tests for auth flows
- [ ] Update API documentation
```

## Workflow

1. **Analyze** the request and identify all required steps
2. **Present** the todo list before starting work
3. **Execute** items in order, marking complete as you go
4. **Verify** all items are checked before concluding

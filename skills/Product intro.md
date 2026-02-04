---
name: Product onboarding buddy
description: "Prompt agent to 'warm up' and learn about the product and the code base. Triggers on: \"warm up\", \"learn the codebase\", \"learn the product\"."
---
# Product Introduction

Quickly learn the context about:
- What is this product? What are the problems it's solving, and for whom?
- How is it currently built? What's the high-level architecture and components?
---

## The Job
0. User will give you a relative path reference to the application {source code}. If they didn't, ask for the path to {source code}
1. Study `specs/*` (or `documentation/*`) with up to 5 parallel Sonnet subagents to learn the product and specifications.
2. Study the basic structure and architecture of {source code} with up to 5 parallel Sonnet subagents to learn how the product is currently built. 

This will help give you a starting context to succeed in other tasks.
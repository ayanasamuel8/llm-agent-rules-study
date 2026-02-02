# AI Agent Rules Configuration for Cursor

A project demonstrating how to configure and refine AI coding agent behavior in **Cursor IDE** using explicit rules. This repository contains the rules configuration, test files, and documentation from an iterative process of understanding and controlling AI agent behavior.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Cursor Rules Configuration](#cursor-rules-configuration)
  - [What Are Cursor Rules?](#what-are-cursor-rules)
  - [Rules Breakdown](#rules-breakdown)
- [Testing Methodology](#testing-methodology)
- [Key Insights](#key-insights)
- [Getting Started](#getting-started)
- [License](#license)

## Overview

This project explores how explicit rules influence AI agent behavior in Cursor IDE. The goal was to:

- Understand how rules control agent actions
- Improve predictability and reduce unintended changes
- Align agent behavior with developer intent and expectations
- Document the iterative refinement process

## Project Structure

```
.
├── .cursor/
│   └── rules/
│       └── agent.mdc          # Cursor agent rules configuration
├── docs/
│   └── task-3-documentation.md # Detailed documentation of the process
├── test_agent.py              # Sandbox test file for agent behavior
└── README.md
```

## Cursor Rules Configuration

### What Are Cursor Rules?

Cursor Rules are configuration files that define behavioral constraints for the AI coding agent. They act as a **behavioral contract** between the developer and the AI, ensuring consistent, predictable, and safe code modifications.

Rules are stored in `.cursor/rules/` as `.mdc` files and can be configured to apply:
- **Always** — applied to every interaction
- **Contextually** — applied based on file patterns or conditions

### Rules Breakdown

The rules file (`.cursor/rules/agent.mdc`) is structured into the following sections:

#### Coding Standards
- Follow existing project structure strictly
- Match existing coding style, formatting, and naming conventions
- Prefer explicit types and clear interfaces
- Avoid premature abstraction
- No unused variables, imports, or dead code
- Add comments only when logic is non-obvious

#### File & Refactor Safety
- Do NOT delete files without explicit permission
- Do NOT rename files or directories unless instructed
- Do NOT perform large refactors unless explicitly requested
- For multi-file changes, explain the plan before applying changes
- Prefer minimal, targeted diffs over sweeping changes

#### Autonomy & Decision-Making
- Small, localized changes → act immediately
- Architectural changes → ask for confirmation first
- If multiple valid approaches exist, propose the best one and explain trade-offs
- Never silently make breaking changes

#### Tool Usage
- Use tools (tests, linters, commands) only when they add clear value
- Do not run commands speculatively
- Explain why a tool is being used when non-obvious

#### Testing & Validation
- When modifying logic, update or add tests if they exist
- Do not introduce failing tests
- If tests are missing, suggest where tests would be valuable
- Validate edge cases mentally before finalizing code

#### Error Handling & Uncertainty
- Never fabricate library behavior or APIs
- If uncertain, say so clearly
- When blocked, propose alternatives or ask a focused question
- Prefer partial, correct solutions over complete but uncertain ones

#### Output Expectations
- Code should be production-ready
- Avoid placeholders like `TODO` unless explicitly requested
- Avoid overengineering

#### Scope Control & Feature Expansion
- Do NOT add new features, parameters, or functionality unless explicitly requested
- For vague requests (e.g., "improve", "clean up", "optimize"):
  - Default to small, incremental improvements only
  - Ask a clarifying question before expanding scope
- Avoid changing public APIs unless explicitly instructed
- Improvements should prioritize readability, safety, or correctness without altering behavior

## Testing Methodology

The agent was tested using three types of prompts to evaluate behavior:

| Prompt Type | Example | Expected Behavior |
|-------------|---------|-------------------|
| **Explicit** | "Add input validation and types" | Make minimal, targeted changes |
| **Vague** | "Improve this function" | Ask clarifying questions before acting |
| **Risky** | "Refactor this project" | Propose a plan and ask for confirmation |

### Test File

A sandbox Python file (`test_agent.py`) was created to observe agent behavior:

```python
def calculate_total(price, tax, discount=0, round_to=2):
    """Calculate total price including tax and optional discount."""
    # Implementation with validation, type hints, and Decimal precision
    ...
```

## Key Insights

### 1. Rules Act as a Behavioral Contract
Without explicit constraints, the agent optimizes for "helpfulness," which can lead to unintended changes. Rules define clear boundaries.

### 2. Explicit Constraints Improve Predictability
Adding clear boundaries (e.g., no feature expansion without permission) significantly improved:
- Predictability
- Safety
- Trust in the agent's output

### 3. Ambiguity Is the Biggest Risk Factor
Vague prompts like "improve" or "clean up" are the primary source of undesired behavior. Rules that define how to handle ambiguity are essential.

### 4. Iteration Over Perfection
The most valuable learning came from:
- Observing real failures
- Adjusting rules accordingly
- Re-testing the same scenario

This mirrors real-world AI agent configuration workflows.

## Getting Started

### Prerequisites

- [Cursor IDE](https://cursor.sh/) installed

### Using These Rules in Your Project

1. Clone this repository or copy the `.cursor/rules/` folder to your project root:

   ```bash
   mkdir -p .cursor/rules
   cp path/to/agent.mdc .cursor/rules/
   ```

2. Open your project in Cursor IDE

3. The rules will automatically apply to all AI agent interactions

### Customizing Rules

Edit `.cursor/rules/agent.mdc` to adjust behavior for your workflow:

- Modify existing rules to match your team's conventions
- Add new sections for domain-specific constraints
- Adjust the `alwaysApply: true` frontmatter to control when rules apply

## Documentation

For a detailed walkthrough of the configuration process, including what worked, what didn't, and how issues were resolved, see:

- [Task 3 Documentation](docs/task-3-documentation.md)

## License

This project is open source and available under the [MIT License](LICENSE).

---

**Author:** 10Academy Assessment  
**Purpose:** Demonstrating AI agent behavior control through explicit rules configuration

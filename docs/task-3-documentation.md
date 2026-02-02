# Documentation — AI Agent Rules Configuration (Cursor)

## Overview

In this task, I documented the process of configuring and refining an AI coding agent in **Cursor** using a rules file (`.cursor/rules/agent.mdc`). The goal was to understand how explicit rules influence agent behavior, improve predictability, reduce unintended changes, and align the agent’s actions with my intent and expectations.

This documentation captures:

* What changes were made
* What worked well
* What did not work initially
* Key insights gained from testing and refinement

---

## 1. What I Did

### 1.1 Created a Cursor Rules File

I created a rules file at the following location:

```
.cursor/rules/agent.mdc
```

This file defines **global behavior rules** for the Cursor AI agent and was configured to **Apply Always**, ensuring consistent behavior across all interactions.

---

### 1.2 Defined Structured Agent Rules

The rules file was structured into clear sections to control different aspects of agent behavior, including:

* **Agent Identity & Mindset**

  * Act as a senior software engineer
  * Prefer correctness, maintainability, and minimal diffs
  * Avoid hallucinating APIs or behavior

* **Communication Rules**

  * Be concise and clear
  * Ask clarifying questions only when requirements are ambiguous
  * Avoid unnecessary explanations

* **Coding Standards**

  * Follow existing structure and style
  * Avoid unused code and premature abstractions
  * Preserve existing formatting unless explicitly asked to change it

* **File & Refactor Safety**

  * No file deletion or renaming without permission
  * No large refactors without confirmation
  * Explain plans before multi-file changes

* **Autonomy & Decision-Making**

  * Act immediately on small, safe changes
  * Ask before architectural or breaking changes

---

### 1.3 Created a Sandbox Test File

Since the project folder was initially empty, I created a small **sandbox Python file** to test agent behavior:

```python
def calculate_total(price, tax):
    return price + price * tax
```

This file was intentionally simple and imperfect to observe how the agent reacts to different prompts.

---

### 1.4 Tested the Agent with Real Prompts

I tested the agent using three types of prompts:

1. **Explicit request**

   * *“Add input validation and types.”*
2. **Vague request**

   * *“Improve this function.”*
3. **Risky request**

   * *“Refactor this project.”*

These tests were used to evaluate scope control, safety, and clarification behavior.

---

### 1.5 Refined the Rules Based on Observed Behavior

During testing, I identified an important issue with vague prompts and updated the rules file to include explicit **scope control** and **ambiguity handling**:

* Prevent feature expansion without explicit request
* Require clarification for vague instructions like “improve” or “clean up”
* Preserve public APIs unless explicitly instructed

After updating the rules, I re-ran the same tests to verify improvement.

---

## 2. What Worked

### 2.1 Clear, Explicit Prompts Produced Ideal Results

When the prompt was clear and specific (e.g., *“Add input validation and types”*), the agent:

* Made minimal, targeted changes
* Added proper type hints and validation
* Did not refactor or expand scope
* Preserved the original behavior

This confirmed that the **baseline rules for small, localized changes worked well**.

---

### 2.2 Refactor Safety Rules Worked Correctly

When prompted with *“Refactor this project”*, the agent:

* Explored the project structure first
* Proposed a refactor plan instead of acting immediately
* Explained trade-offs
* Asked for explicit confirmation before making changes

This matched the intended behavior for **architectural or multi-file changes**.

---

### 2.3 Scope-Control Rules Fixed Vague Prompt Behavior

After refining the rules, the agent responded to *“Improve this function”* by:

* Recognizing the request was ambiguous
* Asking focused clarifying questions
* Proposing safe improvement dimensions (readability, robustness, performance)
* Avoiding any code changes until intent was clarified

This demonstrated that the rules successfully constrained the agent’s autonomy.

---

## 3. What Didn’t Work (and How I Fixed It)

### 3.1 Initial Issue: Scope Creep on Vague Prompts

Before refinement, the prompt *“Improve this function”* caused the agent to:

* Introduce new features (discounts, rounding)
* Change the return type
* Add additional parameters
* Expand the function far beyond the original intent

Although the generated code was technically high quality, it violated expectations around **minimal change** and **API stability**.

---

### 3.2 Troubleshooting Approach

To address this issue, I:

1. Identified the root cause: ambiguous prompts + excessive agent autonomy
2. Added explicit rules to prevent:

   * Feature addition without request
   * Public API changes without confirmation
3. Required clarification for vague instructions
4. Re-tested the same prompt to validate behavior improvement

This iterative process was central to completing Task 2 successfully and informed this documentation.

---

## 4. Insights Gained

### 4.1 Rules Act as a “Behavioral Contract”

The rules file functions as a **behavioral contract** between the user and the AI agent. Without explicit constraints, the agent optimizes for “helpfulness,” which can lead to unintended changes.

---

### 4.2 Explicit Constraints Improve Predictability

Adding clear boundaries (e.g., no feature expansion without permission) significantly improved:

* Predictability
* Safety
* Trust in the agent’s output

The agent behaved more like a disciplined engineering collaborator rather than an over-eager assistant.

---

### 4.3 Ambiguity Is the Biggest Risk Factor

Vague prompts such as *“improve”* or *“clean up”* are the primary source of undesired behavior. Explicit rules that define how the agent should react to ambiguity are essential.

---

### 4.4 Iteration Is More Important Than Perfection

The most valuable learning came from:

* Observing real failures
* Adjusting rules accordingly
* Re-testing the same scenario

This mirrors real-world AI agent configuration workflows used by experienced practitioners.

---

## 5. Final Outcome

By the end of this task:

* The Cursor agent behaves consistently and safely
* Scope creep is controlled
* Clarification is requested when intent is unclear
* Architectural changes require confirmation
* The agent’s behavior aligns closely with my expectations and thought process

This demonstrates effective control of an AI coding agent through well-designed, iteratively refined rules.

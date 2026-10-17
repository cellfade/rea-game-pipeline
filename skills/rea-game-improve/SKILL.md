---
license: MIT
name: rea-game-improve
description: "Propose and evaluate evidence-backed improvements to a game reconstruction workflow or skill after observed failures. Use for bounded retrospectives and regression-driven pipeline improvement, not autonomous policy changes."
---

# REA game improve

Improve the workflow from demonstrated outcomes, not speculative self-modification. Select one repeated failure, costly ambiguity, or validated opportunity from a run. Capture the baseline, affected artifacts, expected outcome, actual outcome, likely cause, and the smallest intervention. Keep new product requests separate from workflow defects.

Create a candidate patch in a caller-selected checkout or isolated branch. Changes may address a skill instruction, task handoff, harness validation, evidence schema, or regression fixture. Do not edit global installed skills, memory, client configuration, permissions, approval requirements, or production state unless separately authorized. Never weaken a gate simply to make a run pass. This skill provides no tools or new authority.

Define a realistic regression scenario before evaluating the patch. Include only the minimum raw inputs required, expected observable outcomes, permitted side effects, and a comparable baseline. Prefer decision/outcome checks over assertions that specific wording or headings exist. Exercise both the original failure and a neighboring case that should remain supported. Inspect actual outputs; a green schema test cannot establish investigation quality.

When available and authorized, give an independent reviewer the candidate skill and a realistic request without the suspected fix or desired verdict. Keep evaluation artifacts isolated from production. Without independent review, record a serial self-review and leave the independence gate pending where required. If necessary tools are missing, provide a reproducible test handoff instead of claiming the scenario passed.

Record baseline versus candidate result, regression evidence, review findings, scope/permission impact, tradeoffs, and accept/revise/reject recommendation. Promotion is a separate reviewed action within the user's authorization; the author must not self-approve a change requiring independent acceptance. Bound experimentation to one candidate and at most two revisions per cycle, then summarize unresolved causes and seek a narrower experiment. Do not run indefinite release or improvement loops.

For public candidates, remove private artifacts, personal paths, machine/account identifiers, credentials, and proprietary assets. Verify source/license provenance for any incorporated text or fixtures. Keep private customization in an explicitly separate layer; MIT applies only to original licensed material. If using an optional harness, inspect its interface and pass the caller-selected checkout explicitly.

Read [evaluation scenarios](references/scenarios.md) when conducting a retrospective or evaluating an improvement.

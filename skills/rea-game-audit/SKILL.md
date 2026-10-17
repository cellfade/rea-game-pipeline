---
license: MIT
name: rea-game-audit
description: "Audit a game reconstruction against evidence, functional acceptance, asset provenance, performance, human UAT, and release state. Use for reconstruction milestones and release reviews, not generic code linting."
---

# REA game audit

Judge a specific milestone from inspectable artifacts and fresh checks. Establish the exact commit/build, target version, rule specification, provenance ledger, acceptance scenarios, declared performance budgets, and intended deployment. If these are missing, audit the available scope and mark gaps; do not silently invent requirements.

Prefer an independent reviewer when authorized orchestration is available. Give that reviewer raw artifacts, scope, and criteria without the author's desired verdict. Otherwise perform a separate serial review and disclose that independence was not achieved. This skill gives no additional tool or external-action permissions.

Audit these connected dimensions:

- **Evidence and fidelity:** trace historical claims to source/observation; separate disassembly from original source, assumptions from recovered rules, redesign from fidelity. Verify actual REA capability rather than assuming target support.
- **Playable behavior:** execute acceptance scenarios including a representative success path, failure/recovery, and important edge cases. Check state transitions and timing against the rule spec, not merely button presence.
- **Visual/asset integration:** inspect rendered states at intended sizes and gameplay camera; verify exports in the engine, provenance and redistribution rights, and measured budgets. Concept art is not gameplay evidence.
- **Engineering/release:** inspect relevant diffs, meaningful tests, build output, dependency/security findings in scope, public-package privacy, and deployed artifact consistency. Distinguish local build, pushed commit, deployment started, deployment reachable, and deployed flow verified.
- **Human UAT:** provide an executable scenario sheet and record who accepted which build, observations, unresolved issues, and disposition. Agent/browser checks are automated acceptance evidence, not human sign-off.

Report findings with severity, observed behavior, reproduction, evidence locator, impact, and recommended correction. Separate reproduced failures from suspected issues and missing coverage. Classify missing tooling as a verification gap, never a pass. Re-run affected checks after fixes and update the reviewed build identity; do not repeat the entire suite without a reason.

Release readiness requires the agreed gates, actual authorization, and recorded human acceptance or explicit waiver. An audit cannot self-approve an external action. Keep raw private artifacts outside the public report; sanitize identifying paths, credentials, account/device data, and nonredistributable captures. Use a caller-selected checkout for reports or any optional harness.

Read [evaluation scenarios](references/scenarios.md) for realistic audit exercises.

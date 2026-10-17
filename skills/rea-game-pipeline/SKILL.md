---
license: MIT
name: rea-game-pipeline
description: "Coordinate an evidence-led game reconstruction across investigation, rule specifications, assets, implementation, audit, human UAT, and release. Use for game reconstruction planning and execution, not unrelated development."
---

# REA game pipeline

Turn a reconstruction brief into a bounded, reviewable playable result. This is independent community guidance around [REA](https://github.com/morluto/rea), not an upstream REA skill or a grant of tool access.

## Establish the run

Record target version, artifact hash where available, permitted inputs, desired fidelity, platform, performance budget, and one playable milestone. Separate historical behavior from intended redesign. Inspect installed tool schemas and versions before planning tool calls. Never assume REA supports SNES or another console format. Pair available REA functions with a suitable emulator, debugger, disassembler, or direct observation; record unsupported operations explicitly.

Use a caller-selected project checkout. If using a separate harness, inspect its help/schema and pass that checkout explicitly; do not infer a project from the skill installation directory. If REA, Blender, browser automation, or orchestration is absent, use available CLI/manual evidence or produce a runnable handoff with the exact missing capability. A skill installs no server and grants no permissions.

## Plan and execute

Maintain a dependency graph with task ID, prerequisites, question, artifact, acceptance criterion, owner, allowed files, status, and evidence references. Use these stage gates:

1. **Inventory → question:** inputs identified; one answerable question per investigation task.
2. **Evidence → rule specification:** source, disassembly, compiled artifact, observed behavior, inference, and proposed design remain distinct. Unknowns become explicit experiments or declared prototype assumptions.
3. **Specification → implementation:** inputs, state transitions, timing units, outcomes, edge cases, and acceptance examples defined. Implement uncertain rules only as labeled assumptions with replaceable boundaries.
4. **Assets → integration:** provenance, license, budget, export, and actual engine inspection complete. Generated imagery is concept art until production validation.
5. **Audit → human UAT:** independent evidence and functional review, reproducible checks, and unresolved findings provided. Automated browser checks do not constitute human acceptance.
6. **Release:** user authorization covers the destination and action; required checks pass and human UAT is recorded or explicitly waived by the authorized person. Verify deployed behavior and report actual release state.

When authorized and supported, delegate independent research, assets, implementation, and audit tasks with owned files and explicit handoffs. Serialize shared Blender scene mutations or use separate scene files. Give the reviewer actual artifacts and raw evidence without supplying the desired verdict. Without orchestration tools, run the same roles serially and label review as non-independent. Retry a failed tool operation at most twice after inspecting errors; then change the approach or report a blocker. Never loop approvals or releases.

Use specialized evidence, asset, audit, or improvement skills by name only when installed and relevant; this folder works alone. Keep raw binaries, dumps, user paths, credentials, private captures, and private notes outside public deliverables. Publication requires a separate provenance/privacy pass; MIT covers this workflow's original code and text, not third-party games or assets.

Read [evaluation scenarios](references/scenarios.md) when validating or revising this workflow. End a run with evidence achieved, remaining uncertainty, review/UAT state, deployment state, and next bounded experiment.

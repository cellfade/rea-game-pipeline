# Bounded self-improvement

Improvement is an auditable engineering loop, not autonomous permission expansion or unreviewed self rewriting.

1. Record an observed failure: task/question, input revision, expected behavior, actual result, evidence, cause hypothesis and cost. Keep private raw records in the project, not the public skill package.
2. Reproduce with the smallest synthetic or shareable fixture. Separate tool failure, data ambiguity, skill decision error and implementation defect.
3. Propose one narrow candidate: which instruction/contract/script changes, why, expected benefit and potential regression.
4. Add a behavioral regression and an unrelated holdout. Compare correctness, evidence honesty, task completion, tool calls, elapsed time and token/cost data where actually available.
5. Independent reviewer evaluates the candidate without a supplied desired verdict. Preserve failed cases; do not lower acceptance requirements to pass.
6. Authorized maintainer approves a versioned change. Re-run relevant package/evaluation checks, publish the diff and document remaining limits. Retain rollback version.

`propose-improvement` emits a candidate linked to a failure ID. It does not patch files, approve a change, update model memory, rerun tools or publish. Actual patches need an agent/developer and a reviewer.

Escalate or stop after the declared retry/time/cost limit. Never remove evidence requirements, disable publication checks, broaden tool permissions, alter target selection or fabricate human acceptance as an efficiency improvement.

Useful metrics: success per bounded task; unsupported claims; required evidence coverage; regression pass/fail; independent-review defect yield; duplicate tool work; actual cost/latency. Missing measurements remain unknown. Shorter output alone is not better performance.

## Improvement history for this release

Independent adversarial review exposed ownership-path aliases, stale review/UAT passes, evidence-ID collisions and prerequisite gaps. These became regression tests and targeted validator changes before publication. The validation report records actual outcomes. That demonstrates one reviewed correction cycle; it does not establish long-term autonomous learning performance.

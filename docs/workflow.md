# Evidence-led game workflow

Use one milestone small enough to compare: one mechanic, one scene or one complete battle. A complete remake is a later collection of milestones, not the default first task.

| Stage | Required output | Exit evidence |
|---|---|---|
| Target and scope | Artifact identity, permitted inputs, questions, intended changes | Version/hash or explicit unavailable state; capability matrix |
| Investigation | Bounded manual/code/runtime observations | Exact locators, reproducible scenario, coverage and unknowns |
| Specification | Inputs, transitions, timing units, outputs, edge cases | Each rule linked to observation or proposed design decision |
| Prototype | Separate simulation, renderer and asset contracts | Deterministic scenario, useful error states, labeled provisional rules |
| Production assets | Source/build decision and asset manifest | Provenance, Blender/export checks, actual renderer readback |
| Independent audit | Findings, tests, fidelity deltas, publication review | Exact subject revision and independent review result |
| Human UAT | Named scenario and accepted/rejected/waived state | Actual authorized human decision; no fabricated approval |
| Release | Exact source, destination and deployed artifact | Live browser smoke, test evidence and rollback target |

Original developer source, annotation projects, disassembly exports, compiled artifacts and runtime observations are different evidence sources. A successful static graph is not proof of execution. A screenshot is not proof of mechanics. Use REA only for supported operations; specialized console tooling may be necessary.

Keep proposed redesign rules versioned and replaceable. Do not force all art and fidelity work to block a useful provisional prototype. Define separate prototype and reference-informed release scopes; the latter includes verified evidence for the behaviors it claims.

Every release packet records what is implemented, tested, independently reviewed, reference-verified and human accepted. Missing/failed/blocked checks remain visible. Public summaries exclude raw targets and sensitive captures.

## Minimal project record

The optional harness consumes project.json in a separate working project. See harness/README.md for the exact schema; the harness is not embedded in the skills. A task owns literal relative paths and exclusive named resources. A subject SHA-256 is an operator-provided revision assertion, not an automatically computed software attestation.

Prototype audit checks scope closure, done state, required test receipts and independent review. Reference audit additionally requires linked verified observed/derived evidence and human UAT records. A passing manifest audit cannot prove the records are truthful; preserve actual tool logs and reviewer decisions.

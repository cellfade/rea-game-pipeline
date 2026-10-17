# Planning harness

Python 3.10+; standard library only. Run from package root:

```sh
python3 harness/pipeline.py init work/project
python3 harness/pipeline.py validate work/project/project.json
python3 harness/pipeline.py ready work/project/project.json
python3 harness/pipeline.py dispatch work/project/project.json investigate
python3 harness/pipeline.py audit work/project/project.json --level prototype
python3 harness/pipeline.py audit work/project/project.json --level reference
python3 harness/pipeline.py propose-improvement work/project/project.json failure-1
python3 harness/pipeline.py privacy release-directory
python3 -m unittest discover -s tests -v
```

All commands emit JSON: exit 0 passes, 1 means failed gates/findings, 2 means invalid input/operation. Dispatch is a data-only ticket; no agents, tools or shell commands launch, no state changes occur. Operator persists actual results. Init refuses overwrite.

## Contract

Init creates:

```json
{"schema_version":1,"max_workers":2,"tasks":[],"release_tasks":[],"evidence":[],"receipts":[],"reviews":[],"uat":[],"failures":[]}
```

Empty input passes planning validation but fails release audit. `release_tasks` must identify a nonempty milestone scope. Audit requires every scoped task and its dependency closure done. Future tasks outside this closure may remain planned.

Task: `id`, `depends_on` ID list, `allowed_files` relative literal paths/directories, `resources` exclusive names, `status` planned/active/review/done/blocked, `revision` lowercase SHA256 digest, `author`, `required_tests` test-name list, and reference-level `evidence_ids` list.

Paths are literal prefixes, not globs. Traversal/absolute/colon/backslash paths fail. Dot locks the project. Ready schedules in document order using completed dependencies, active locks, nonintersecting writes/resources, and max_workers residual capacity. It does not reserve tasks; apply state changes before requesting another batch. This is not a filesystem sandbox.

Evidence: `id`, `claim`, `status` observed/derived/inferred/proposed/unknown, `source: {identity, locator}`, `verified`, `reviewer`. Source identity should identify version/checksum and locator the precise observation. Reference claims require task-linked observed/derived evidence with `verified: true` and reviewer.

Receipt: `task_id`, `test`, `status` pass/fail/blocked, `revision`. Last matching revision receipt must pass each required test. Review: `task_id`, `author`, `reviewer`, `subject_digest`, `verdict: pass`. Reviewer differs from task author, author matches task, digest matches revision. Human UAT is separate: `task_id`, `revision`, `status: pass`, `reviewer`. Reference audits require UAT on each scoped task.

Failure: `id` plus reproduction/evidence fields. Improvement proposals remain candidates requiring reproduction, regression checks, independent review and human approval. No self modification.

## Limits

Digests and receipts are operator assertions. Harness checks consistency; it does not calculate artifact hashes or establish that tests ran, reviewers are independent people, or UAT happened. Preserve real review and test evidence. This is not an LLM runtime, deployment tool, emulator or security boundary.

Privacy checks common account paths, email/token/key patterns, risky artifact extensions, symlinks, and binary/large files. Values are redacted. It is heuristic, not certification; manual privacy, license and provenance reviews remain required. Scan clean staging without bytecode/cache artifacts.

### Audit hardening

Write paths must be canonical POSIX strings: `src/file` is accepted, while `./src/file`, repeated separators, trailing slashes and control characters are rejected. Active/review/done tasks require done prerequisites. Collection members are typed objects; evidence and failure IDs are unique. Review and UAT histories are append-ordered: the latest eligible result per reviewer governs, and any current failing/blocked eligible reviewer blocks the gate. Reference evidence reviewers and human UAT reviewers must differ from each task author. These are identity-label checks; no authentication of people or independence is provided.

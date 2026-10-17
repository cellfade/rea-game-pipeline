# REA Game Pipeline

Portable agent skills and a small, dependency-free planning harness for evidence-led game reverse engineering, original reconstruction, asset production and release review.

**Independent community workflow; not an official REA or Blender package.** Early release: record validation and synthetic evaluation are useful safeguards, not proof of an end-to-end game reconstruction.

## What it does

Turn a game question into a traceable chain:

**target → evidence → rule or design decision → task → test → review → human acceptance → release**

Use REA where the installed version supports the target. Use specialist emulators/disassemblers when console formats or hardware behavior require them. Build a new implementation with a separate gameplay simulation and renderer. Treat concept imagery, Blender scenes, exported models and browser-verified assets as different production states.

| Skill | Use it for |
|---|---|
| `rea-game-pipeline` | Scope the investigation, stage work and coordinate bounded workers |
| `rea-game-evidence` | Establish artifact identity, observations, hypotheses and rule provenance |
| `rea-game-assets` | Source/build decisions, concepts, Blender ownership and runtime asset proof |
| `rea-game-audit` | Independent technical, fidelity, privacy and release-readiness review |
| `rea-game-improve` | Failure-driven candidate changes with regression evaluation |

Each skill works independently. They use the Agent Skills folder format; client discovery and tool configuration still vary. No skill grants tools or permissions.

## Quick start

Requires Python 3.10+ for the optional harness; skills can be used without Python.

```sh
python3 harness/pipeline.py init work-project
python3 harness/pipeline.py validate work-project/project.json
python3 harness/pipeline.py ready work-project/project.json
```

Read [the harness contract](harness/README.md) before recording task/review results. `dispatch` emits a structured ticket for an actual agent coordinator; it does not start an LLM or tool process. `audit` validates supplied release evidence and fails closed on missing prerequisites. It cannot authenticate claims made by a dishonest recorder.

Install skills into a directory selected for your client:

```sh
python3 scripts/install_skills.py --dest ./local-skills --dry-run
python3 scripts/install_skills.py --dest ./local-skills
```

No automatic client configuration edits, downloads, paid services or API keys. The installer refuses conflicting existing folders. For agent-specific discovery and optional tool setup, see [adapters](docs/adapters.md).

## Workflow and evaluations

- [Workflow and stage gates](docs/workflow.md)
- [Orchestration and ownership](docs/orchestration.md)
- [Bounded improvement loop](docs/improvement.md)
- [Ecosystem and recommended tools](docs/ecosystem.md)
- [Public/private separation](docs/privacy-publication.md)
- [Behavioral evaluation scenarios](evals/scenarios.json)
- [Validation record](docs/validation.md)

Run package checks:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_package.py
python3 harness/pipeline.py privacy .
```

The privacy scanner is heuristic. Review prompts, traces, archives, images and full Git history manually before publishing. Do not commit original game artifacts or production credentials.

## Public package and private projects

This repository contains generic skills, code, documentation and synthetic examples only. Create project manifests, local tool paths, approved artifact identities and private reference captures in a separate project directory. A `.local/` overlay is ignored but must still be checked before release; `.gitignore` alone is not a privacy guarantee.

Do not copy personal client configuration into templates. The example overlay contains field names only and is not read or executed by the harness.

## License

[MIT](LICENSE) for this package's original code, skills and documentation. Referenced tools, game code/assets, model downloads and third-party material keep their own terms. No game or external tool license is granted by this package. See [third-party boundaries](THIRD_PARTY.md).

# Ecosystem and recommended skills

Research date: 2026-10-16. These are recommendations, not a claim that the tools have been installed or tested together. Verify versions, license files, and compatibility at the commit actually adopted.

## Tool choices

| Component | Purpose and when to use | License evidence | Limits and verification needed |
| --- | --- | --- | --- |
| [REA](https://github.com/morluto/rea) | Evidence-oriented inspection of supported binaries, applications, managed code, JavaScript, and browser targets | Upstream identifies REA-authored code as MIT; third-party notices remain applicable | No verified general SNES ROM analysis lane is asserted here. Test a concrete question before depending on a provider. Commercial analysis engines require separate entitlement. |
| [Agent Skills specification](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx) | Portable instruction folders with YAML metadata, references, and scripts | [Repository](https://github.com/agentskills/agentskills) identifies code as Apache-2.0 and documentation as CC-BY-4.0 | Follow the format; write original instructions. Format compatibility does not guarantee client discovery, permission behavior, or MCP registration. |
| [Blender Lab MCP](https://www.blender.org/lab/mcp-server/) | Blender-hosted experimental scene/API workflow; preferred baseline when its capabilities fit | [Source](https://projects.blender.org/lab/blender_mcp); license text could not be retrieved during this review, so license remains unverified here | Pin the exact source and matching extension/server. Do not substitute a similarly named package. Treat Python execution as execution with host permissions. Verify export and browser import separately. |
| [MCP for Blender](https://github.com/ahujasid/mcp-for-blender) | Community alternative with modeling, material, inspection, and optional external asset services | Repository identifies MIT | Explicitly unaffiliated with Blender Foundation. Server/add-on pairing differs from Lab. Optional cloud services and asset licenses require their own review. |
| [Mesen2](https://github.com/SourMesen/Mesen2) | Emulator/debugging option for repeatable SNES observation and focused runtime investigation | [GPL version 3 license text](https://raw.githubusercontent.com/SourMesen/Mesen2/master/LICENSE) | Pin emulator/core/settings/input sequence. Platform availability and automated capture integration need local testing. Emulator license does not license game contents. |
| [DiztinGUIsh](https://github.com/DizTools/DiztinGUIsh) | SNES disassembly and annotation; useful alongside runtime evidence | [GPL version 3 license text](https://raw.githubusercontent.com/DizTools/DiztinGUIsh/master/LICENSE.md) | Code/data boundaries and processor state require care. A sparse annotation project is not complete recovered source. Export/rebuild support must be demonstrated on the selected revision. |
| [bsnes](https://github.com/bsnes-emu/bsnes) | Secondary emulator for cross-checking observations | License not independently verified in this review | Debug/trace support differs by build; inspect the exact distribution. Do not assume traces interoperate with another tool without a fixture. |
| [glTF Validator](https://github.com/KhronosGroup/glTF-Validator) | Structural validation of glTF/GLB asset exports | [Apache-2.0 license](https://raw.githubusercontent.com/KhronosGroup/glTF-Validator/main/LICENSE) | A valid file still needs scale, pivot, material, animation, visual, and performance checks in the actual renderer. |
| [Playwright](https://github.com/microsoft/playwright) | Browser scenario tests, screenshots, traces, input flows | [Apache-2.0 license](https://raw.githubusercontent.com/microsoft/playwright/main/LICENSE) | Browser automation cannot establish game fidelity alone. Use assertions on gameplay state and independent human UAT. |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Optional second-layer secret detection for release candidates and history | Inspect its license at the pinned version before redistribution | Pattern scanning does not prove privacy or identify all confidential prose, image metadata, assets, or model traces. |

The MIT license of this pipeline covers its original implementation and instructions. It does not relicense any referenced tool, target artifact, extracted code, screenshot, music, model, or game brand. Tools are external dependencies, not bundled vendor skills.

## Skill composition

Required workflow responsibilities, whether implemented as dedicated skills or explicit task contracts:

1. **Pipeline orchestration:** scope, dependency graph, worker ownership, checkpoints, budget, stop conditions, and independent reviewers.
2. **Evidence investigation:** artifact identity, bounded questions, reproducible capture, claim IDs, confidence, limitations, and alternate explanations.
3. **Behavior specification:** convert observations into testable rules; keep original observations separate from deliberate redesign choices.
4. **Validation and release:** deterministic scenarios, regression evidence, human UAT, license/provenance/privacy audit, and deployment readback.
5. **Improvement review:** failure records, proposed workflow changes, regression fixtures, and reviewed promotion; never silently rewrite acceptance criteria to pass.

Optional specializations: creative direction/concept generation, Blender asset production, source-asset sourcing, performance profiling, emulator-specific investigation, and accessibility review. Use a source asset only after its per-item license and attribution requirements are recorded. Generated concept art is design input, not evidence of original gameplay or a production-ready mesh.

Instructions and tool setup are distinct. A skill cannot supply a missing ROM, MCP server, authorized analysis engine, Blender extension, renderer, or deployment credential. Maintain a capability matrix with `documented`, `configured`, `connected`, `operation-tested`, and `workflow-tested` states. Record which state was actually achieved for each client and tool.

## Adoption order

Start with synthetic fixtures and one measurable mechanic. Prove observation → specification → implementation → scenario comparison before broad reconstruction. Add Blender only when a concrete asset contract exists; prove one GLB through validation and browser import. Expand autonomy after repeated successful release gates, not because additional agents are available.

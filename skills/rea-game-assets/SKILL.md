---
license: MIT
name: rea-game-assets
description: "Plan, source, generate, and validate original or licensed game assets through concept art, Blender, and engine integration. Use for reconstruction asset pipelines, provenance, and production readiness."
---

# REA game assets

Make assets support a playable reconstruction without confusing visual proposals with verified game behavior. Establish camera distance, silhouette/readability needs, reference sources, art direction, target engine, delivery format, and measurable per-asset/render budgets before detailed production.

Search suitable licensed assets when useful; record source URL, author, exact license/version, attribution, permitted modifications and redistribution, acquisition date, and local changes. Verify the actual asset license, not a directory's marketing copy. Unknown licensing blocks public redistribution, not unrelated experimentation. Prefer original replacements when rights remain unclear. MIT licensing of a pipeline does not relicense models, textures, fonts, sounds, or reference art.

Use image generation for alternate concepts, material studies, and composition where available. Record model/tool when exposed, prompt, reference provenance, generation date, selection rationale, and edits; do not claim seed reproducibility if unavailable. Label concept imagery and mock gameplay clearly. Reconcile inconsistent generated views before modeling; never treat an attractive image as a geometrically complete specification.

For Blender production, inspect the current scene and MCP capabilities first. A listed tool does not prove it works. Use one scene owner at a time or isolated .blend files, checkpoint before destructive edits, and restrict generated Python to the agreed scene/task. Verify units, axes, origin, scale, topology, UVs, normals, material compatibility, animation names, and required LOD/collision geometry. If MCP is unavailable, use a supported local Blender CLI or write a reproducible handoff; do not report a render or export that was only planned.

Export the agreed engine format and inspect it in the actual engine/browser. Check silhouette at gameplay scale, dimensions, lighting, animation, missing textures, draw calls, memory and frame-time against declared budgets. A Blender render cannot prove browser compatibility. Produce a source scene, exported asset, inspection capture, provenance entry, and acceptance result; distinguish concept-ready, model-ready, exported, integrated, and accepted states.

Keep private prompts/reference captures, credentials, account details, and local identifying paths outside public packages. Publish only reviewed redistributable assets and sanitized metadata within existing authorization. Use a caller-selected checkout for asset records or an optional external harness. This skill installs no tools and does not authorize cloud spending or downloads requiring new permissions.

Read [evaluation scenarios](references/scenarios.md) when evaluating the production handoff.

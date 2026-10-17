# Client adapters and optional tools

All five skill folders are self-contained Agent Skills entries. Discovery paths and reload behavior belong to the current client's documentation; select an explicit destination instead of assuming a global directory is shared by every agent.

| Environment | Instructions | Tool access |
|---|---|---|
| Codex | Install into a configured skill directory; optional agents/openai.yaml provides UI metadata | Register compatible MCP services separately, restart/reconnect and perform a real read-only call |
| Claude Code | Install into the client's supported personal or project skill directory | Its own MCP configuration and permission model applies |
| Cursor | Use supported skill/rule discovery or load SKILL.md as project guidance | Configure its own MCP server entries and verify actual calls |
| Hermes | Use supported skill catalog/directory or explicitly load the skill | Confirm installed Hermes version supports the intended integration; transport discovery is separate from a successful model-driven turn |
| Other LLM agents | Load the relevant SKILL.md and references as ordinary instructions | Use equivalent CLI/manual tools; serial roles remain valid when delegation is absent |

This is an adaptation guide, not a claim of live interoperability tests across all clients. No package installer edits client config, replaces upstream REA skills or adds tools.

## Capability verification ladder

Documented → installed → configured → connected → operation-tested → workflow-tested. Record each tool/client separately. MCP tool listing does not prove scene editing, export, browser import or persistence. A local scene query does not establish all Blender Python operations or GPU rendering.

Prefer upstream REA setup instructions and actual connected tool schemas. Keep the installed upstream reverse-engineering skill; this suite adds game-specific coordination rather than duplicating its tool catalog. For Blender, select and pin one integration with a matching extension/server, bind local bridges to loopback and serialize scene owners. Verify one original GLB in the actual target renderer before scaling production.

No API keys, local executable paths, hostnames or deployment account identifiers belong in the public skill. Keep actual values in a private project overlay selected by the operator. The included overlay example is documentation only; the harness never loads it or changes permissions from it.

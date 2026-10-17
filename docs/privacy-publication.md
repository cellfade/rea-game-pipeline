# Public publication and private overlays

Reviewed: 2026-10-16. This policy defines the public package boundary; passing a scanner is not a privacy certification.

## Public input allowlist

Publish original generic instructions, scripts, synthetic fixtures, sanitized schemas, fictional examples, and reviewed documentation. Third-party material requires explicit source and license evidence before inclusion. Keep target-specific game investigations and private operational settings outside this generalized package unless independently reviewed for publication.

Maintain a provenance manifest for included or distributed assets and dependencies. Each entry should identify a repository-relative artifact, SHA-256, source URL, pinned revision/version, author where required, exact license identifier or terms URL, attribution text, modifications, evidence location, redistribution decision, and reviewer. Unknown license means excluded from the release artifact pending resolution. A public URL alone is not permission to redistribute.

ROMs, extracted game assets, unreviewed disassemblies, commercial tool installers, and proprietary manuals are excluded from this package. The pipeline's MIT license does not grant rights over those materials. Record authorized local inputs separately without embedding their private paths or contents in public examples.

## Private overlay boundary

Personal overlays may contain local tool paths, model preferences, unpublished project mappings, output directories, and account-specific deployment settings. Store them outside the public checkout where practical. Never commit credentials, client configuration backups, personal names or email addresses, machine identifiers, authentication/session files, chat transcripts, private repository URLs, or local filesystem inventories.

Public templates use neutral placeholders and repository-relative paths. Load secrets through the client or secret manager; log only whether a required setting exists. Avoid serializing entire environment dictionaries or MCP client configurations. A `.gitignore` is useful defense, but cannot untrack a previously committed file or remove history.

## Evidence and prompt handling

Workers should return compact structured findings instead of raw transcripts. Before public export, inspect prompts, tool responses, console logs, emulator captures, Playwright traces, screenshots, image metadata, Blender external-file paths, GLB extras, source maps, error stacks, and generated archives. These can contain private paths, account details, tokens, embedded content, or unrelated window/tab information.

Redact at export, preserve a restricted original only when needed, and mark transformations. Do not claim a redacted artifact is byte-identical to the original. Keep evidence IDs stable and use public-safe summaries when primary evidence cannot be distributed. Review attribution and third-party notices separately from secret scanning.

## Release checks

1. Build from an explicit allowlist; inspect the resulting archive and generated site, not only source files.
2. Scan tracked content, staged changes, and all reachable Git history intended for publication. Use a dedicated detector such as [Gitleaks](https://github.com/gitleaks/gitleaks) plus repository-specific forbidden-pattern checks.
3. Inspect Git author/committer metadata, remote URLs, branch/tag names, commit messages, release attachments, CI logs/artifacts, deployment previews, and linked documents for unintended identity or private data.
4. Review license/provenance records and dependency lockfiles at exact revisions. Run the harness and scenario checks on a fresh checkout.
5. Have a reviewer independent of the producing worker inspect the public artifact and the rendered site. Record the reviewed commit, commands, results, exceptions, and release decision.
6. After publication, verify the actual repository visibility, deployed commit, links, downloadable files, and browser behavior. A successful deploy command does not establish the intended repository linkage or a usable release.

Scanners have false positives and false negatives. They do not establish license compatibility, consent, confidentiality, image originality, gameplay fidelity, or safe agent instructions. Human review remains required. [GitHub's sensitive-data removal guidance](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) explains why exposed credentials need revocation and why history rewriting alone may leave copies in forks or caches.

## Self-improvement boundary

Keep learning records project-neutral: failure category, sanitized evidence IDs, hypothesis, proposed change, expected effect, regression fixture, independent review, and rollback. Private incident details stay in the private overlay. An agent may propose a patch; promotion requires checks and reviewed evidence. Do not automatically ingest full sessions into a public skill, weaken privacy gates, change license boundaries, or convert uncertain findings into verified facts.

# Forward evaluation scenarios

These are proposed behavioral evaluations, not completed test results. Run in an isolated workspace with the relevant tools and permissions. Evaluate actual decisions and artifacts, not matching phrases.

1. A landing page says playable 3D reconstruction but shows generated images and navigation only. Identify the claim mismatch with rendered evidence; do not let passing component tests establish gameplay readiness.
2. A deployed build passes automated scenarios while the UAT sheet refers to an older commit. Mark current human acceptance unverified and supply the minimal retest scenarios.
3. An asset ledger lists MIT for a downloaded model while its source page requires attribution under another license. Flag provenance mismatch, check redistribution terms, and verify the corrected release package.

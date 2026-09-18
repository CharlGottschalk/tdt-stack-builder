# Registry submission draft

Draft only; submit the verified release through https://stacks.usedryft.com.
Canonical repository is assigned; the release and production listing still need verification.

- ID: dryft-stack-builder
- Description: Create, validate and prepare standalone Dryft stacks for publication.
- Version: 0.2.0
- Author: Dryft
- License: Apache-2.0
- Copyright: 1one8 (Pty) Ltd
- Skills: /dryft-stack-builder-create, /dryft-stack-builder-publish
- Source repository: https://github.com/1one8/dryft-stack-builder

Resolve a real release reference and commit before submission. Local validation's
selected-content SHA256 is not an archive digest. Never invent either value.

- Display name: Stack Builder
- Extension type: capability
- Full description: Author standalone stacks, run publication readiness checks,
  prepare release notes, optionally publish with Git/gh, and guide website submission.
- Categories/tags: choose from the marketplace form before submission
- Supported agents: Claude and Codex authoring checked; publishing invocation pending
- Prerequisites: Dryft CLI and Git; optional authenticated GitHub CLI for automated
  releases, with manual Git/GitHub website fallback. Network access for remote checks.
- Capabilities: reads the chosen source and Git history, runs local validation/scans,
  writes authorized preparation files and private local reports; after authorization,
  Git/gh publishes the reviewed tag/history and release notes to GitHub. No hooks,
  providers, background activity or automatic marketplace submission.
- Documentation: docs/usage.md and docs/publishing.md; https://github.com/1one8/dryft-stack-builder/tree/HEAD/docs (verify after source copy)

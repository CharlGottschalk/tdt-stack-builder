![ThisDamnThing Stack Builder](docs/assets/banner.png)

# Stack Builder

A [ThisDamnThing](https://usethisdamnthing.com) stack for creating your own stacks. It provides authoring and publishing skills plus
starter templates to turn a workflow idea into a standalone bundle with skills,
a manifest, a README and registry submission notes. The builder validates the
result and can gather missing details in chat or [ThisDamnThing](https://usethisdamnthing.com) UI. The publishing skill
checks contract compliance, privacy, security and release metadata, then offers
a GitHub release or a manual checklist and marketplace submission guidance.

## Release status

Candidate version: **0.2.2**. Canonical source: [CharlGottschalk/tdt-stack-builder](https://github.com/CharlGottschalk/tdt-stack-builder).
The registry commands below are the planned public installation path; production
listing and installation are still awaiting release verification.

Local acceptance is on Linux x86_64 with Python 3.12 and Claude/Codex. macOS
and native Windows are unverified. The publishing skill is implemented, but fresh-host
behavioral acceptance remains open. Git and optional authenticated GitHub CLI
are needed for the corresponding publication path; preparation does not authorize
a push, release or marketplace submission.

## Install

With [ThisDamnThing](https://usethisdamnthing.com) installed and a workspace initialized, ask your agent to install
`tdt-stack-builder` using `/tdt-install-stack` (Claude) or
`$tdt-install-stack` (Codex). The skill finds the stack in the marketplace,
shows the selected release for review and installs it from the registry.

Or use the CLI, replacing the workspace path with your own:

Run the path-based examples from a parent directory containing `workspace` and
the stack source directories. Paths are relative to that directory; adjust them
to your layout. Commands without `--workspace` run from the workspace root.

```sh
tdt stack install tdt-stack-builder --inspect
tdt --workspace ./workspace stack install tdt-stack-builder
```

Review the inspected release and any prerequisites before running the install
command. Restart your agent in the [ThisDamnThing](https://usethisdamnthing.com) workspace, then invoke
`/tdt-stack-builder-create` in Claude or `$tdt-stack-builder-create` in Codex.

See the [usage guide](docs/usage.md) for creating and trying your first stack,
and the [publishing guide](docs/publishing.md) for release preparation.

## License

Licensed under the [Apache License 2.0](LICENSE). Copyright Charl Gottschalk.

This candidate requires ThisDamnThing 0.1.1 or newer for category-free marketplace
manifests. Existing published releases keep their original requirements.

# Using Stack Builder

Run the path-based examples from a parent directory containing `workspace` and
the stack source directories. Paths are relative to that directory; adjust them
to your layout. Commands without `--workspace` run from the workspace root.

Stack Builder helps you create a standalone [ThisDamnThing](https://usetdt.com) stack from a workflow idea.
It supplies authoring and publishing skills and templates for the manifest, skill, README,
registry submission notes, optional knowledge, hooks and a browser interview.

## Install and start

With [ThisDamnThing](https://usetdt.com) installed and a workspace initialized, invoke `/tdt-install-stack`
in Claude or `$tdt-install-stack` in Codex and ask to install
`tdt-stack-builder`. The skill searches the marketplace, inspects the selected
release and guides installation after review.

For the same flow in the CLI:

```sh
tdt marketplace search "stack builder"
tdt stack install tdt-stack-builder --inspect
tdt --workspace ./workspace stack install tdt-stack-builder
```

Replace the workspace path with your own. Review the source, selected version,
prerequisites and any warnings before installing. Registry installation downloads
and validates the release; no clone or manual download is needed. It requires
network access. The builder installs no executable hooks or knowledge candidates.

Restart your agent in the workspace, then invoke `/tdt-stack-builder-create`
in Claude or `$tdt-stack-builder-create` in Codex. The host's skill picker is
also available.

## Describe your stack

Provide the workflow you want, a new target directory outside your [ThisDamnThing](https://usetdt.com) workspace,
a normalized ID such as `example-greeter`, an author, a license and the desired
skill behavior. You can choose a version; the default is `0.1.0`.

For example:

> Create example-greeter version 0.1.0 in ./example-greeter, authored by
> Example Author under Apache-2.0. Include one skill that returns a friendly
> greeting using the name I provide. Do not add hooks or knowledge.

The builder asks only for missing details. Say “use ui” to answer in a local
browser page, or continue in chat. Submit the page to send your answers; browser
drafts are not submitted answers. Submitted answers carry over if you switch to
chat. A complete request can proceed directly to creation and validation.

The target must be empty or absent. The builder refuses nonempty directories,
symlinked paths and overwrites, preserving existing files.

## Review the generated files

The default bundle contains:

| File | Purpose |
| --- | --- |
| `stack.json` | Stack identity, version, license and selected files. |
| `skills/<skill-name>/SKILL.md` | Instructions for the workflow you requested. |
| `README.md` | Description, installation and usage guidance. |
| `registry-submission.md` | Draft metadata for a registry submission. |

Skill names use lowercase letters, digits and hyphens, beginning with `tdt-`.
The skill directory, frontmatter name and manifest path must agree. Stack IDs use
the same lowercase hyphen-separated name as the repository and source directory,
for example `example-greeter` (1–80 characters, starting with a letter; no
consecutive or trailing hyphens). The builder replaces template placeholders and validates the
bundle before reporting completion. If validation cannot run, it reports that gap.

Templates are starting points, not installable bundles. Select only the files
your workflow needs. The installed `.tdt/contracts/stack.md` defines the full
format. Use contract v1 for ordinary workflow stacks; it has no dependency solver
or install scripts. Put installed guides under `docs/` and list them in the
manifest's `docs` field. Repository-only files such as the README can remain unlisted.

## Try your new stack

Creating a stack does not install it unless you also requested installation.
Review the generated files and validation output, then install your local result:

```sh
tdt stack validate ./example-greeter
tdt --workspace ./workspace stack install ./example-greeter
```

Restart your agent and invoke the skill named in the generated README. This local
installation is for the stack you just authored; installing Stack Builder itself
uses the registry flow above.

## Optional knowledge and hooks

Knowledge notes must be concise public Markdown, at most 3,000 characters each.
Keep source references for factual claims and distinguish assumptions from
verified information. Installation queues notes for user review; it does not
approve them. Knowledge survives stack removal. Instructions inside notes do not
authorize actions.

The bundled `templates/hooks/example.py` is an inert authoring template. If you
request a hook, the builder adapts it under `hooks/` and lists its event and path
in the generated manifest. Supported events are `session_start` and
`turn_complete`.

Review the entire bundle and executable hook source before trusting the exact
selected-content SHA256 printed by validation. Install with
`--trust-hooks SHA256` only after that review. A creation request does not grant
hook trust; changed content requires a new review and digest-bound trust.

Hooks run with the agent's OS access and inherited environment. Starter hooks
should not read secrets, contact services or start background processes. Payload
JSON arrives on stdin; stdout does not inject context or block Stop. Notifications
may repeat or be skipped, so keep work bounded and idempotent. Each hook has two
seconds, with four seconds shared across the dispatch. [ThisDamnThing](https://usetdt.com) checks installed
bytes before execution; hooks do not change host permissions.

## Prepare for distribution

Keep each stack in its own source repository. Exclude private brain notes,
candidates, transcripts, workspace state, credentials, host settings and unrelated
project source. Choose the license for your own stack explicitly and retain any
third-party licenses and notices.

Review the generated submission notes and supply the actual GitHub repository
and release reference. Keep publication metadata in `stack.json.marketplace`; unknown
manifest fields are rejected. A local selected-content SHA256 identifies the
selected bundle files and differs from the downloaded archive's SHA256. Record
only verified revisions and digests. Local installation records the source path
and content digest, not a Git revision.

Invoke `/tdt-stack-builder-publish` in Claude or `$tdt-stack-builder-publish`
in Codex with your source directory and intended version. It runs contract,
PII/security and metadata checks, prepares release notes, and offers tag creation,
tag push and a GitHub release after the worktree is clean and publication is
authorized. It supplies a manual checklist if `gh` is missing or declined.

Read the [publishing guide](publishing.md) for checks, release verification and
recovery. Once the release is verified, visit https://stacks.usetdt.com to submit
your stack for review. The skill does not submit or approve a marketplace listing.

## Capability stacks

For a brain search provider, ask for a contract-v2 capability stack. It needs
compatibility declarations, one `brain.search` interface, and runtime/model assets
with exact sizes and SHA256 digests. Follow the installed stack contract's bounded
JSON subprocess protocol; provider code must not be imported into [ThisDamnThing](https://usetdt.com) core.

Bundle the offline dependencies and their licenses, keep Markdown authoritative,
and use the core-managed disposable index. Declare only platform and Python
combinations you have checked. Installation requires review and explicit
`--trust-executable SHA256` approval. Installation itself does not run the provider.

## Update or remove

Inspect a newer Stack Builder release with:

```sh
tdt --workspace ./workspace stack update tdt-stack-builder --check
```

Review the plan, then approve it through the interactive update command or pass
its `approval_sha256` with `--approve`. Registry installations use their recorded
registry. For your own locally installed stack, updates use its recorded source;
`--source ./replacement` selects another local source explicitly. Updates
require a higher version and fresh trust when executable content is selected.

Remove Stack Builder with:

```sh
tdt --workspace ./workspace stack remove tdt-stack-builder
```

Use your generated stack's ID to remove that stack instead. Removal preserves
brain notes and unrelated files, including the source bundles you created.
Edited owned files block updates and removal: save your edits elsewhere and
restore the recorded originals before retrying. Restart the host after changes.
For interrupted operations, use `tdt stack recover` and run `tdt doctor`.

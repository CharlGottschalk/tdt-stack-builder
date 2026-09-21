# Publishing a stack

Run the path-based examples from a parent directory containing `workspace` and
the stack source directories. Paths are relative to that directory; adjust them
to your layout. Commands without `--workspace` run from the workspace root.

Invoke `/tdt-stack-builder-publish` in Claude or
`$tdt-stack-builder-publish` in Codex with the source directory and intended
version. The skill prepares a release, runs checks, and offers GitHub publication
when ready. You can choose manual publication instead. Neither path submits the
stack to the marketplace automatically.

## Record the candidate

Use one stack at a Git repository root. Record the canonical GitHub repository,
manifest ID/version, intended tag (`X.Y.Z` or `vX.Y.Z`), full commit SHA and [ThisDamnThing](https://usethisdamnthing.com)
selected-content SHA256. A tag must equal the manifest version after removing at
most one leading `v`. Never infer identity, license, destination or compatibility.
Inspect existing local and remote tags/releases before proposing a new version.

Run `git status --porcelain=v1 --untracked-files=all` from the repository root;
include staged, unstaged, untracked and submodule changes. Inspect ignored selected
files too: a clean status does not prove release completeness. An unborn/shallow
repository, unavailable remote or unreadable history needs an explicit coverage
resolution before release, not an assumed pass. Keep private scan reports outside
the repository. Changes to files, commit, notes or tag message invalidate affected
review evidence. Record commands, tool versions, scope, exit results and limitations.

## Three readiness checks

### 1. Contract and packaged files

Run `tdt stack validate ./stack` and inspect the actual output. Use the
installed `.tdt/contracts/stack.md`, including its v2 additions when applicable.
Confirm the manifest ID, source directory and repository name use the same
normalized lowercase hyphen-separated name (for example `tdt-search-sqlite`).
A display title can remain human-readable. After a rename, publish a commit whose
manifest contains the new ID and regenerate registry identities and digests;
renaming the GitHub repository alone does not change an older release archive.
Check required fields, numeric version, names/frontmatter, explicit file lists,
hooks, docs, knowledge, safe paths, limits and v2 compatibility/asset hashes. Declare publication metadata in the `marketplace` object in `stack.json`. CLI absence or unsupported contract is incomplete.

Validate an isolated archive of the exact candidate commit too, not only the
working directory. Inspect archive entries before extraction; reject traversal,
symlinks, special files and collisions. Check all selected files are present and
byte-identical, including runtime/model binaries. Review `.gitattributes`, ignored
files, Git LFS pointers and submodules: source archives may omit content or carry
pointers. A separately attached release asset does not repair the marketplace's
commit-source archive. Resolve missing content before publication.

Check installed documentation and skill references using only manifest-selected
files laid out as `.tdt/stacks/<id>/` and projected skills; core contract/skill
references resolve from the workspace. Source-only links do not count as installed
coverage. This can be a disposable layout check without executing hooks/providers.
Record real host/platform checks separately from static validation; do not invent
compatibility evidence or require every unrelated local stack to be installed.

### 2. PII, secrets and security

Scan the complete proposed public tree/archive, reachable history (including
commit/tag messages and identity metadata), release notes and proposed attachments.
The selected bundle digest does not cover all of this. Deleted secrets in history
remain exposed by a tag push. Scan author metadata with context: an intentional
public attribution is not automatically a private-data finding.

Run local, non-executing searches with `rg` or an equivalent scanner for credential
assignments/tokens, private keys, credential-bearing URLs, emails, personal absolute
paths, private hosts/IPs and copied brain notes, transcripts, caches, `.env` files
or host configuration. Search filenames and contents; include hidden tracked files
and history, with NUL-safe file enumeration. Use installed secret scanners in
redacted, offline/non-verifying mode if available; inspect their help/version and
coverage rather than assuming their defaults scan history. Do not upload source,
print matched secrets into chat, read unrelated credential stores, or test tokens.
A tool's absence alone does not block equivalent local scanning plus review, but
unscanned content, tool errors or truncated results are incomplete. Regex matches
need contextual review; a zero-match search alone is not a pass.

Read every selected skill, hook/provider, script, template and relevant packaging/
automation file for instruction injection, hidden execution, unsafe shell/path
handling, credential access, network/exfiltration, destructive actions and incorrect
permission claims. Review generated instructions as behavior, even with no code.
Assess bundled binaries/dependencies using provenance, hashes, licenses and available
local security evidence; document unsupported/uninspected components as incomplete.
Never execute candidate hooks, providers, build scripts or repository automation
just to scan. Any dynamic check needs an authorized disposable environment without
production credentials. Inspect release-triggered workflows before offering a push.

Report redacted locations, category, impact and fix. Distinguish confirmed findings,
false positives and intentionally public information with reasons. Unresolved
findings block readiness; do not silently waive them or treat them as success.
Exposed credentials need owner-led revocation/remediation, not just deletion from
HEAD. Do not rewrite history automatically. A pass describes completed static and
agent review, not proof of universal safety or install-time executable trust.

### 3. Repository and marketplace metadata

Check root `stack.json`, a usable README/installation/usage guide, license text
consistent with the declared license, and required third-party notices/licenses.
A NOTICE file is required only when applicable. Check required selected files and
resolved documentation links. A changelog is useful, not a universal contract
requirement. `registry-submission.md` is a convenient draft, not a required manifest
field or mandatory marketplace filename.

The form collects only a name, GitHub URL and description. Put the remaining
publication metadata in `stack.json.marketplace`: extension type
(`functionality`, `capability`, `both`),
site-supported categories, lowercase tags, supported agents, prerequisites and
capability/data-flow disclosures. Record required/optional dependencies, purpose,
setup links, version constraints, authentication and payment needs without secrets.
Disclose reads/writes, process/network/connector access, data leaving the machine
(or none), exact hooks and v2 providers/platform/Python limits. Optional media need
HTTPS URLs and alt text. Do not fabricate categories, tested hosts or author control.
Use the current website form for submission requirements; do not invent an API.

Resolve placeholders in release metadata, notes and user-facing setup instructions.
Intentional placeholders inside reusable templates/examples are valid when clearly
marked and the generating workflow replaces them. Confirm repository control and
public visibility without changing visibility automatically. Repository availability
can be checked in the browser when `gh` is unavailable. Unknown access is incomplete.

For a new release, separate local readiness from pending post-publication checks.
The absent new release itself is expected. Existing tags must peel to the checked
commit; a same-name tag at another commit blocks publication. Existing published
versions cannot be overwritten. Draft/prerelease releases are not marketplace
eligible. Local readiness does not mean the remote archive has been verified.

## Optional GitHub CLI publication

After readiness passes, check `gh --version`, authentication without exposing
tokens, and repository access. Prepare exact tag/release messages and notes in
private temporary files. Present the repository, commit, version/tag and notes for
the user's publication choice. Tag creation and push use Git; `gh` creates the
release. Fill variables from verified values using safe argument passing; never
paste untrusted metadata into shell code. Review configured Git hooks before
mutation; do not bypass safeguards or execute unexpected hooks implicitly.

For a new tag, the command shape is:

```sh
git tag -a "$release_tag" "$checked_commit" -F "$tag_message_file"
git push "$verified_remote" "refs/tags/$release_tag:refs/tags/$release_tag"
gh release create "$release_tag" --repo "$github_repo" --verify-tag \
  --title "$release_title" --notes-file "$release_notes_file"
```

Run each step only after the preceding step succeeds. Immediately beforehand,
recheck the whole worktree is clean, HEAD is the reviewed commit, selected bytes
match the recorded digest, and remote/tag/release state still agrees. Push only
the exact tag; do not push all branches/tags or force. After push, independently
resolve the remote tag (peeling annotated tags) to the checked commit before
creating the release. `--verify-tag` checks existence, not commit equality. Never
let `gh` create a tag implicitly on a default branch. Publish a regular release,
not a draft or prerelease. GitHub CLI reference:
[release create](https://cli.github.com/manual/gh_release_create).

If a step fails or its outcome is uncertain, reread remote state before retrying.
Keep a correct local tag after a failed push. Reuse a correct remote tag after a
failed release. Reuse a matching published release instead of creating a duplicate;
check its notes/content too. Existing drafts need review and authorization before
publishing. Do not replace tags/releases or delete successful publication to undo
a later verification failure. Report the last confirmed state and pending action.

## Verify the published release

Confirm canonical public repository, published non-draft/non-prerelease release,
version/tag agreement and independently resolved full commit. Fetch the immutable
archive from `https://codeload.github.com/<owner>/<repo>/zip/<commit>` without
credentials, using HTTPS and only the intended codeload host for redirects.
Bound requests to 30 seconds, compressed bytes to 384 MiB, expanded bytes to
512 MiB and entries to 12,000. Before extraction require one top-level directory
with root `stack.json`; reject unsafe paths, symlinks, special/encrypted entries,
duplicates and nesting beyond 20 components. Reuse available [ThisDamnThing](https://usethisdamnthing.com) archive
validation rather than extracting unchecked ZIPs.

Hash the actual downloaded ZIP with SHA256, validate its safely extracted root,
and compare manifest identity and selected-content digest with the reviewed
candidate. Check the complete archive matches the reviewed public content;
export substitutions or LFS expansion require review of their actual bytes.
Archive SHA256 and selected-content SHA256 are different evidence: never substitute
one for the other or use a locally built ZIP's hash as the GitHub archive hash.
Missing/changed assets or a network/verification failure leaves the release
unverified and blocks a ready-for-submission claim. Do not use another transport
or attached asset as a silent fallback. Record the real release URL and verified
values outside the committed tree to avoid a self-referential digest update.

## Manual checklist and marketplace handoff

When `gh` is absent, unavailable or declined, deliver a tailored checklist. Fill
known values and mark unknowns and failed checks; do not present blockers as done.

- [ ] Resolve reported contract, privacy/security and metadata findings. Complete
  required scans and local archive validation; retain redacted evidence.
- [ ] Review intended files and commit them using your normal safeguards. Rerun
  checks on the resulting commit; confirm the entire worktree is clean.
- [ ] Confirm the public GitHub destination and your access. Prepare the agreed
  version, exact commit, tag message and release notes; check existing versions.
- [ ] Create the annotated tag at that exact checked commit and push only that
  tag using the Git commands above, with concrete safely quoted values supplied
  by the agent. Tag push exposes reachable history. Never move an existing tag.
- [ ] In the repository's GitHub Releases page, create a release using the
  existing pushed tag. Paste the prepared title/notes and publish a normal
  release with draft/prerelease disabled. Reuse an existing matching release.
- [ ] Complete the public release/archive verification above; record the release
  URL, full commit and both verified SHA256 values. Ask the agent to help verify
  when tools are available; skipped checks remain pending.
- [ ] Visit [the ThisDamnThing marketplace](https://stacks.usethisdamnthing.com), register/sign in
  as needed, and submit your repository and release with the prepared listing
  information. Follow the website's repository-control and review steps. If the
  site is unavailable, retain the checklist and retry later; do not claim submission.

End with that marketplace reminder in both automated and manual paths. The author
submits through the site; publication alone does not create an approved listing.
Each new version requires review. Only report submitted/approved if independently
observed or explicitly attributed to the author, never inferred from release success.

# {{title}}

Run the path-based examples from a parent directory containing `workspace` and
the stack source directories. Paths are relative to that directory; adjust them
to your layout. Commands without `--workspace` run from the workspace root.

{{description}}

Author: {{author}}
License: {{license}}

```sh
dryft stack validate ./{{id}}
dryft --workspace ./workspace stack install ./{{id}}
```

Review validation output before installation. If this stack selects executable
hooks, review the code and explicitly trust its selected-content SHA256 with
--trust-hooks <SHA256>. Hooks execute with the host's OS access, not in a sandbox.
Knowledge files enter pending review; installation does not approve them.

Restart the host and use /{{skill_name}}. Codex may require ${{skill_name}} or its
skill picker. {{usage_example}}

Keep this stack in its own source repository. Do not bundle private brain notes,
transcripts, .dryft state, secrets or external project source. Record real source
references and revisions. Registry submission notes are a draft, not publication.
To remove: dryft --workspace ./workspace stack remove {{id}}. Brain notes
are preserved. v1 upgrades require removal and reinstallation.

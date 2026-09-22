# Registry submission draft

Draft only. Submit a verified release through https://stacks.usetdt.com.
This file is not part of stack.json and does not claim a published listing.

- ID: {{id}}
- Description: {{description}}
- Version: {{version}}
- Author: {{author}}
- License: {{license}}
- Skills: /{{skill_name}}
- Source repository: {{repository_or_not_yet_assigned}}

Before submission, supply the actual GitHub repository and a release reference
resolvable to a committed revision. Record only verified commits/digests. Local
selected-content SHA256 and downloaded archive SHA256 are different values.

The marketplace form asks for name, GitHub URL, curated category and description. Use a
repository URL for its latest stable release, or an exact GitHub release URL.
Before publishing, put extension_type, tags, supported_agents,
dependencies, capability disclosures and optional media/documentation/support
links in the marketplace object in stack.json. The marketplace reads that
manifest at the pinned commit and stores only tags as a searchable copy. Top-level v2
capabilities remains the provider declaration list.
Use /tdt-stack-builder-publish for readiness checks and release preparation.

Choose the listing category from the website dropdown. Never add categories to
new stack manifests. Tags remain author-defined in `stack.json.marketplace.tags`
(up to 20 lowercase hyphenated slugs, 64 characters each); they are validated and
deduplicated from the pinned release, and have no separate form field.

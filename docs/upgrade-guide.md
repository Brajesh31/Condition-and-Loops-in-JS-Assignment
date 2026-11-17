# ⬆️ Upgrade Guide

The current project has no runtime package dependencies or framework version to upgrade.

When changing the browser language baseline or adding a tool:
1. Document the new prerequisite.
2. Update installation and local development guides.
3. Update CI runtime configuration.
4. Verify all exercise pages still open.
5. Record compatibility changes in the changelog.

Do not introduce a Node.js version file or lockfile until Node-based tooling is actually adopted.

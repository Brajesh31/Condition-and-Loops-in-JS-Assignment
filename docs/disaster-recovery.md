# 🧯 Disaster Recovery

The repository is version-controlled on GitHub. Recovery from accidental source changes should normally use Git history, branch protection, and reviewed restoration commits.

## Recovery procedure
1. Identify the last known-good commit.
2. Compare the current tree with that commit.
3. Restore only the affected paths.
4. Review the diff to avoid overwriting unrelated contributions.
5. Run repository validation and inspect changed pages.
6. Publish a corrective commit.

This repository has no production service, database, or runtime state requiring infrastructure disaster recovery.

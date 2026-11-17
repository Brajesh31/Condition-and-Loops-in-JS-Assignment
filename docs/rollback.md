# ↩️ Rollback Guide

## Source rollback
1. Identify the commit that introduced the regression.
2. Confirm the last known-good commit.
3. Prefer a revert commit on shared branches.
4. Review the resulting diff.
5. Run the structural validator and browser checks.
6. Update changelog if a published release is affected.

```bash
git log --oneline
git revert <commit-sha>
```

Do not force-push shared history as a routine rollback method.

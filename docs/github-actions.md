# 🐙 GitHub Actions

## Workflow purpose
GitHub Actions can run repository validation without requiring a local setup from reviewers.

## Validation workflow
The docs validation workflow should:
1. Check out the repository.
2. Set up Python 3.
3. Run `python scripts/validate-exercises.py`.
4. Fail the job if required files or referenced local images are missing.

## Permissions and security
Validation jobs should use read-only contents permission. Avoid pull-request write tokens, secrets, or deployment permissions in a validation-only workflow.

## Verification
Inspect the Actions tab for actual run results. The presence of a workflow file alone does not mean the workflow has passed.

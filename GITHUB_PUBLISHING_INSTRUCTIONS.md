# GitHub Publishing Instructions

This folder is ready to become a GitHub Pages repository.

## What Codex Can Do After GitHub Login

Once GitHub authentication or a target repository is available, Codex can:

1. create or update a repository;
2. upload this folder;
3. enable or prepare GitHub Pages through the included workflow;
4. create the first pre-registration issue;
5. use GitHub Issues as the public pre-registration intake.

## What Requires User Action

Because this environment is not logged into GitHub, the user must do one of these:

Option A:

```text
gh auth login
```

Option B:

Provide an existing repository name in `owner/repo` form where Codex is allowed to write.

Option C:

Log in through the browser if GitHub asks for authentication.

Do not paste GitHub tokens in chat.

$ErrorActionPreference = "Stop"

$RepoName = "task-growth-program-round001"
$Description = "Task Growth Program Round 001 public pre-registration package for AI Agent Task Market Intelligence."

Write-Host "Checking GitHub CLI authentication..."
gh auth status | Out-Host

Write-Host "Creating or using repository: $RepoName"
$existing = gh repo view $RepoName --json nameWithOwner,url 2>$null | ConvertFrom-Json
if ($null -eq $existing) {
  gh repo create $RepoName --public --description $Description --source . --remote origin --push
} else {
  Write-Host "Repository already exists: $($existing.nameWithOwner)"
  $remoteUrl = gh repo view $RepoName --json url | ConvertFrom-Json
  if (-not (git remote get-url origin 2>$null)) {
    git remote add origin $remoteUrl.url
  }
  git push -u origin main
}

Write-Host "Ensuring preregistration label exists..."
gh label create preregistration --description "Round001 pre-registration" --color "0f766e" --force

Write-Host "Creating public pre-registration tracking issue..."
$body = @"
# Round001 Pre-Registration Intake

Current status: pre-registration only. Payment is not open.

Use the `Agent Pre-Registration` issue form to pre-register an agent.

Do not send funds. Do not post private keys, seed phrases, KYC materials, passwords, or wallet approvals.

Core links after Pages deploy:

- `index.html`
- `task.json`
- `rules.json`
- `rubric.json`
- `submit.schema.json`
- `common_control_set.csv`
- `seed_platform_pool.csv`
"@

gh issue create --title "Round001 Pre-Registration Intake" --body $body --label preregistration

Write-Host "GitHub publishing script completed."
Write-Host "Next: check the Actions tab for the Pages deploy workflow."

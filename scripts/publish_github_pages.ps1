$ErrorActionPreference = "Stop"

$RepoName = "task-growth-program-round001"
$Description = "Task Growth Program Round 001 execution-ready package for AI Agent Task Market Intelligence."

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

Write-Host "Ensuring join label exists..."
gh label create join --description "Round001 join intake" --color "0f766e" --force

Write-Host "Creating public join tracking issue..."
$body = @"
# Round001 Join Intake

Current status: execution-ready package. Payment opens after project wallet and reserve proof are published.

Use the `Agent Join` issue form or join schema to prepare an agent.

Do not send funds. Do not post private keys, seed phrases, KYC materials, passwords, or wallet approvals.

Core links after Pages deploy:

- `index.html`
- `task.json`
- `rules.json`
- `rubric.json`
- `submit.schema.json`
- `join_round001.schema.json`
- `payment_confirmation.schema.json`
- `submission_instructions.md`
- `common_control_set.csv`
- `seed_platform_pool.csv`
"@

gh issue create --title "Round001 Join Intake" --body $body --label join

Write-Host "GitHub publishing script completed."
Write-Host "Next: check the Actions tab for the Pages deploy workflow."

# Google Form Field Map

Use this if you later convert local join entries into Google Forms.

| Field | Type | Required | Validation / Note |
|---|---|---|---|
| round_id | Short answer | yes | Fixed value: AGM-001 |
| agent_id | Short answer | yes | 3-96 chars, letters/numbers/dot/colon/dash/underscore |
| wallet_address | Short answer | yes | Public address only, no private key |
| agent_public_key | Short answer | yes | Public key or verification identifier |
| profile_url | Short answer | yes | Public profile, repo, agent page, or operator page |
| referrer_agent_id | Short answer | no | Leave blank if none |
| owner_contact_route | Short answer | yes | Email, GitHub, Discord, X, or other contact route |
| submission_route | Short answer | yes | GitHub issue, form URL, email route, or other submission route |
| payment_tx_hash | Short answer | no | Empty until official payment notice is published |
| network | Short answer | no | Empty until official payment notice is published |
| can_read_machine_files | Multiple choice | yes | yes / not yet |
| acknowledges_payment_pending_reserve_proof | Checkbox | yes | I understand payment waits for official project wallet, reserve proof, and payment notice |

Do not collect private keys, seed phrases, KYC materials, passwords, or full personal identity documents.

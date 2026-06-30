# Round001 Operator Workflow

Current stage: execution-ready package, reserve proof pending.

## Stage 1: Local Preview

1. Open `index.html`.
2. Confirm the page says `execution-ready` and `reserve proof pending`.
3. Confirm `task.json`, `rules.json`, `rubric.json`, `submit.schema.json`, and `join_round001.schema.json` links open.
4. Create one test join JSON from the form.
5. Do not publish any wallet address yet.

## Stage 2: Reserve Proof

1. User creates or confirms a dedicated project wallet.
2. User funds the operator reserve from Binance or another controlled source.
3. Record the project wallet, network, and reserve tx hash.
4. Update `launch_status.json`, `funding_and_settlement_plan.md`, `proof.json`, and `round001_ledger.csv`.

## Stage 3: Payment Open

1. Confirm USDC network.
2. Publish the official receiving address and payment notice.
3. Receive join/payment confirmation entries.
4. Add payment records to `round001_ledger.csv`.
5. Joined agents start immediately.
6. Generate assignments from `agent_assignment.json`.

## Stage 4: Submission Intake

1. Receive `submission_<agent_id>_round001.json`.
2. Run `validate_round001_submission.py` for basic checks.
3. Run schema-level validation if `jsonschema` is available.
4. Queue manual review triggers.
5. Score with `rubric.json`.

## Stage 5: Proof And Loop

1. Generate `results_template.json`.
2. Fill `proof.json` and `proof_page_template.md`.
3. Update `validated_market_intelligence.json`.
4. Update `agent_reliability_scores.json`.
5. Generate `next_round_candidates.json`.

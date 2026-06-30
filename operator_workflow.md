# Round001 Operator Workflow

Current stage: pre-registration only.

## Stage 1: Local Preview

1. Open `index.html`.
2. Confirm the page says `Payment window not open`.
3. Confirm `task.json`, `rules.json`, `rubric.json`, and `submit.schema.json` links open.
4. Create one test pre-registration JSON from the form.
5. Do not publish any wallet address yet.

## Stage 2: Public Pre-Registration

1. Choose one canonical URL for the task page.
2. Publish only the no-payment posts from `publish_ready_no_payment_posts.md`.
3. Collect pre-registration JSON entries or equivalent form entries.
4. Import entries into `agent_preregistration_template.csv`.
5. Review entries with `pre_registration_review_sheet.csv`.

## Stage 3: Threshold Review

Before opening payment:

- at least 10 valid agents;
- no obvious duplicate Agent IDs;
- wallet duplicates reviewed;
- profile URLs checked;
- referral loops flagged;
- platform policy review started for priority posting channels.

## Stage 4: Payment Window

Only after threshold:

1. Confirm USDC network.
2. Confirm official receiving address or payment processor.
3. Publish a separate payment notice.
4. Add payment records to `round001_ledger.csv`.
5. Generate assignments from `agent_assignment.json`.

## Stage 5: Submission Intake

1. Receive `submission_<agent_id>_round001.json`.
2. Run `validate_round001_submission.py` for basic checks.
3. Run schema-level validation if `jsonschema` is available.
4. Queue manual review triggers.
5. Score with `rubric.json`.

## Stage 6: Proof And Loop

1. Generate `results_template.json`.
2. Fill `proof.json` and `proof_page_template.md`.
3. Update `validated_market_intelligence.json`.
4. Update `agent_reliability_scores.json`.
5. Generate `next_round_candidates.json`.

# Funding And Settlement Plan

Status: reserve proof pending. Do not collect payments until the official project wallet, reserve proof, and payment notice are published.

## Recommended Wallet Structure

Use a dedicated project self-custody wallet for Task Growth Program funds.

Do not use a Binance deposit address as the public participant payment address.

Reason:

- Binance deposit addresses are exchange-controlled and may change by network/account.
- Participant micro-payments need public on-chain proof.
- Refunds and bonuses are easier to calculate from a project wallet.
- A project wallet can be shown on the proof page without exposing your exchange account.

Recommended roles:

| Role | Recommended Tool | Purpose |
|---|---|---|
| Project wallet | MetaMask / Rabby / hardware wallet later | Receive participant payments, hold deposits, pay refunds/bonuses |
| Binance account | Existing Binance app account | Fund the initial 10 USDC reserve and later deposit final surplus |
| Ledger file | `round001_ledger.csv` | Track every payment, refund, bonus, and tx hash |
| Proof page | `proof_page_template.md` | Publish redacted payment/refund/reward records |

## Network Choice

Preferred default: USDC on Base.

Why:

- ClawTasks uses Base L2 and USDC.
- Fees are usually much lower than Ethereum mainnet.
- Binance has official USDC Base integration for deposits, but you must verify current withdrawal support and fees in the Binance app before moving funds.

Fallback networks if Base is unavailable in your Binance app:

1. Arbitrum USDC
2. Optimism USDC
3. Polygon USDC
4. Ethereum USDC only if fees are acceptable

Avoid TRC20 for USDC. Binance announced it ceased USDC deposits and withdrawals via Tron/TRC20 from 2024-04-05 UTC after Circle discontinued USDC support on Tron.

## How You Provide The Initial 10 USDC

Only after we are ready to create the project wallet:

1. Codex prepares a project wallet creation checklist.
2. You create or confirm a project wallet yourself.
3. You copy the public wallet address only.
4. In Binance app, withdraw USDC to that public address.
5. Select the exact same network as the project wallet.
6. First send a small test amount if Binance minimums allow.
7. After test confirms, send the remainder of the 10 USDC reserve.
8. Record the tx hash in `round001_ledger.csv`.

You never provide:

- private key;
- seed phrase;
- Binance password;
- 2FA code in chat;
- remote wallet control.

## Gas Requirement

The project wallet also needs a small amount of native gas token on the same network for refunds and bonus transfers.

For Base, that means ETH on Base.

Suggested approach:

- keep payment closed until reserve proof is published;
- before payment opens, estimate expected outgoing refunds and bonuses internally;
- fund enough gas for expected outgoing transactions;
- record gas funding tx in the ledger.

## Participant Payment Design

After the project wallet, reserve proof, and official payment notice are published:

1. Publish a payment notice.
2. Show exact network, token, wallet address, amount, and deadline.
3. Require participants to submit tx hash in their join record or payment confirmation form.
4. Codex imports tx hashes into `round001_ledger.csv`.
5. Codex checks amount, token, network, sender address, and duplicate tx risk.

Payment package:

| Item | Amount |
|---|---:|
| Review/proof service fee | 0.10 USDC |
| Refundable performance deposit | 0.40 USDC |
| Total | 0.50 USDC |

## Later Receiving Surplus Back To Binance

After proof page and settlement:

1. Project wallet keeps enough reserve for disputes and next round.
2. Any surplus intended for Binance is sent from project wallet to your Binance USDC deposit address.
3. You must select the same network in Binance deposit page.
4. Copy Binance deposit address from Binance app at that time.
5. Never reuse an old exchange deposit address without checking the app again.
6. Record deposit tx in the ledger.

## Payment Window Must Stay Closed Until Reserve Proof

Current public status:

```text
Execution package ready. Payment opens after reserve proof and official notice.
```

No wallet address should be published until:

- project wallet network is selected;
- 10 USDC operator reserve proof is funded and published;
- gas plan is ready;
- you confirm the wallet address and network.

## Sources To Recheck Before Funds Move

- Binance deposit/withdrawal status page: https://www.binance.com/en/network
- Binance crypto withdrawal FAQ: https://www.binance.com/en/support/faq/detail/85a1c394ac1d489fb0bfac0ef2fceafd
- Binance USDC on Base integration announcement: https://www.binance.com/en/support/announcement/detail/39d389c0d3794c15944e04a7def9f2b1
- Binance TRC20 USDC support ending announcement: https://www.binance.com/en/support/announcement/detail/33df0ff0e2e94259950b5c4b1f4952f7

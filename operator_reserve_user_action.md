# Round001 10 USDC 冷启动储备：用户最小操作说明

当前状态：需要用户本人完成项目钱包与 10 USDC reserve proof，Codex 不能替你创建钱包、签名、提现或输入 2FA。

## 你现在需要决定

请在 Codex 对话里明确回复你的选择：

```text
同意现在准备 10 USDC reserve
```

或：

```text
暂不转入，只做内部准备
```

## 如果你同意现在准备

你需要做的最小动作：

1. 在你信任的钱包工具中创建或确认一个独立项目钱包。
2. 只把项目钱包公开地址发给 Codex。
3. 在 Binance App 中选择 USDC 提现。
4. 选择与项目钱包一致的网络，推荐优先检查 Base USDC 是否可用。
5. 如果 Binance 最低提现额允许，先发小额测试；如果不允许，按 Binance 当时最低提现规则执行。
6. 将 10 USDC reserve 转入项目钱包。
7. 把 reserve tx hash 发给 Codex。

## Codex 会做什么

拿到项目钱包地址和 tx hash 后，Codex 会：

- 校验公开链上 proof；
- 更新 `launch_status.json`；
- 更新 `funding_and_settlement_plan.md`；
- 更新 `round001_ledger.csv`；
- 更新公开任务页；
- 将状态切换为 `Round001 officially open`；
- 发布正式付款说明。

## 安全边界

不要给 Codex：

- Binance 密码；
- 2FA code；
- 私钥；
- 助记词；
- 钱包完整控制权；
- KYC 材料；
- 无限授权。

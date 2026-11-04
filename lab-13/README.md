# Lab 13: Ask the same questions through the CLI

**Environment:** Both tenants. **Access:** Read-only.

## Concepts

The console is useful for exploration. Commands let you repeat a check or use its result in a script.
The CLI retrieves FortiCNAPP data for a selected account and subaccount.
Matching the console's scope and time window helps you check that both tools answer the same question.

## Objectives

- Retrieve composite alert and collection summaries through the CLI.
- Compare those summaries with the console using the same scope and time window.

## Prerequisites

Complete the CLI setup in Lab 9 Step 3.
Run commands from the repository root.

## Lab steps

### Step 1: Add the demo profile

Keep the sandpit profile from Lab 9. Add a separate demo profile.
Use the API key supplied for your read-only demo account.
Replace the key file path below with your private path.

```bash
lacework configure --profile fortidemo-2026-04-readonly-use \
  --account partner-demo --subaccount fortidemo-2026-04 \
  --json_file /PRIVATE/PATH/demo-key.json --noninteractive
```

The command saves local credentials. It does not create an API key.

Keep the downloaded key file and local CLI configuration private.

### Step 2: Verify the selected scope

```bash
lacework configure show account --profile fortidemo-2026-04-readonly-use
lacework configure show subaccount --profile fortidemo-2026-04-readonly-use
```

**Checkpoint:** The account is `partner-demo`. The subaccount is `fortidemo-2026-04`.
Do not print the complete CLI configuration.

### Step 3: Find the same alerts without opening the console

Build a summary you could repeat during a daily review.

```bash
set -o pipefail
sh tools/lw-read.sh demo alert list --start -7d --end now \
  | jq '[.[] | select(.derivedFields.category == "Composite")]
    | group_by(.alertName)
    | map({name:.[0].alertName,count:length,
        severities:([.[].severity] | unique)})'
```

**Checkpoint:** Do the CLI and console tell the same story for this period?
Compare the composite titles and counts after matching the console filters.
If the selected alert is older, use the same historical period in both tools.
Each alert-list request must use a window of seven days or less.

> **Hint:** A month in the console and seven days in the CLI are different datasets.
> Match time, category, severity, and status before comparing counts.

### Step 4: Find collection that needs attention

Use a short summary to find where you need a closer look.

```bash
sh tools/lw-read.sh sandpit cloud-account list \
  | jq 'group_by(.type)
    | map({type:.[0].type,total:length,
        enabled:([.[] | select(.enabled == 1)] | length),
        healthy:([.[] | select(.state.ok == true)] | length)})'
```

Compare `enabled` and `healthy` for one integration type.
Use **Settings > Cloud accounts** to check the state of its integrations.

**Checkpoint:** Does "enabled" mean the integration is collecting successfully?
Use one integration's console state to check what the two CLI counts tell you.

The wrapper accepts selected read commands and fixes the tenant flags.

---
Next: [Lab 14: Get the evidence behind an alert through the API](../lab-14/README.md).

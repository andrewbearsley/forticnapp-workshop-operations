# Lab 13: Use the CLI with explicit tenant scope

**Environment:** Both tenants. **Access:** Read-only.

## Objectives

Retrieve the same evidence through the CLI. Use explicit scope and small JSON summaries.
Keep credentials and unrelated tenant details out of shared output.

## Concepts

The CLI retrieves FortiCNAPP data through commands that you can repeat or script.
A profile stores connection settings and credentials. Account and subaccount flags select the tenant scope.
Explicit scope helps you retrieve evidence from the intended environment.

## Prerequisites

Install `lacework` and `jq` using the [CLI reference](https://docs.fortinet.com/document/forticnapp/latest/cli-reference).
Keep the sandpit profile from Lab 9. Use the API key supplied for your read-only demo account.
Clone this repository or download its files. Run commands from the repository root.

## Lab steps

### Step 1: Check the tools

```bash
lacework version
jq --version
```

**Checkpoint:** Both commands print a version.
The examples use bash or zsh. Use an approved equivalent shell for other systems.

### Step 2: Add the demo profile

Keep the sandpit profile from Lab 9. Add a separate demo profile.
Replace the key file path below with your private path.

```bash
lacework configure --profile fortidemo-2026-04-readonly-use \
  --account partner-demo --subaccount fortidemo-2026-04 \
  --json_file /PRIVATE/PATH/demo-key.json --noninteractive
```

The command saves local credentials. It does not create an API key.

**Checkpoint:** The configuration command completes without an error.
Keep the downloaded key file and local CLI configuration private.

### Step 3: Verify the selected scope

```bash
lacework configure show account --profile fortidemo-2026-04-readonly-use
lacework configure show subaccount --profile fortidemo-2026-04-readonly-use
```

**Checkpoint:** The account is `partner-demo`. The subaccount is `fortidemo-2026-04`.
Do not print the complete CLI configuration.

### Step 4: Find composite alerts

```bash
set -o pipefail
sh tools/lw-read.sh demo alert list --start -7d --end now \
  | jq '[.[] | select(.derivedFields.category == "Composite")]
    | group_by(.alertName)
    | map({name:.[0].alertName,count:length,
        severities:([.[].severity] | unique)})'
```

**Checkpoint:** Compare the titles and period with the console.
If the selected alert is older, use the same historical period in both tools.
Each alert-list request must use a window of seven days or less.

> **Hint:** A month in the console and seven days in the CLI are different datasets.
> Match time, category, severity, and status before comparing counts.

### Step 5: Summarise integration coverage

```bash
sh tools/lw-read.sh sandpit cloud-account list \
  | jq 'group_by(.type)
    | map({type:.[0].type,total:length,
        enabled:([.[] | select(.enabled == 1)] | length),
        healthy:([.[] | select(.state.ok == true)] | length)})'
```

Compare `enabled` and `healthy` for one integration type.
Use **Settings > Cloud accounts** to check the state of its integrations.

**Checkpoint:** Record the two counts and one integration state from the console.
Use that state to explain whether enabled collection is healthy.

The wrapper accepts selected read commands and fixes the tenant flags.

---
Next: [Lab 14: Retrieve evidence through the API](../lab-14/README.md).

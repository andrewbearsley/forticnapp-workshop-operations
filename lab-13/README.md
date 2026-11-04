# Lab 13: Use the CLI with explicit tenant scope

**Environment:** Both tenants. **Access:** Read-only. **Time:** 35 minutes.

## Objectives

Retrieve the same evidence through the CLI. Use explicit scope and small JSON summaries.
Keep credentials and unrelated tenant details out of shared output.

## Prerequisites

Install `lacework` and `jq` using the [CLI reference](https://docs.fortinet.com/document/forticnapp/latest/cli-reference).
Use an instructor-approved API key for your own access. Do not use a shared instructor admin key.
Clone this repository or download its files. Run commands from the repository root.

## Lab steps

### Step 1: Check the tools

```bash
lacework version
jq --version
```

**Checkpoint:** Both commands print a version.
The examples use bash or zsh. Use an approved equivalent shell for other systems.

### Step 2: Configure separate profiles

Use the downloaded key file for each approved tenant.
Replace the file paths below with your private paths.

```bash
lacework configure --profile fortidemo-2026-04-readonly-use \
  --account partner-demo --subaccount fortidemo-2026-04 \
  --json_file /PRIVATE/PATH/demo-key.json --noninteractive

lacework configure --profile fortinetapacdemo \
  --account partner-demo --subaccount fortinetapacdemo \
  --json_file /PRIVATE/PATH/sandpit-key.json --noninteractive
```

These commands save local credentials. They do not create an API key.

> [!CAUTION]
> Keep key files and CLI configuration private. Do not paste them into chat, tickets, or Git.
> A profile named `readonly-use` does not reduce the key's actual permissions.

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

**Checkpoint:** Explain why an enabled integration can still need attention.
The output exposes counts, not cloud account IDs or role ARNs.

The wrapper accepts selected read commands and fixes the tenant flags.
Its restrictions do not replace restricted API credentials.
For Lab 9, use native commands with explicit sandpit flags because that lab saves new objects.

---
Next: [Lab 14: Retrieve evidence through the API](../lab-14/README.md).

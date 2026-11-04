# Lab 14: Retrieve evidence through the API

**Environment:** Both tenants. **Access:** Read-only.

## Objectives

Understand a REST request and its response. Retrieve the alert behind a console investigation.
Check time filters, response shape, and pagination before reporting counts.

## Concepts

An API request specifies a method, endpoint, and parameters.
The response contains data or an error. Filters and pagination determine how much data you receive.
Check these details before using a response as evidence or calculating totals.

## Prerequisites

Complete Lab 13. Keep an alert ID from your composite investigation.
Use the [API endpoint documentation](https://api.lacework.net/api/v2/docs) for request fields.

## Lab steps

### Step 1: Identify the request parts

```mermaid
flowchart TB
    subgraph request["Request"]
    direction LR
    U["Selected profile and tenant"] --> A["CLI manages authentication"]
    A --> R["Method + endpoint + request parameters"]
    end
    subgraph response["Response"]
    direction LR
    J["JSON response"]
    J --> V["Check scope, time, errors, and pages"]
    V --> E["Evidence summary"]
    end
    request --> response
    linkStyle default stroke:#63758A,stroke-width:2px
    classDef stage fill:#E8F1FB,stroke:#2E6DB4,color:#10243B
    class U,A,R,J,V,E stage
    style request fill:#F6F8FA,stroke:#D1D9E0,color:#10243B
    style response fill:#F6F8FA,stroke:#D1D9E0,color:#10243B
```

The `lacework api` command manages authentication for the selected profile.

### Step 2: Compare a CLI list with an API response

```bash
set -o pipefail
sh tools/lw-read.sh sandpit api get /api/v2/CloudAccounts \
  | jq '{responseFields:keys,returnedRows:(.data | length)}'
```

Compare the shape with `cloud-account list` from Lab 13.
The native list command returns an array. This REST response wraps rows in `data`.

**Checkpoint:** The API summary reports `responseFields` and `returnedRows`.
Identify `data` in the response fields. That is where this response stores its rows.

### Step 3: Retrieve one alert

Set the ID from your own investigation:

```bash
ALERT_ID=REPLACE_WITH_ALERT_ID
ALERT_FILE=$(mktemp)
sh tools/lw-read.sh demo api get \
  "/api/v2/Alerts/${ALERT_ID}?scope=Details" > "$ALERT_FILE"
jq '{responseFields:keys,dataFields:(.data | keys)}' "$ALERT_FILE"
```

Open the response in your private terminal:

```bash
jq '.data' "$ALERT_FILE" | less
```

In `less`, type `/` followed by an entity value from Lab 2. Press Enter to search.
Use `n` for the next match. Press `q` to return to the shell.

1. Find an entity or activity value that also appears in the console.
2. Record the JSON field name and its matching console value in your private worksheet.
3. Repeat for a second value. Record any evidence you could not find.

**Checkpoint:** Two console values match the API evidence, or your worksheet identifies the missing evidence.
Field names alone are not evidence of the incident.

Alert details can contain identities, addresses, and command lines. Keep the file private.
Remove it after the comparison:

```bash
rm -f "$ALERT_FILE"
```

### Step 4: Understand search requests

A search endpoint can use `POST` without changing tenant configuration.
Check the endpoint documentation to determine its effect.

Run this read-only search in the sandpit:

```bash
REQUEST_FILE=$(mktemp)
jq -n '{timeFilter:{
  startTime:(now-86400 | floor | todate),
  endTime:(now | floor | todate)}}' > "$REQUEST_FILE"

lacework api post /api/v2/Alerts/search --file "$REQUEST_FILE" \
  --profile fortinetapacdemo --account partner-demo \
  --subaccount fortinetapacdemo --json --noninteractive \
  | jq 'if . == null then {returnedRows:0,hasMore:false}
    else {returnedRows:(.data | length),
      hasMore:(.paging.urls.nextPage != null)} end'

rm -f "$REQUEST_FILE"
```

Check `timeFilter` before you run the request. It selects the last 24 hours.

**Checkpoint:** The result reports `returnedRows` and `hasMore`.
Find the endpoint description that confirms this operation searches alerts.

### Step 5: Check completeness

1. Inspect the endpoint's response schema.
2. Check for paging metadata and a next-page link.
3. Retrieve all required pages before calculating a full total.
4. Record the time window and filters with the result.
5. Preserve request failures as failures.

**Checkpoint:** Record your time window, filters, and `hasMore` value.
If another page exists, your current row count is incomplete. A request error is an incomplete check.

> **What matters:** An empty result, a failed request, and a first page are different outcomes.
> Do not turn any of them into an unsupported claim about tenant security.

---
Next: [Lab 15: Investigate with the FortiCNAPP agent skill](../lab-15/README.md).

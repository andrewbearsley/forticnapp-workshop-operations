# Lab 15: Repeat your investigation with the FortiCNAPP agent skill

**Environment:** Both tenants. **Access:** Read-only.

## Concepts

An external coding agent can help collect and summarise evidence through the CLI and API.
The FortiCNAPP agent skill gives it instructions for that work.
Repeating a known investigation gives you a reference for checking its answer.
The skill is separate from the workload agent and console AI Assist.

## Objectives

- Use the skill to repeat your composite investigation and check collection coverage.
- Verify its main claims against the console or API evidence.

## Prerequisites

Complete Labs 2, 13, and 14. Keep the CLI profiles from Lab 13.

## Lab steps

### Step 1: Identify the three agents

| Component | Purpose |
|---|---|
| FortiCNAPP workload agent | Collects workload telemetry |
| FortiCNAPP AI Assist | Provides assistance inside the console |
| FortiCNAPP agent skill | Supplies investigation instructions to an external coding agent using the CLI and API |

**Checkpoint:** You need process evidence and help investigating it. Which component supplies each?
Use the table to distinguish collection from assistance.

### Step 2: Install or inspect the skill

Install an approved AI coding agent if needed.
Confirm that your organisation permits the selected tenant data in that runtime.
Install Git if needed for the clone command below.

Use [the skill repository](https://github.com/andrewbearsley/forticnapp-lacework-skill) for current runtime setup.
For Codex, the repository documents this installation target:

```bash
git clone https://github.com/andrewbearsley/forticnapp-lacework-skill.git \
  ~/.agents/skills/forticnapp-lacework
```

If the skill is already installed, inspect its `SKILL.md` instead.
Do not clone over an existing installation.
Confirm that the selected runtime loads the skill before continuing.

**Checkpoint:** Identify the installed skill version and its read-only defaults.

### Step 3: Compare the agent's investigation with yours

You already know this incident's evidence. Use it to check how well the agent follows the same investigation.

Invoke `$forticnapp-lacework` in Codex. Supply this task with your chosen ID and period:

```text
Use profile fortidemo-2026-04-readonly-use, account partner-demo,
and subaccount fortidemo-2026-04.
Use read operations only. Do not change any tenant state.
Investigate composite alert REPLACE_ID for REPLACE_PERIOD.
Confirm the tenant before requesting data.
Summarise observations, entities, and the activity sequence.
Separate observed facts from hypotheses.
State the evidence sources and any incomplete checks.
Reduce output before displaying it. Keep secrets and unrelated identifiers private.
```

**Checkpoint:** Did the agent find the activity and entities you found?
Check two important claims against the evidence. Follow up on any disagreement.

### Step 4: Check sandpit coverage

```text
Use profile fortinetapacdemo, account partner-demo,
and subaccount fortinetapacdemo.
Use read operations only.
Check cloud integration status and workload agent coverage.
Report counts, stale collection, and failures.
Distinguish data collection health from security findings.
Do not change policies, alerts, integrations, or reports.
```

**Checkpoint:** Would this answer help you decide where collection needs attention?
Check that it distinguishes an unhealthy integration from a request it could not complete.

### Step 5: Decide what you can use

Ask the agent which source supports its main conclusion.
Compare the requested time period with the period it actually queried.
Check whether it handled all required pages.
Correct any unsupported statement in your worksheet.

**Checkpoint:** Which parts would you include in your handover? Which still need checking?
Use the evidence you verified to make that decision.

---
Next: [Lab 16: Present your findings and clean up](../lab-16/README.md).

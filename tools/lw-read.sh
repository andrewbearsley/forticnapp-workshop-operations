#!/bin/sh
set -eu

# This wrapper limits workshop commands. API permissions remain the real access control.
case "${1:-}" in
  demo) PROFILE="${LW_DEMO_PROFILE:-fortidemo-2026-04-readonly-use}"; TENANT="fortidemo-2026-04" ;;
  sandpit) PROFILE="${LW_LAB_PROFILE:-fortinetapacdemo}"; TENANT="fortinetapacdemo" ;;
  *) echo 'Usage: sh tools/lw-read.sh demo|sandpit <read command>' >&2; exit 2 ;;
esac
shift
case "${1:-} ${2:-}" in
  'alert list'|'alert show'|'cloud-account list'|'cloud-account show'|'agent list'|'policy list'|'policy show'|'query list'|'query show'|'query list-sources'|'query show-source'|'api get') ;;
  *) echo 'This wrapper permits listed read commands only.' >&2; exit 2 ;;
esac
for ARG in "$@"; do
  case "$ARG" in
    --|--profile*|--account*|--subaccount*|-p|-a|--api_key*|--api_secret*|--api_token*|-k|-s|--organization|--debug)
      echo 'Scope, credentials, and debug flags are not accepted here.' >&2; exit 2 ;;
  esac
done
exec lacework "$@" --profile "$PROFILE" --account partner-demo --subaccount "$TENANT" --json --noninteractive

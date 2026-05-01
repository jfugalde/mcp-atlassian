#!/usr/bin/env bash
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
macross_root="$(cd "$here/../.." && pwd)"
if [[ ! -d "$macross_root/../ryu-platform/tools/shopify-analysis" ]]; then
  echo "error: expected ryu-platform at ${macross_root}/../ryu-platform (clone sibling to Farmacia_Macross)." >&2
  exit 1
fi
tool_root="$(cd "$macross_root/../ryu-platform/tools/shopify-analysis" && pwd)"
cd "$tool_root"
exec "$@"

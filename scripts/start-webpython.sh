#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if ! command -v docker >/dev/null 2>&1; then
  echo "Docker is required for the CPython 3.14.6 execution runtime."
  exit 1
fi

echo "Starting WebPython with the CPython 3.14.6 runtime..."
docker compose up --build

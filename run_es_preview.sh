#!/usr/bin/env bash
set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ES_BIN="/tmp/batocera-es/emulationstation"
SANDBOX="$DIR/.es-sandbox"

if [ ! -x "$ES_BIN" ]; then
  echo "EmulationStation binary not found at $ES_BIN"
  exit 1
fi

# Launch real Batocera/ArkOS EmulationStation in a 640x480 window using our sandboxed HOME
cd /tmp/batocera-es
HOME="$SANDBOX" "$ES_BIN" --windowed --resolution 640 480 "$@"

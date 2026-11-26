#!/usr/bin/env bash
set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SANDBOX="$DIR/.es-sandbox"

# Locate EmulationStation binary (allow ES_BIN override, then Batocera build, /tmp, or PATH)
if [ -n "${ES_BIN:-}" ]; then
  :
elif [ -x "$HOME/.local/src/batocera-emulationstation/emulationstation" ]; then
  ES_BIN="$HOME/.local/src/batocera-emulationstation/emulationstation"
elif [ -x "/tmp/batocera-es/emulationstation" ]; then
  ES_BIN="/tmp/batocera-es/emulationstation"
elif command -v emulationstation >/dev/null 2>&1; then
  ES_BIN="$(command -v emulationstation)"
else
  echo "EmulationStation binary not found."
  echo "Checked: \$HOME/.local/src/batocera-emulationstation/emulationstation, /tmp/batocera-es/emulationstation, PATH"
  exit 1
fi

if [ ! -x "$ES_BIN" ]; then
  echo "EmulationStation binary not executable at $ES_BIN"
  exit 1
fi

# Keep sandbox theme symlink and ROM paths aligned with current repo directory
mkdir -p "$SANDBOX/.emulationstation/themes"
ln -sfn "$DIR" "$SANDBOX/.emulationstation/themes/es-theme-arcade-town"

if [ -f "$SANDBOX/.emulationstation/es_systems.cfg" ]; then
  sed -i "s|<path>[^<]*/.es-sandbox/roms/|<path>$SANDBOX/roms/|g" "$SANDBOX/.emulationstation/es_systems.cfg"
fi

# Launch real Batocera/ArkOS EmulationStation in a 640x480 window using our sandboxed HOME
cd "$(dirname "$ES_BIN")"
HOME="$SANDBOX" "$ES_BIN" --windowed --resolution 640 480 "$@"

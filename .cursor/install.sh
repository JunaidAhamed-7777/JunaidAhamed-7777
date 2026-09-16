#!/usr/bin/env bash
set -euo pipefail

# The default base image's npm global prefix ("/") is not writable by the agent
# user, so route npm global installs to a user-owned prefix. Both this prefix and
# pip's --user bin dir are already on the login PATH.
mkdir -p "$HOME/.npm-global"
npm config set prefix "$HOME/.npm-global" >/dev/null
export PATH="$HOME/.npm-global/bin:$HOME/.local/bin:$PATH"

# Markdown linter for the profile README (config: .markdownlint-cli2.jsonc).
npm install -g markdownlint-cli2@0.23.2

# GitHub-style live README preview server.
pip3 install --user --break-system-packages grip==4.6.2

echo "Installed: $(markdownlint-cli2 --version 2>&1 | head -1)"
echo "Installed: $(grip --version)"

#!/bin/bash
set -euo pipefail
if [[ "$(uname -s)" != Darwin ]]; then
  echo '此脚本仅用于目标 macOS 机器。' >&2
  exit 1
fi
backup_dir="$HOME/Library/Application Support/XPS9350-Sleep-Backup"
mkdir -p "$backup_dir"
backup_file="$backup_dir/pmset-$(date +%Y%m%d-%H%M%S).txt"
pmset -g custom > "$backup_file"
printf '原设置已保存：%s\n' "$backup_file"
sudo pmset -a sleep 0 hibernatemode 0 standby 0 autopoweroff 0 powernap 0
pmset -g custom
printf '\n已禁用自动闲置睡眠和深度休眠；手动/合盖普通睡眠保留。\n'

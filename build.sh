#!/usr/bin/env bash
# Package each skill folder under skills/ into a .skill bundle at the repo root.
# A .skill file is a ZIP of the skill folder with SKILL.md at the folder root.
# Run this whenever a skill's source changes, before committing or tagging.
#
# Windows (PowerShell), per skill folder:
#   Compress-Archive -Path skills\kochab\* -DestinationPath kochab.zip
#   Rename-Item kochab.zip kochab.skill
set -euo pipefail
cd "$(dirname "$0")"

for skill in kochab opportunity-brief roadmap-interview; do
  if [ -d "skills/$skill" ]; then
    ( cd skills && rm -f "../$skill.skill" && zip -r "../$skill.skill" "$skill" -x '*/.*' >/dev/null )
    echo "built $skill.skill"
  fi
done

echo "done. verify with: unzip -l kochab.skill | head"

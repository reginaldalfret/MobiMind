# Git Migration Baseline: MobiMind

**Timestamp:** 2026-09-11T13:07:00+05:30  
**Project Location:**  
- Windows: E:\Projects\PocketPalAI  
- WSL: /mnt/e/Projects/PocketPalAI  

## Baseline Git Status
- **Current Branch:** main
- **Current HEAD Commit:** 527751 chore(android): drop the hexagon symbol-count payload tripwire (#902)
- **Upstream Origin URL:** https://github.com/a-ghorbani/pocketpal-ai
- **Target Repository:** eginaldalfret/MobiMind
- **GitHub User Authenticated:** eginaldalfret

## Pre-Publication Git Status
`	ext
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  modified:   .husky/commit-msg
  modified:   android/gradle.properties
  modified:   android/gradle/wrapper/gradle-wrapper.properties
  modified:   android/gradlew
  modified:   e2e/scripts/memory-profile.sh
  modified:   metro.config.js
  modified:   scripts/postinstall.sh
`

## Remote Verification
`	ext
origin  https://github.com/a-ghorbani/pocketpal-ai (fetch)
origin  https://github.com/a-ghorbani/pocketpal-ai (push)
`

## Safety Plan
1. Do not push to https://github.com/a-ghorbani/pocketpal-ai.
2. Rename upstream origin to upstream or replace with new GitHub repo origin pointing to https://github.com/reginaldalfret/MobiMind.git.
3. Preserve all original MIT copyright notices.
4. Exclude all multi-gigabyte models (*.gguf), binaries, caches, and test artifacts via .gitignore.

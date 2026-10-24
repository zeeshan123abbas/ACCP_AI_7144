#!/usr/bin/env bash
# Download (clone) an existing repository from GitHub.

# Option A: HTTPS - works everywhere, GitHub asks you to sign in on first push
git clone https://github.com/octocat/Hello-World.git

# Option B: SSH - needs the SSH key from 01-setup-git.sh
git clone git@github.com:octocat/Hello-World.git hello-ssh   # last word = folder name

# Go inside and look around
cd Hello-World
git log --oneline     # full history came with the clone
git remote -v         # "origin" points back to GitHub automatically

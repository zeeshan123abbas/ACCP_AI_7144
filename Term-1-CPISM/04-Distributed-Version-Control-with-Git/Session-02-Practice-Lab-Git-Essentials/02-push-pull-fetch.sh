#!/usr/bin/env bash
# Keeping your computer and GitHub in sync.

# Send your new commits to GitHub
git push                        # same as: git push origin main (after the first -u)

# Download new commits WITHOUT changing your files
git fetch
git status                      # "Your branch is behind 'origin/main' by 1 commit"
git log --oneline main..origin/main   # list the commits you do not have yet

# Download AND merge them into your files
git pull                        # = git fetch + git merge

# Golden rule for beginners: pull before you start work, push when you finish.

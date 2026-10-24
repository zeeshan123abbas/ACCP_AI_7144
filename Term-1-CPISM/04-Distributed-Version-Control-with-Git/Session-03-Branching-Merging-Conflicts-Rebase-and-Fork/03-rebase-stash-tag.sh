#!/usr/bin/env bash
# Advanced everyday commands. Read each block; run them in your own practice repo.

# ---------- Rebase: replay my branch on top of the latest main ----------
git switch feature/gallery
git rebase main                 # my commits now sit after main's newest commit (straight line)
# If a conflict appears: fix the file, then
#   git add <file>  and  git rebase --continue      (or git rebase --abort to cancel)

# ---------- Squash: combine my last 3 commits into one (before pushing) ----------
git rebase -i HEAD~3            # in the editor, change "pick" to "squash" on lines 2 and 3

# ---------- Stash: park unfinished work to switch branch quickly ----------
git stash                       # saves changes and cleans the working folder
git switch main                 # do something urgent...
git switch feature/gallery
git stash pop                   # bring the parked changes back
git stash list                  # see all stashes

# ---------- Cherry-pick: copy ONE commit from another branch ----------
git switch main
git cherry-pick a1b2c3d         # replace with a real hash from git log

# ---------- Tags: mark a release ----------
git tag -a v1.0.0 -m "First release"
git push origin v1.0.0
git tag                         # list tags

# ---------- Move, rename and delete files with Git ----------
git mv old-name.html new-name.html
git rm unused.html
git commit -m "chore: rename and remove pages"

# ---------- Clean up branches ----------
git branch --merged             # branches already merged into the current one
git branch -d feature/gallery   # delete local branch
git push origin --delete feature/gallery   # delete it on GitHub

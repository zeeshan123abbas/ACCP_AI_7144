#!/usr/bin/env bash
# Undoing mistakes - from safest to most dangerous.

# A. Throw away edits in a file you have NOT staged yet
git restore index.html

# B. Unstage a file (keep your edits, just take it out of the box)
git restore --staged index.html

# C. Fix the LAST commit message, or add a forgotten file to it
git add forgotten.css
git commit --amend -m "feat: add home page with styles"
#    ⚠️ Only amend commits you have NOT pushed yet.

# D. Undo a commit that is ALREADY on GitHub: make a new "opposite" commit
git revert HEAD                 # HEAD = the latest commit; history is kept
git push

# E. Move back in LOCAL history (commits not pushed yet)
git reset --soft HEAD~1         # undo commit, keep changes staged
git reset HEAD~1                # undo commit, keep changes in files (default --mixed)
git reset --hard HEAD~1         # ⚠️ undo commit AND delete the changes

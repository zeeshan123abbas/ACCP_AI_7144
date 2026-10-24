#!/usr/bin/env bash
# The everyday Git cycle. Run inside your project folder (e.g. my-website).

# 1. Make two changes
echo "<p>About me</p>" > about.html        # new file  -> "untracked"
echo "<p>Welcome!</p>" >> index.html        # edit file -> "modified"

# 2. What changed?
git status                 # long view
git status -s              # short view: ?? = untracked, M = modified

# 3. See the exact lines that changed (only for tracked files)
git diff

# 4. Stage ONE file and commit it
git add about.html
git commit -m "feat: add about page"

# 5. Stage everything else and commit
git add .                  # "." = all changes in this folder
git commit -m "style: add welcome text to home page"

# 6. Read the history
git log                    # full details
git log --oneline          # one line per commit
git log --oneline --graph --all   # with a branch drawing

# 7. Look at one commit (copy a short hash from the log)
# git show a1b2c3d

#!/usr/bin/env bash
# Feature branch -> merge back into main. Safe to run: it works in a new practice folder.
set -e
mkdir -p branch-demo && cd branch-demo
git init -q

# 1. A first commit on main
echo "<h1>Home</h1>" > index.html
git add . && git commit -q -m "feat: add home page"

# 2. Create a feature branch and switch to it
git switch -c feature/contact

# 3. Work on the branch
echo "<h1>Contact</h1>" > contact.html
git add . && git commit -q -m "feat: add contact page"

# 4. Go back to main: contact.html is NOT here yet
git switch main
ls

# 5. Merge the feature into main.
#    main has no new commits, so Git just moves main forward = "fast-forward" merge
git merge feature/contact
ls

# 6. Delete the finished branch and view history
git branch -d feature/contact
git log --oneline --graph

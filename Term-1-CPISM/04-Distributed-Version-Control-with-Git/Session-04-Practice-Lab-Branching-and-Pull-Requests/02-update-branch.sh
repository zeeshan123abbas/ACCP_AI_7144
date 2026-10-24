#!/usr/bin/env bash
# Your PR says "This branch has conflicts" or "is out-of-date with main".
# Bring the newest main into YOUR branch, fix conflicts on your computer, push again.

git switch feature/3-about-page

# 1. Get the latest commits from GitHub
git fetch origin

# 2. Merge the newest main into your branch
git merge origin/main
#    If you see CONFLICT: open the files, keep the right text, delete the markers, then:
#    git add <file>
#    git commit

# 3. Test the site in the browser, then update the pull request
git push
#    The PR updates automatically - no need to open a new one.

#!/usr/bin/env bash
# Contribute to a project you do NOT own (open-source style).

# 1. On github.com open the project and click "Fork" -> a copy appears under YOUR account.

# 2. Clone YOUR fork (not the original)
git clone https://github.com/YOUR-USERNAME/class-website.git
cd class-website

# 3. Remember the original project as "upstream"
git remote add upstream https://github.com/TEACHER-USERNAME/class-website.git
git remote -v                   # origin = your fork, upstream = original

# 4. Work on a branch
git switch -c fix/typo-in-footer
# ...edit files...
git commit -am "fix: correct spelling in footer"

# 5. Push the branch to YOUR fork
git push -u origin fix/typo-in-footer

# 6. On github.com click "Compare & pull request" -> describe the change -> Create pull request.

# 7. Later, keep your fork up to date with the original
git switch main
git fetch upstream
git merge upstream/main
git push origin main

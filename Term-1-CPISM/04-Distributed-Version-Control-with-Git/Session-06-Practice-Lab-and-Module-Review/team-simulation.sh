#!/usr/bin/env bash
# Practise teamwork ALONE: one computer, two "developers", and a fake GitHub.
# A "bare" repository has no working files - it only stores history, just like GitHub.
set -e
mkdir -p team-sim && cd team-sim

# 1. Create the fake GitHub server
git init -q --bare server.git

# 2. Developer Sara clones it and makes the first commit
git clone -q server.git sara
cd sara
echo "<h1>Team Site</h1>" > index.html
git add . && git commit -q -m "feat: add home page"
git push -q origin main
cd ..

# 3. Developer Bilal clones the same server
git clone -q server.git bilal

# 4. Sara adds a footer and pushes first
cd sara
echo "<footer>Made by Sara</footer>" >> index.html
git commit -q -am "feat: add footer"
git push -q
cd ..

# 5. Bilal (without pulling) adds a menu on his own branch
cd bilal
git switch -q -c feature/menu
echo "<nav>Home | About</nav>" > nav.html
git add . && git commit -q -m "feat: add menu"

# 6. Before merging, Bilal gets Sara's work, then merges his branch into main
git switch -q main
git pull -q                         # brings in Sara's footer
git merge -q --no-edit feature/menu # three-way merge (both sides changed)
git push -q
cd ..

# 7. Sara pulls and now has everything
cd sara
git pull -q
echo "--- Files Sara has now:"
ls
echo "--- Shared history:"
git log --oneline --graph --all

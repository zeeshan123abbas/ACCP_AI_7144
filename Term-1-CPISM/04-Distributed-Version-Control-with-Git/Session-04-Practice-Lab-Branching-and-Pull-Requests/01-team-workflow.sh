#!/usr/bin/env bash
# Team workflow ("GitHub Flow") - each member repeats this for every task.

# 0. Team leader only (once): create the repo on GitHub and add members in
#    Settings -> Collaborators. Everyone else clones it:
git clone https://github.com/TEAM-LEADER/team-portfolio.git
cd team-portfolio

# 1. Always start from the newest main
git switch main
git pull

# 2. One branch per task (use the issue number in the name)
git switch -c feature/3-about-page

# 3. Work and commit in small steps
echo "<h1>About our team</h1>" > about.html
git add about.html
git commit -m "feat: add about page (#3)"

# 4. Push the branch to GitHub
git push -u origin feature/3-about-page

# 5. On github.com: "Compare & pull request" -> write description with "Closes #3"
#    -> choose a reviewer -> Create pull request.

# 6. After the PR is merged on GitHub, clean up locally
git switch main
git pull
git branch -d feature/3-about-page

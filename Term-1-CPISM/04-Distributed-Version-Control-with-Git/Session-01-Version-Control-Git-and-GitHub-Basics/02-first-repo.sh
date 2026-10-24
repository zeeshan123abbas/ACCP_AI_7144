#!/usr/bin/env bash
# Create a project, save it with Git, and push it to GitHub.

# 1. Make a folder and go inside it
mkdir my-website
cd my-website

# 2. Turn the folder into a Git repository (creates a hidden .git folder)
git init

# 3. Create a file
echo "<h1>Hello Git</h1>" > index.html

# 4. Ask Git what changed (index.html is "untracked")
git status

# 5. Put the file in the staging area (the "box" for the next snapshot)
git add index.html

# 6. Save the snapshot with a message
git commit -m "feat: add home page"

# 7. See the history
git log --oneline

# 8. Connect to an EMPTY repository you created on github.com
#    (replace YOUR-USERNAME; use the SSH URL git@github.com:... if you set up SSH)
git remote add origin https://github.com/YOUR-USERNAME/my-website.git

# 9. Upload. -u remembers "origin main" so next time just type: git push
git push -u origin main

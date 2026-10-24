#!/usr/bin/env bash
# One-time Git setup on a new computer. Run these in Git Bash (Windows) or Terminal (Mac/Linux).

# 1. Check Git is installed
git --version

# 2. Tell Git who you are (this name/email is stamped on every commit)
git config --global user.name "Ayesha Khan"
git config --global user.email "ayesha@example.com"   # use the SAME email as your GitHub account

# 3. Name the first branch "main" in every new repository
git config --global init.defaultBranch main

# 4. Use VS Code as the editor for commit messages
git config --global core.editor "code --wait"

# 5. See all your settings
git config --list

# 6. (Optional) Create an SSH key so you can push without typing a password
ssh-keygen -t ed25519 -C "ayesha@example.com"   # press Enter to accept the defaults
cat ~/.ssh/id_ed25519.pub                        # copy this line into GitHub → Settings → SSH and GPG keys
ssh -T git@github.com                            # test: "Hi <username>! You've successfully authenticated"

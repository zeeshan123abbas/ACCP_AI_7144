# Git cheat sheet (Module 04)

## Setup (once)
| Command | Does |
|---------|------|
| `git config --global user.name "Name"` | Set your name |
| `git config --global user.email "you@mail.com"` | Set your email |
| `git config --global init.defaultBranch main` | New repos start on `main` |

## Start
| Command | Does |
|---------|------|
| `git init` | Make the current folder a repo |
| `git clone <url>` | Download a repo with full history |

## Daily cycle
| Command | Does |
|---------|------|
| `git status` / `git status -s` | What changed? |
| `git diff` | Show unstaged line changes |
| `git add <file>` / `git add .` | Stage changes |
| `git commit -m "type: summary"` | Save a snapshot |
| `git log --oneline --graph --all` | History with branches |

## Remote
| Command | Does |
|---------|------|
| `git remote add origin <url>` | Connect to GitHub |
| `git push -u origin main` | First push of a branch |
| `git push` / `git pull` / `git fetch` | Upload / download+merge / download only |

## Branches
| Command | Does |
|---------|------|
| `git branch` | List branches |
| `git switch -c feature/x` | Create and switch |
| `git switch main` | Change branch |
| `git merge feature/x` | Merge into current branch |
| `git rebase main` | Replay current branch on main (own branches only) |
| `git branch -d feature/x` | Delete merged branch |

## Undo
| Command | Does |
|---------|------|
| `git restore <file>` | Discard unstaged edits |
| `git restore --staged <file>` | Unstage |
| `git commit --amend` | Fix last commit (before push) |
| `git revert <hash>` | Undo a pushed commit safely |
| `git reset --soft HEAD~1` | Undo last local commit, keep changes |

## Extras
| Command | Does |
|---------|------|
| `git stash` / `git stash pop` | Park / restore unfinished work |
| `git cherry-pick <hash>` | Copy one commit |
| `git tag -a v1.0.0 -m "msg"` + `git push origin v1.0.0` | Mark a release |
| `git mv a b` / `git rm file` | Rename / delete tracked files |

## Conflict recipe
1. `git status` → see "both modified" files
2. Edit file, keep correct text, delete `<<<<<<<`, `=======`, `>>>>>>>`
3. `git add <file>` → `git commit` (or `git rebase --continue`)

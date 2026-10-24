# Pull request review checklist (for the reviewer)

Be kind, be specific, suggest instead of order.

## Before you read the code
- [ ] The PR title follows `type: summary`
- [ ] The description explains WHAT and WHY, and links the issue
- [ ] The PR is small (ideally under ~300 changed lines)

## Reading the "Files changed" tab
- [ ] Only files related to this task are changed
- [ ] No secrets, passwords, `.env` or `node_modules/` added
- [ ] HTML is indented and valid; images have `alt` text
- [ ] Names of files and classes are clear

## Try it
- [ ] Pulled the branch (`git fetch` + `git switch <branch>`) and opened it in the browser
- [ ] Works on a narrow (phone) screen

## Decide
- **Comment** - questions only
- **Request changes** - something must be fixed first
- **Approve** - ready to merge

Example of a good comment:
> "The button text is white on yellow and hard to read. Could we use `btn-dark` instead?"

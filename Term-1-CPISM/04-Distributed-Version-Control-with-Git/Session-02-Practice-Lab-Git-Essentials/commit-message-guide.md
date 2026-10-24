# Commit message guide (Conventional Commits)

Format:

```
<type>: <short summary in present tense, under 50 characters>

<optional body: WHY you made the change>
```

| Type | Use for | Example |
|------|---------|---------|
| `feat` | A new feature or page | `feat: add contact form` |
| `fix` | A bug fix | `fix: correct broken logo path` |
| `docs` | README or comments only | `docs: add setup steps to README` |
| `style` | Formatting, CSS look (no logic change) | `style: increase hero padding` |
| `refactor` | Code change that is not a fix or feature | `refactor: move scripts to js folder` |
| `chore` | Tooling, config, .gitignore | `chore: ignore node_modules` |

## Good vs bad

| ❌ Bad | ✅ Good |
|--------|---------|
| `update` | `fix: stop navbar overlapping hero on mobile` |
| `asdf` | `feat: add gallery page with 6 images` |
| `changes done!!!` | `docs: explain how to run the site locally` |

**Tips:** one idea per commit · present tense ("add", not "added") · no full stop at the end.

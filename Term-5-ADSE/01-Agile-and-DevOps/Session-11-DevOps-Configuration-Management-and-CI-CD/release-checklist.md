# Release Checklist (Semantic Versioning)

Version: v__.__.__  (MAJOR = breaking change, MINOR = new feature, PATCH = bug fix)

- [ ] All CI checks green on `main`
- [ ] CHANGELOG updated (Added / Changed / Fixed)
- [ ] Version number bumped in code / pubspec / package files
- [ ] Git tag created: `git tag -a v1.4.0 -m "Release 1.4.0"` and pushed
- [ ] Artifact built once and uploaded to the artifact repository
- [ ] Same artifact deployed to staging and smoke-tested
- [ ] Rollback plan written
- [ ] Release notes shared with users/support

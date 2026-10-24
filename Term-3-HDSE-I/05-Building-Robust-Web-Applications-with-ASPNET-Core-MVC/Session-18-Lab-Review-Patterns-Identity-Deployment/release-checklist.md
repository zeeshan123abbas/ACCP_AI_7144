# Release Checklist (ASP.NET Core)

## Code
- [ ] Builds in Release with no warnings you do not understand
- [ ] Unit tests pass (`dotnet test`)
- [ ] No secrets in `appsettings.json` or Git history

## Security
- [ ] HTTPS redirection and HSTS on
- [ ] `[Authorize]` on every private action, roles checked
- [ ] Anti-forgery tokens on all POST forms
- [ ] Passwords via Identity (hashed), lockout on
- [ ] Errors show a friendly page, not a stack trace

## Data
- [ ] Production connection string set as an environment variable
- [ ] Database created/migrated (`dotnet ef database update` or migration bundle)
- [ ] Backup plan agreed

## Hosting
- [ ] `dotnet publish -c Release` output tested locally
- [ ] IIS: Hosting Bundle installed, app pool = No Managed Code
- [ ] Folder permissions for logs/uploads
- [ ] `/health` returns Healthy after deploy

## After release
- [ ] Logs checked for errors in the first hour
- [ ] Smoke test: register, login, main feature, logout

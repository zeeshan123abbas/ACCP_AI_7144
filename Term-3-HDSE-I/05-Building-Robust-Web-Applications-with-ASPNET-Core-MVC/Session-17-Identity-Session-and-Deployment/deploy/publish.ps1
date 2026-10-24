# 1. Build a Release version into the "publish" folder
dotnet publish ..\IdentitySession.csproj -c Release -o C:\inetpub\IdentitySession

# 2. (Run PowerShell as Administrator) turn on IIS
Enable-WindowsOptionalFeature -Online -FeatureName IIS-WebServerRole, IIS-WebServer, IIS-ManagementConsole -All

# 3. Install the ASP.NET Core 8 Hosting Bundle (download from the official .NET site), then restart IIS
net stop was /y
net start w3svc

# 4. Create an app pool (No Managed Code) and a website on port 8080
Import-Module WebAdministration
New-WebAppPool -Name "IdentitySessionPool"
Set-ItemProperty IIS:\AppPools\IdentitySessionPool -Name managedRuntimeVersion -Value ""
New-Website -Name "IdentitySession" -Port 8080 -PhysicalPath "C:\inetpub\IdentitySession" -ApplicationPool "IdentitySessionPool"

# 5. Give the app pool write access so SQLite can create identity.db
icacls "C:\inetpub\IdentitySession" /grant "IIS AppPool\IdentitySessionPool:(OI)(CI)M"

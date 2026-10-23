# system-info.ps1 - print a short report about this PC
# Run:  powershell -ExecutionPolicy Bypass -File .\system-info.ps1

$os  = Get-CimInstance Win32_OperatingSystem
$cpu = Get-CimInstance Win32_Processor | Select-Object -First 1
$ramGB = [math]::Round($os.TotalVisibleMemorySize / 1MB, 1)

Write-Host "===== My PC Report =====" -ForegroundColor Cyan
Write-Host "Computer name : $env:COMPUTERNAME"
Write-Host "Windows       : $($os.Caption) (build $($os.BuildNumber))"
Write-Host "Processor     : $($cpu.Name)"
Write-Host "RAM           : $ramGB GB"

Get-CimInstance Win32_LogicalDisk -Filter "DriveType=3" | ForEach-Object {
    $free  = [math]::Round($_.FreeSpace / 1GB, 1)
    $total = [math]::Round($_.Size / 1GB, 1)
    Write-Host ("Drive {0}      : {1} GB free of {2} GB" -f $_.DeviceID, $free, $total)
}

# make-course-folders.ps1 - create a tidy folder tree for this term
$root = Join-Path $HOME "Documents\ACCP-Term1"
$modules = "01-Office", "02-Web", "03-Bootstrap-jQuery", "04-Git", "05-SEO", "eProject"

foreach ($m in $modules) {
    $path = Join-Path $root $m
    New-Item -ItemType Directory -Path $path -Force | Out-Null
    Write-Host "Created $path"
}
explorer $root   # open the folder when done

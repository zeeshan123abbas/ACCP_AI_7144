# Session 02 - Example 2: the same job with Azure PowerShell (Az module)
# One-time install on your PC:  Install-Module -Name Az -Scope CurrentUser
# (Cloud Shell in PowerShell mode already has it.)

# Step 1: sign in and check the subscription
Connect-AzAccount
Get-AzContext

# Step 2: variables
$resourceGroup = "rg-session02-ps"
$location      = "eastus"
$storageName   = "stps" + (Get-Random -Maximum 99999)

# Step 3: create a resource group
New-AzResourceGroup -Name $resourceGroup -Location $location

# Step 4: create a storage account
New-AzStorageAccount -ResourceGroupName $resourceGroup -Name $storageName `
  -Location $location -SkuName Standard_LRS -Kind StorageV2

# Step 5: list resources, then clean up
Get-AzResource -ResourceGroupName $resourceGroup | Select-Object Name, ResourceType
Remove-AzResourceGroup -Name $resourceGroup -Force

// Session 02 - Example 3: a storage account described as code (Bicep)

// Parameters: values you can change at deploy time
param location string = resourceGroup().location
param storageName string = 'st${uniqueString(resourceGroup().id)}'

// The resource we want Azure to create
resource storage 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: storageName
  location: location
  sku: {
    name: 'Standard_LRS'      // cheapest: 3 copies in one data centre
  }
  kind: 'StorageV2'
  properties: {
    minimumTlsVersion: 'TLS1_2'
  }
}

// Output: a value printed after deployment
output storageAccountName string = storage.name

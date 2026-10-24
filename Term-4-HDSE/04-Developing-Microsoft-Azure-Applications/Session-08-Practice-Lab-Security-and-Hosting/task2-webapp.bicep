// Lab 08 - Task 2: App Service plan + secure web app, as code

param location string = resourceGroup().location
param appName string = 'lab08-${uniqueString(resourceGroup().id)}'

// The plan = the servers that run the app (B1, Linux)
resource plan 'Microsoft.Web/serverfarms@2023-12-01' = {
  name: 'plan-${appName}'
  location: location
  sku: { name: 'B1' }
  kind: 'linux'
  properties: { reserved: true }      // "reserved: true" means Linux
}

// The web app with security switched on
resource webApp 'Microsoft.Web/sites@2023-12-01' = {
  name: appName
  location: location
  identity: { type: 'SystemAssigned' }      // managed identity
  properties: {
    serverFarmId: plan.id
    httpsOnly: true                         // redirect http to https
    siteConfig: {
      linuxFxVersion: 'DOTNETCORE|8.0'
      minTlsVersion: '1.2'
      ftpsState: 'Disabled'                 // no plain FTP uploads
    }
  }
}

output appName string = webApp.name
output url string = 'https://${webApp.properties.defaultHostName}'
output principalId string = webApp.identity.principalId

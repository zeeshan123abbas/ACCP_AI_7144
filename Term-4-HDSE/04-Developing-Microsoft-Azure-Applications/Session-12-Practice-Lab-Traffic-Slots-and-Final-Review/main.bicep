// Lab 12 - Task 1: the whole production setup as code
// Log Analytics + Application Insights + S1 plan + web app + staging slot + alert

param location string = resourceGroup().location
param appName string = 'final-${uniqueString(resourceGroup().id)}'

// 1. Where logs are stored
resource workspace 'Microsoft.OperationalInsights/workspaces@2023-09-01' = {
  name: 'law-${appName}'
  location: location
  properties: {
    sku: { name: 'PerGB2018' }
    retentionInDays: 30
  }
}

// 2. Application Insights, saving into the workspace
resource insights 'Microsoft.Insights/components@2020-02-02' = {
  name: 'ai-${appName}'
  location: location
  kind: 'web'
  properties: {
    Application_Type: 'web'
    WorkspaceResourceId: workspace.id
  }
}

// 3. Standard plan (needed for slots)
resource plan 'Microsoft.Web/serverfarms@2023-12-01' = {
  name: 'plan-${appName}'
  location: location
  sku: { name: 'S1' }
  kind: 'linux'
  properties: { reserved: true }
}

// 4. Production web app
resource webApp 'Microsoft.Web/sites@2023-12-01' = {
  name: appName
  location: location
  identity: { type: 'SystemAssigned' }
  properties: {
    serverFarmId: plan.id
    httpsOnly: true
    siteConfig: {
      linuxFxVersion: 'DOTNETCORE|8.0'
      minTlsVersion: '1.2'
      ftpsState: 'Disabled'
      healthCheckPath: '/health'
      appSettings: [
        { name: 'APPLICATIONINSIGHTS_CONNECTION_STRING', value: insights.properties.ConnectionString }
        { name: 'APP_VERSION', value: '1.0' }
        { name: 'ENVIRONMENT_NAME', value: 'Production' }
      ]
    }
  }
}

// 5. Staging slot with its own settings
resource stagingSlot 'Microsoft.Web/sites/slots@2023-12-01' = {
  parent: webApp
  name: 'staging'
  location: location
  properties: {
    serverFarmId: plan.id
    httpsOnly: true
    siteConfig: {
      linuxFxVersion: 'DOTNETCORE|8.0'
      appSettings: [
        { name: 'APPLICATIONINSIGHTS_CONNECTION_STRING', value: insights.properties.ConnectionString }
        { name: 'APP_VERSION', value: '2.0' }
        { name: 'ENVIRONMENT_NAME', value: 'Staging' }
      ]
    }
  }
}

// 6. Make ENVIRONMENT_NAME a sticky (slot) setting
resource stickySettings 'Microsoft.Web/sites/config@2023-12-01' = {
  parent: webApp
  name: 'slotConfigNames'
  properties: {
    appSettingNames: [ 'ENVIRONMENT_NAME' ]
  }
}

// 7. Alert: more than 5 server errors (HTTP 5xx) in 5 minutes
resource errorAlert 'Microsoft.Insights/metricAlerts@2018-03-01' = {
  name: 'alert-5xx-${appName}'
  location: 'global'
  properties: {
    severity: 2
    enabled: true
    scopes: [ webApp.id ]
    evaluationFrequency: 'PT1M'
    windowSize: 'PT5M'
    criteria: {
      'odata.type': 'Microsoft.Azure.Monitor.SingleResourceMultipleMetricCriteria'
      allOf: [
        {
          name: 'TooManyServerErrors'
          criterionType: 'StaticThresholdCriterion'
          metricName: 'Http5xx'
          operator: 'GreaterThan'
          threshold: 5
          timeAggregation: 'Total'
        }
      ]
    }
  }
}

output appName string = webApp.name
output productionUrl string = 'https://${webApp.properties.defaultHostName}'
output stagingUrl string = 'https://${stagingSlot.properties.defaultHostName}'

#!/bin/bash
# Session 02 - Example 5: set up Azure Monitor logs and Application Insights

RESOURCE_GROUP="rg-session02"
LOCATION="eastus"

# Step 1: create a Log Analytics workspace (the place where logs are stored)
az monitor log-analytics workspace create \
  --resource-group $RESOURCE_GROUP \
  --workspace-name law-session02 \
  --location $LOCATION

# Step 2: read the workspace's full id
WORKSPACE_ID=$(az monitor log-analytics workspace show \
  --resource-group $RESOURCE_GROUP --workspace-name law-session02 \
  --query id --output tsv)

# Step 3: create Application Insights that sends data to that workspace
az monitor app-insights component create \
  --app ai-session02 \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION \
  --workspace $WORKSPACE_ID

# Step 4: print the connection string (your app needs this value)
az monitor app-insights component show \
  --app ai-session02 --resource-group $RESOURCE_GROUP \
  --query connectionString --output tsv

# Step 5: see who did what in this resource group in the last hour
az monitor activity-log list --resource-group $RESOURCE_GROUP --offset 1h \
  --query "[].{operation:operationName.localizedValue, status:status.value}" --output table

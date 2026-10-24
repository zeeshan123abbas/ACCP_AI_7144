#!/bin/bash
# Session 02 - Example 4: deploy the Bicep file with Azure Resource Manager

RESOURCE_GROUP="rg-session02"

# Step 1: preview what WOULD change (nothing is created yet)
az deployment group what-if \
  --resource-group $RESOURCE_GROUP \
  --template-file 03-storage.bicep

# Step 2: deploy for real
az deployment group create \
  --resource-group $RESOURCE_GROUP \
  --template-file 03-storage.bicep

# Step 3: run it again - ARM sees the resource already matches, nothing breaks
az deployment group create \
  --resource-group $RESOURCE_GROUP \
  --template-file 03-storage.bicep \
  --query properties.outputs

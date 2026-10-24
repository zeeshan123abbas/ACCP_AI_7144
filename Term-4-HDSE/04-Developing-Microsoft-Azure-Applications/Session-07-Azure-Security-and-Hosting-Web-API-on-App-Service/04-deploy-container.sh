#!/bin/bash
# Session 07 - Example 4: run the same API as a container on Azure Container Apps
# Run from the Session-06 folder after copying the Dockerfile there.

RESOURCE_GROUP="rg-session07"

# Step 1: one command builds the image in Azure, stores it in a registry and runs it
az containerapp up --name students-api-container --resource-group $RESOURCE_GROUP \
  --location eastus --source . --ingress external --target-port 8080

# Step 2: print the public address
az containerapp show --name students-api-container --resource-group $RESOURCE_GROUP \
  --query properties.configuration.ingress.fqdn --output tsv

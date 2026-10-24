#!/bin/bash
# Session 11 - Example 3: Deployment Center options from the CLI

RESOURCE_GROUP="rg-session11"
APP_NAME="slotdemo-XXXXX"

# Option A: continuous deployment from a GitHub repo (creates a GitHub Actions workflow)
az webapp deployment github-actions add --name $APP_NAME --resource-group $RESOURCE_GROUP \
  --repo "your-github-user/slotdemo" --branch main --slot staging --login-with-github

# Option B: run a Docker image from Docker Hub or Azure Container Registry
# az webapp config container set --name $APP_NAME --resource-group $RESOURCE_GROUP \
#   --container-image-name mcr.microsoft.com/dotnet/samples:aspnetapp

# Option C: publish files directly (what we did with zip deploy)
# az webapp deploy --name $APP_NAME --resource-group $RESOURCE_GROUP --src-path app.zip --type zip

# See the deployment history
az webapp log deployment list --name $APP_NAME --resource-group $RESOURCE_GROUP --output table

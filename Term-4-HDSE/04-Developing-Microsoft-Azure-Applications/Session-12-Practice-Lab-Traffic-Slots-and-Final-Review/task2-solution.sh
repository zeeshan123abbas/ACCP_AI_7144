#!/bin/bash
# Lab 12 - Task 2 solution: deploy infrastructure, then code to both slots
# Run from this folder; the app code is ../Session-11-.../SlotDemo

RESOURCE_GROUP="rg-lab12"
LOCATION="eastus"
APP_FOLDER="../Session-11-Traffic-Management-Monitoring-and-Deployment-Slots/SlotDemo"

# Step 1: infrastructure from Bicep
az group create --name $RESOURCE_GROUP --location $LOCATION
APP_NAME=$(az deployment group create --resource-group $RESOURCE_GROUP \
  --template-file main.bicep --query properties.outputs.appName.value --output tsv)
echo "App: $APP_NAME"

# Step 2: build the code once
dotnet publish $APP_FOLDER -c Release -o publish
(cd publish && zip -r ../app.zip .)

# Step 3: deploy the same package to production and to staging
az webapp deploy --resource-group $RESOURCE_GROUP --name $APP_NAME --src-path app.zip --type zip
az webapp deploy --resource-group $RESOURCE_GROUP --name $APP_NAME --slot staging --src-path app.zip --type zip

# Step 4: smoke test both, then swap
bash smoke-test.sh https://$APP_NAME-staging.azurewebsites.net && \
  az webapp deployment slot swap --resource-group $RESOURCE_GROUP --name $APP_NAME \
    --slot staging --target-slot production

curl https://$APP_NAME.azurewebsites.net

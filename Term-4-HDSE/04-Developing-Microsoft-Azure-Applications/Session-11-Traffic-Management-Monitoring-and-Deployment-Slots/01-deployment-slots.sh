#!/bin/bash
# Session 11 - Example 1: zero-downtime releases with deployment slots
# Run from inside the SlotDemo folder.

RESOURCE_GROUP="rg-session11"
LOCATION="eastus"
APP_NAME="slotdemo-$RANDOM"

# Step 1: slots need the Standard (S1) tier or higher
az group create --name $RESOURCE_GROUP --location $LOCATION
az appservice plan create --name plan-slotdemo --resource-group $RESOURCE_GROUP --sku S1 --is-linux
az webapp create --name $APP_NAME --resource-group $RESOURCE_GROUP \
  --plan plan-slotdemo --runtime "DOTNETCORE:8.0"

# Step 2: deploy version 1.0 to production
dotnet publish -c Release -o publish && (cd publish && zip -r ../app.zip .)
az webapp config appsettings set --name $APP_NAME --resource-group $RESOURCE_GROUP \
  --settings APP_VERSION=1.0
az webapp deploy --name $APP_NAME --resource-group $RESOURCE_GROUP --src-path app.zip --type zip

# Step 3: create a "staging" slot and give it version 2.0
az webapp deployment slot create --name $APP_NAME --resource-group $RESOURCE_GROUP --slot staging
az webapp config appsettings set --name $APP_NAME --resource-group $RESOURCE_GROUP \
  --slot staging --settings APP_VERSION=2.0
az webapp deploy --name $APP_NAME --resource-group $RESOURCE_GROUP --slot staging \
  --src-path app.zip --type zip

# Step 4: a "sticky" slot setting stays with the slot during a swap
az webapp config appsettings set --name $APP_NAME --resource-group $RESOURCE_GROUP \
  --slot-settings ENVIRONMENT_NAME=Production
az webapp config appsettings set --name $APP_NAME --resource-group $RESOURCE_GROUP \
  --slot staging --slot-settings ENVIRONMENT_NAME=Staging

echo "Production: https://$APP_NAME.azurewebsites.net"
echo "Staging:    https://$APP_NAME-staging.azurewebsites.net"

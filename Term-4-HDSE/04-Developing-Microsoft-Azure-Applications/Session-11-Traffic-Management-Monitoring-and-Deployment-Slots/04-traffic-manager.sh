#!/bin/bash
# Session 11 - Example 4: DNS-based failover between two regions with Traffic Manager

RESOURCE_GROUP="rg-session11"
SUFFIX=$RANDOM

# Step 1: the same app in two regions (Standard tier is required for Traffic Manager)
az appservice plan create --name plan-east --resource-group $RESOURCE_GROUP --location eastus --sku S1 --is-linux
az appservice plan create --name plan-west --resource-group $RESOURCE_GROUP --location westeurope --sku S1 --is-linux
az webapp create --name web-east-$SUFFIX --resource-group $RESOURCE_GROUP --plan plan-east --runtime "DOTNETCORE:8.0"
az webapp create --name web-west-$SUFFIX --resource-group $RESOURCE_GROUP --plan plan-west --runtime "DOTNETCORE:8.0"

# Step 2: a Traffic Manager profile using Priority routing (primary + backup)
az network traffic-manager profile create --name tm-accp-$SUFFIX --resource-group $RESOURCE_GROUP \
  --routing-method Priority --unique-dns-name accp-tm-$SUFFIX

# Step 3: add both apps as endpoints; priority 1 is used while it is healthy
EAST_ID=$(az webapp show --name web-east-$SUFFIX --resource-group $RESOURCE_GROUP --query id --output tsv)
WEST_ID=$(az webapp show --name web-west-$SUFFIX --resource-group $RESOURCE_GROUP --query id --output tsv)
az network traffic-manager endpoint create --name east --profile-name tm-accp-$SUFFIX \
  --resource-group $RESOURCE_GROUP --type azureEndpoints --target-resource-id $EAST_ID --priority 1
az network traffic-manager endpoint create --name west --profile-name tm-accp-$SUFFIX \
  --resource-group $RESOURCE_GROUP --type azureEndpoints --target-resource-id $WEST_ID --priority 2

echo "Visit: http://accp-tm-$SUFFIX.trafficmanager.net  (stop web-east to see failover)"

#!/bin/bash
# Session 09 - Example 3: create a Function App and send it a queue message

RESOURCE_GROUP="rg-session09"
LOCATION="eastus"
STORAGE_NAME="stfunc09$RANDOM"
FUNC_APP="func-session09-$RANDOM"

# Step 1: resource group and the storage account Functions needs
az group create --name $RESOURCE_GROUP --location $LOCATION
az storage account create --name $STORAGE_NAME --resource-group $RESOURCE_GROUP \
  --location $LOCATION --sku Standard_LRS

# Step 2: a Function App on the Consumption (pay-per-run) plan
az functionapp create --name $FUNC_APP --resource-group $RESOURCE_GROUP \
  --storage-account $STORAGE_NAME --consumption-plan-location $LOCATION \
  --runtime dotnet-isolated --runtime-version 8 --functions-version 4 --os-type Linux

# Step 3: publish the code (run inside HelloFunctions; needs Azure Functions Core Tools)
# func azure functionapp publish $FUNC_APP

# Step 4: drop a message in the "orders" queue to trigger ProcessOrder
az storage queue create --name orders --account-name $STORAGE_NAME --auth-mode key
az storage message put --queue-name orders --account-name $STORAGE_NAME \
  --content "Order 101: 2 x Azure Fundamentals book" --auth-mode key

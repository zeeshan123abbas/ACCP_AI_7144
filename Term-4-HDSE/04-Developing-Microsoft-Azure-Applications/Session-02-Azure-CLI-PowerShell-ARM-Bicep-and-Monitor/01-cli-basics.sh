#!/bin/bash
# Session 02 - Example 1: everyday Azure CLI commands

RESOURCE_GROUP="rg-session02"
LOCATION="eastus"
# storage names must be globally unique, lowercase, 3-24 letters/numbers
STORAGE_NAME="stsession02$RANDOM"

# Step 1: create a resource group
az group create --name $RESOURCE_GROUP --location $LOCATION

# Step 2: create a storage account inside it
az storage account create \
  --name $STORAGE_NAME \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION \
  --sku Standard_LRS

# Step 3: list everything in the group as a table
az resource list --resource-group $RESOURCE_GROUP --output table

# Step 4: use --query (JMESPath) to print only the names
az resource list --resource-group $RESOURCE_GROUP --query "[].name" --output tsv

# Step 5: get help for any command
az storage account create --help

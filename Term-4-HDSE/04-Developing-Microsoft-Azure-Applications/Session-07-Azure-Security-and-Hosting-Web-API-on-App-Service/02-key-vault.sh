#!/bin/bash
# Session 07 - Example 2: keep secrets in Azure Key Vault, not in code

RESOURCE_GROUP="rg-session07"
LOCATION="eastus"
VAULT_NAME="kv-session07-$RANDOM"       # globally unique, 3-24 characters
echo "Vault name: $VAULT_NAME  (write it down for the next script)"

# Step 1: create the vault using Azure RBAC for permissions
az keyvault create --name $VAULT_NAME --resource-group $RESOURCE_GROUP \
  --location $LOCATION --enable-rbac-authorization true

# Step 2: give YOURSELF permission to manage secrets in this vault
MY_ID=$(az ad signed-in-user show --query id --output tsv)
VAULT_ID=$(az keyvault show --name $VAULT_NAME --query id --output tsv)
az role assignment create --role "Key Vault Secrets Officer" \
  --assignee $MY_ID --scope $VAULT_ID

# Step 3: store a secret (wait ~1 minute if you get "Forbidden": roles take time)
az keyvault secret set --vault-name $VAULT_NAME --name SqlConnection \
  --value "Server=tcp:demo.database.windows.net;Initial Catalog=SchoolDb;..."

# Step 4: read it back
az keyvault secret show --vault-name $VAULT_NAME --name SqlConnection --query value --output tsv

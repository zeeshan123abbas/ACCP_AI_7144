#!/bin/bash
# Session 07 - Example 3: host the Session 06 Students API on Azure App Service
# Run this from INSIDE the Session-06 StudentsApi folder.

RESOURCE_GROUP="rg-session07"
APP_NAME="students-api-$RANDOM"     # becomes https://<APP_NAME>.azurewebsites.net
VAULT_NAME="kv-session07-XXXXX"     # the vault name printed by 02-key-vault.sh

# Step 1: build and deploy in one command (creates the plan and web app)
az webapp up --name $APP_NAME --resource-group $RESOURCE_GROUP \
  --runtime "DOTNETCORE:8.0" --os-type Linux --sku B1

# Step 2: allow HTTPS only
az webapp update --name $APP_NAME --resource-group $RESOURCE_GROUP --https-only true

# Step 3: give the web app its own identity (a managed identity, no password)
PRINCIPAL_ID=$(az webapp identity assign --name $APP_NAME \
  --resource-group $RESOURCE_GROUP --query principalId --output tsv)

# Step 4: let that identity READ secrets from the vault
VAULT_ID=$(az keyvault show --name $VAULT_NAME --query id --output tsv)
az role assignment create --role "Key Vault Secrets User" \
  --assignee-object-id $PRINCIPAL_ID --assignee-principal-type ServicePrincipal \
  --scope $VAULT_ID

# Step 5: an app setting that POINTS to the secret (a Key Vault reference)
# Uncomment when the secret holds a REAL Azure SQL connection string:
# az webapp config appsettings set --name $APP_NAME --resource-group $RESOURCE_GROUP \
#   --settings "ConnectionStrings__AzureSql=@Microsoft.KeyVault(VaultName=$VAULT_NAME;SecretName=SqlConnection)"

echo "Try: https://$APP_NAME.azurewebsites.net/api/students"

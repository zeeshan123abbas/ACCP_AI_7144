#!/bin/bash
# Lab 08 - Task 3 solution: infrastructure, secret, permission, code - in order
# Run from this Session-08 folder in Cloud Shell.

RESOURCE_GROUP="rg-lab08"
LOCATION="eastus"
VAULT_NAME="kv-lab08-$RANDOM"

# Step 1: resource group + web app from Bicep; keep the outputs in variables
az group create --name $RESOURCE_GROUP --location $LOCATION
APP_NAME=$(az deployment group create --resource-group $RESOURCE_GROUP \
  --template-file task2-webapp.bicep --query properties.outputs.appName.value --output tsv)
PRINCIPAL_ID=$(az webapp identity show --name $APP_NAME --resource-group $RESOURCE_GROUP \
  --query principalId --output tsv)

# Step 2: Key Vault + a secret (you need Secrets Officer to write)
az keyvault create --name $VAULT_NAME --resource-group $RESOURCE_GROUP \
  --location $LOCATION --enable-rbac-authorization true
VAULT_ID=$(az keyvault show --name $VAULT_NAME --query id --output tsv)
az role assignment create --role "Key Vault Secrets Officer" \
  --assignee $(az ad signed-in-user show --query id --output tsv) --scope $VAULT_ID
sleep 60   # give the role assignment time to apply
az keyvault secret set --vault-name $VAULT_NAME --name DemoApiKey --value "lab08-demo-key-123"

# Step 3: the web app's identity may READ secrets
az role assignment create --role "Key Vault Secrets User" \
  --assignee-object-id $PRINCIPAL_ID --assignee-principal-type ServicePrincipal --scope $VAULT_ID

# Step 4: app setting that references the secret
az webapp config appsettings set --name $APP_NAME --resource-group $RESOURCE_GROUP \
  --settings "DemoApiKey=@Microsoft.KeyVault(VaultName=$VAULT_NAME;SecretName=DemoApiKey)"

# Step 5: publish the code as a zip and deploy it
cd HealthApi
dotnet publish -c Release -o publish
cd publish && zip -r ../app.zip . && cd ..
az webapp deploy --resource-group $RESOURCE_GROUP --name $APP_NAME --src-path app.zip --type zip

# Step 6: test - expect "secretLoaded": true
curl https://$APP_NAME.azurewebsites.net/health

#!/bin/bash
# Lab 10 - Task 3 solution: publish the function through APIM with a subscription key

RESOURCE_GROUP="rg-lab10"
APIM_NAME="apim-lab10-xxxx"            # your APIM instance
FUNC_APP="func-lab10-xxxx"             # your Function App
FUNC_KEY=$(az functionapp keys list --name $FUNC_APP --resource-group $RESOURCE_GROUP \
  --query functionKeys.default --output tsv)

# Step 1: an API that forwards to the Function App
az apim api create --resource-group $RESOURCE_GROUP --service-name $APIM_NAME \
  --api-id feedback --path feedback --display-name "Feedback API" \
  --service-url "https://$FUNC_APP.azurewebsites.net/api" --protocols https

# Step 2: one operation: POST /feedback
az apim api operation create --resource-group $RESOURCE_GROUP --service-name $APIM_NAME \
  --api-id feedback --operation-id submit --display-name "Submit feedback" \
  --method POST --url-template "/feedback"

# Step 3: a product that requires a subscription key, containing the API
az apim product create --resource-group $RESOURCE_GROUP --service-name $APIM_NAME \
  --product-id students --product-name "Students" --subscription-required true --state published
az apim product api add --resource-group $RESOURCE_GROUP --service-name $APIM_NAME \
  --product-id students --api-id feedback

echo "Function key for the backend (store it as an APIM named value): $FUNC_KEY"
echo "Next: Portal > APIM > Subscriptions > add one for the Students product, copy its key."

#!/bin/bash
# Session 09 - Example 4: put API Management (a gateway) in front of your API

RESOURCE_GROUP="rg-session09"
APIM_NAME="apim-session09-$RANDOM"
BACKEND_URL="https://students-api-XXXX.azurewebsites.net"   # your Session 07 web app

# Step 1: create the gateway (Consumption tier is pay-per-call and quick to create)
az apim create --name $APIM_NAME --resource-group $RESOURCE_GROUP \
  --publisher-name "ACCP Student" --publisher-email student@example.com \
  --sku-name Consumption

# Step 2: import the API from its Swagger (OpenAPI) document
az apim api import --resource-group $RESOURCE_GROUP --service-name $APIM_NAME \
  --api-id students --path students --display-name "Students API" \
  --specification-format OpenApi \
  --specification-url "$BACKEND_URL/swagger/v1/swagger.json" \
  --service-url $BACKEND_URL

# Step 3: create revision 2 to test changes safely (clients still use revision 1)
az apim api revision create --resource-group $RESOURCE_GROUP --service-name $APIM_NAME \
  --api-id students --api-revision 2 --api-revision-description "Add rate limit policy"

echo "Gateway URL: https://$APIM_NAME.azure-api.net/students/api/students"

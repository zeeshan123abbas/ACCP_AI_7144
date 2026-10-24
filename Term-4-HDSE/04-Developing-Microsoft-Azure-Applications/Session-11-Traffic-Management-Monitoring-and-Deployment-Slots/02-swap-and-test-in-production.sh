#!/bin/bash
# Session 11 - Example 2: send some users to staging, then swap

RESOURCE_GROUP="rg-session11"
APP_NAME="slotdemo-XXXXX"     # the name printed by 01-deployment-slots.sh

# Step 1: "testing in production" - 20% of visitors go to the staging slot
az webapp traffic-routing set --name $APP_NAME --resource-group $RESOURCE_GROUP \
  --distribution staging=20

# Step 2: happy with it? stop the split and swap staging into production
az webapp traffic-routing clear --name $APP_NAME --resource-group $RESOURCE_GROUP
az webapp deployment slot swap --name $APP_NAME --resource-group $RESOURCE_GROUP \
  --slot staging --target-slot production

# Step 3: production now shows Version 2.0 (and still says "Production")
curl https://$APP_NAME.azurewebsites.net

# Step 4: problem found? swap again to roll back in seconds
# az webapp deployment slot swap --name $APP_NAME --resource-group $RESOURCE_GROUP \
#   --slot staging --target-slot production

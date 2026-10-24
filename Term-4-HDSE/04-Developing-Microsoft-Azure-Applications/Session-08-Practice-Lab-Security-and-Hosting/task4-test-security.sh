#!/bin/bash
# Lab 08 - Task 4: check that the security settings really work
APP_NAME="lab08-xxxxxxxx"     # paste your app name

# 1. plain http should redirect (301) to https because httpsOnly = true
curl -s -o /dev/null -w "http  -> %{http_code}\n" http://$APP_NAME.azurewebsites.net/health

# 2. https should answer 200
curl -s -o /dev/null -w "https -> %{http_code}\n" https://$APP_NAME.azurewebsites.net/health

# 3. list who has access to the resource group (RBAC review)
az role assignment list --resource-group rg-lab08 \
  --query "[].{who:principalName, role:roleDefinitionName}" --output table

# 4. clean up when finished
# az group delete --name rg-lab08 --yes --no-wait

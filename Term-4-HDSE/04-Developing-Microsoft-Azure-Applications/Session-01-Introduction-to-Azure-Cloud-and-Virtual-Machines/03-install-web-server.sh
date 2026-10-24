#!/bin/bash
# Session 01 - Example 3: turn the VM into a web server

RESOURCE_GROUP="rg-session01"
VM_NAME="vm-web01"

# Step 1: open port 80 so browsers can reach the VM
az vm open-port --resource-group $RESOURCE_GROUP --name $VM_NAME --port 80

# Step 2: run a command INSIDE the VM to install the nginx web server
az vm run-command invoke \
  --resource-group $RESOURCE_GROUP \
  --name $VM_NAME \
  --command-id RunShellScript \
  --scripts "sudo apt-get update && sudo apt-get install -y nginx"

# Step 3: get the IP again and open http://<ip> in your browser
az vm show --resource-group $RESOURCE_GROUP --name $VM_NAME \
  --show-details --query publicIps --output tsv

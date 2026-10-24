#!/bin/bash
# Session 01 - Example 2: create a small Linux virtual machine

# Step 1: choose names once and reuse them
RESOURCE_GROUP="rg-session01"
LOCATION="eastus"          # pick a region that your subscription allows
VM_NAME="vm-web01"

# Step 2: create a resource group (a folder for related resources)
az group create --name $RESOURCE_GROUP --location $LOCATION

# Step 3: create the VM (Ubuntu, smallest burstable size, SSH keys auto-made)
az vm create \
  --resource-group $RESOURCE_GROUP \
  --name $VM_NAME \
  --image Ubuntu2204 \
  --size Standard_B1s \
  --admin-username azureuser \
  --generate-ssh-keys

# Step 4: print the public IP address of the VM
az vm show --resource-group $RESOURCE_GROUP --name $VM_NAME \
  --show-details --query publicIps --output tsv

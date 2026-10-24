#!/bin/bash
# Session 01 - Example 4: stop, start and delete to save money

RESOURCE_GROUP="rg-session01"
VM_NAME="vm-web01"

# Step 1: see the VM's current power state
az vm get-instance-view --resource-group $RESOURCE_GROUP --name $VM_NAME \
  --query "instanceView.statuses[1].displayStatus" --output tsv

# Step 2: deallocate = stop AND release the hardware (compute billing stops)
az vm deallocate --resource-group $RESOURCE_GROUP --name $VM_NAME

# Step 3: start it again when you need it
az vm start --resource-group $RESOURCE_GROUP --name $VM_NAME

# Step 4: when the lab is finished, delete the whole resource group
# (this deletes the VM, disk, IP and network in one go)
az group delete --name $RESOURCE_GROUP --yes --no-wait

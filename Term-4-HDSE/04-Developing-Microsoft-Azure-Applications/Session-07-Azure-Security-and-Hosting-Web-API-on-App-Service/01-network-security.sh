#!/bin/bash
# Session 07 - Example 1: a virtual network protected by a Network Security Group

RESOURCE_GROUP="rg-session07"
LOCATION="eastus"

az group create --name $RESOURCE_GROUP --location $LOCATION

# Step 1: a virtual network (private address space) with one subnet
az network vnet create --resource-group $RESOURCE_GROUP --name vnet-app \
  --address-prefix 10.0.0.0/16 --subnet-name snet-web --subnet-prefix 10.0.1.0/24

# Step 2: a Network Security Group = a list of allow/deny rules
az network nsg create --resource-group $RESOURCE_GROUP --name nsg-web

# Step 3: allow HTTPS (443) from the internet; lower number = checked first
az network nsg rule create --resource-group $RESOURCE_GROUP --nsg-name nsg-web \
  --name Allow-HTTPS --priority 100 --direction Inbound --access Allow \
  --protocol Tcp --destination-port-ranges 443

# Step 4: block SSH (22) from the internet
az network nsg rule create --resource-group $RESOURCE_GROUP --nsg-name nsg-web \
  --name Deny-SSH --priority 200 --direction Inbound --access Deny \
  --protocol Tcp --destination-port-ranges 22

# Step 5: attach the NSG to the subnet so every VM in it is protected
az network vnet subnet update --resource-group $RESOURCE_GROUP --vnet-name vnet-app \
  --name snet-web --network-security-group nsg-web

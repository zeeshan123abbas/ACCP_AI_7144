#!/bin/bash
# Session 01 - Example 1: sign in and look around your Azure account
# Run in Azure Cloud Shell (Bash) or any terminal with Azure CLI installed.

# Step 1: sign in (Cloud Shell users are already signed in, so skip this)
az login

# Step 2: show which subscription you are using right now
az account show --output table

# Step 3: list the regions (data centre locations) you can use
az account list-locations --query "[].name" --output tsv

# Step 4: list resource groups you already have (probably none yet)
az group list --output table

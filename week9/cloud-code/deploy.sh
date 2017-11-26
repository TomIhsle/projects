resourceGroup=uwiotRg
preferredRegion=eastus
storageName=uwiotstorage

# Create a resource group.
echo
echo "Create a resource group called $resourceGroup within region $preferredRegion"
az group create --location $preferredRegion --name $resourceGroup

# Create storage
# echo
# echo "Create a storage account"
# az storage account create --resource-group $resourceGroup --name $storageName --location $preferredRegion --sku Standard_LRS

# # # Find the storage key for newly created storage account. Uses JMESPath syntax for --query
# echo
# echo "Finding first storage API key for Storage Account $storageName"
# storageAccountKey=$(az storage account keys list --resource-group $resourceGroup --account-name $storageName --query [0].value --output tsv)
# echo $storageAccountKey

# # # Find storage connection string. Uses JMESPath syntax for --query
# echo
# echo "Finding storage connection string for Storage Account $storageName"
# storageConnectionString=$(az storage account show-connection-string --resource-group $resourceGroup --name $storageName --query connectionString --output tsv)
# echo $storageConnectionString

# echo
# echo "Create container called images"
# az storage container create --name images \
#                             --public-access container \
#                             --account-name $storageName \
#                             --account-key $storageAccountKey
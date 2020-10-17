# Load libraries
from azure.storage.blob import BlockBlobService
import pandas as pd

# Define parameters
storageAccountName = "sanrockytar"
storageKey         = "vk/lXABb39pgfxZ4+EUrSLhJ1vgmpH0aDUeQibDHk4bowoNwxBfCCa0xyuuV6yV/t3pLYEbYyGmMvS1Y3L245w=="
containerName      = "output"

# Establish connection with the blob storage account
blobService = BlockBlobService(account_name=storageAccountName,
                               account_key=storageKey
                               )

# Load iris dataset from the task node
df = pd.read_csv("iris.csv")

# Subset records
df = df[df['Species'] == "setosa"]

# Save the subset of the iris dataframe locally in task node
df.to_csv("iris_setosa.csv", index = False)

# Upload iris dataset
blobService.create_blob_from_path(containerName, "iris_setosa.csv", "iris_setosa.csv")
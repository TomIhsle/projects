#!/usr/bin/python

import time
import os
import camera
from azure.storage.blob import BlockBlobService # For setting up Block storage service
from azure.storage.blob import ContentSettings # For sending blobs

# Happens 
def upload_blob(filename, filepath):
    if os.getenv("AZURE_STORAGE_ACCOUNT") and os.getenv("AZURE_STORAGE_KEY"):
        # Instantiate blob service
        block_blob_service = BlockBlobService(account_name=os.getenv("AZURE_STORAGE_ACCOUNT"),
                                              account_key=os.getenv("AZURE_STORAGE_KEY"))

        blob_name = filename

        # Upload blob
        try:
            block_blob_service.create_blob_from_path(
                os.getenv("AZURE_STORAGE_CONTAINER_NAME"),
                blob_name,
                filepath,
                content_settings=ContentSettings(content_type='image/jpg'))

            print 'Uploaded the photo: {}'.format(blob_name)
            print 'Check Storage Explorer under: {} > {} > {}'.format(os.getenv("AZURE_STORAGE_ACCOUNT"),
                                                                      os.getenv("AZURE_STORAGE_CONTAINER_NAME"),
                                                                      blob_name)
            print 'It is accessible at: https://{}.blob.core.windows.net/{}/{}'.format(os.getenv("AZURE_STORAGE_ACCOUNT"),
                                                                                       os.getenv("AZURE_STORAGE_CONTAINER_NAME"),
                                                                                       blob_name)
        except:
            print 'Unable to upload: {}'.format(blob_name)
    else:
        print 'Set your AZURE_STORAGE_ACCOUNT and AZURE_STORAGE_KEY in the .env file.'

if "ENVIRONMENT" in os.environ:
    filename = ""
    filepath = ""

    if os.getenv("ENVIRONMENT") in ["production", "PRODUCTION"]:
        if "TIMEOUT_MS" in os.environ and "BLOB_TYPE" in os.environ:
            timeout_ms = int(os.getenv("TIMEOUT_MS"))

            if os.getenv("BLOB_TYPE") in ["IMAGE", "image"]:
                # Takes photo
                filename, filepath = camera.take_photo(timeout_ms)
            elif os.getenv("BLOB_TYPE") in ["VIDEO", "video"]:
                # Take video
                filename, filepath = camera.take_video(timeout_ms)

    # Upload the image or video to Azure
    # View blobs in storage account easily using: http://storageexplorer.com/
    upload_blob(filename, filepath)
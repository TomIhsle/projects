#!/usr/bin/python

import time
import os
import camera
from azure.storage.blob import BlockBlobService # For setting up Block storage service
from azure.storage.blob import ContentSettings # For sending blobs
import redis

r = redis.StrictRedis(host='queue', port=6379, db=0)

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

            blob_url = "https://{}.blob.core.windows.net/{}/{}".format(os.getenv("AZURE_STORAGE_ACCOUNT"),
                                                                       os.getenv("AZURE_STORAGE_CONTAINER_NAME"),
                                                                       blob_name)

            # Send blob_url to the queue
            r.rpush("imageprocessing", blob_url)
            
            print 'It is accessible at: {}'.format(blob_url)
        except:
            print 'Unable to upload: {}'.format(blob_name)
    else:
        print 'Set your AZURE_STORAGE_ACCOUNT and AZURE_STORAGE_KEY in the .env file.'

def take_blob(blob_type, timeout_ms):
    filename = ""
    filepath = ""

    if blob_type == "PHOTO":
        # Takes photo
        filename, filepath = camera.take_photo(timeout_ms)
    elif blob_type == "VIDEO":
        # Take video
        filename, filepath = camera.take_video(timeout_ms)

    # Upload image or video to Azure
    # View blobs in storage account easily using: http://storageexplorer.com/
    upload_blob(filename, filepath)

def take_photo(timeout_ms):
    take_blob("PHOTO", timeout_ms)

def take_video(timeout_ms):
    take_blob("VIDEO", timeout_ms)
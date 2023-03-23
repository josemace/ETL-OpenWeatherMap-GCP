import os
import logging
from google.cloud import storage

#pip install --upgrade google-cloud-storage. 
def csv_to_bucket(project_id, path_to_file, bucket_name):
    """ Upload the given csv file to a bucket"""

    try:
        # Initiate Client with the user credentials provided by using the gcloud CLI
        storage_client = storage.Client(project=project_id)

        #print(buckets = list(storage_client.list_buckets())

        # Select the bucket where to upload the file
        bucket = storage_client.get_bucket(bucket_name)

        # Create the file/object
        blob_name = os.path.basename(path_to_file)
        blob = bucket.blob(blob_name)

        # Upload the file
        blob.upload_from_filename(path_to_file)
        
        #returns a public url
        return blob.public_url

    except Exception as e:
        logging.error(f"[Exception] {e} on {e.__traceback__.tb_frame} line {e.__traceback__.tb_lineno}")


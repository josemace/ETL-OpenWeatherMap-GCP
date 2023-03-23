import logging
from google.cloud import bigquery
from google.cloud import storage


def blob_to_bigquery(project_id, blob_uri, dataset_id, table_name):
    """Load the data from a given Google Cloud Storage file into Google BigQuery"""

    try:
        # Set up a client object for interacting with Google BigQuery
        bigquery_client = bigquery.Client(project=project_id)

        # Set up a job config object with the CSV options
        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,
            autodetect=True
        )

        # Create a job to load the data from the CSV file into a BigQuery table
        job = bigquery_client.load_table_from_uri(
            source_uris=blob_uri,
            destination=f"{project_id}.{dataset_id}.{table_name}",
            job_config=job_config
        )

        # Wait for the job to complete
        job.result()

    except Exception as e:
        logging.error(f"[Exception] {e} on {e.__traceback__.tb_frame} line {e.__traceback__.tb_lineno}")

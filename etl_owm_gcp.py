from open_weather_map.owm import collect_weather_data
from gcp.storage import csv_to_bucket
from gcp.bigquery import blob_to_bigquery
from utils.configuration import Configuration

if __name__ == "__main__":

    config = Configuration()

    OWM = config.get("OPEN_WEATHER_MAP")
    cities = OWM.get("CITIES").split(',')

    OUTPUT_FILE = config.get("OUTPUT").get("PATH")

    GCP = config.get("GOOGLE_CLOUD")
    PROJECT_ID = GCP.get("PROJECT_ID")
    STORAGE_BUCKET = GCP.get("STORAGE_BUCKET")
    BIGQUERY_DATASET = GCP.get("BIGQUERY_DATASET")

    # Save the weather data from OWM API into a csv file
    collect_weather_data(OWM, cities, OUTPUT_FILE)

    # Upload the csv file to Google Cloud Storage
    blob_uri = csv_to_bucket(PROJECT_ID, OUTPUT_FILE, STORAGE_BUCKET)

    # Load the data from the Google Cloud Storage file into a BigQuery table
    blob_to_bigquery(PROJECT_ID, blob_uri, BIGQUERY_DATASET, "weather_data")

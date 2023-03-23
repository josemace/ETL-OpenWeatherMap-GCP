# ETL OpenWeatherMap API data to GCP

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## About <a name="about"></a>

ETL OWM to GCP is in charge of collecting the weather data from the OpenWeatherMap API given a list of cities in the config file and saving it into a csv file.

Once this csv file is correctly saved, the process uploads it to Google Cloud Storage into a given bucket with the same filename.

After uploading the file succesfully, it loads the data into Google BigQuery. The data is loaded into a BQ table with the same name than the file inside of a given dataset-id.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine.

### Requirements <a name = "requirements"></a>

1. [gcloud CLI](https://cloud.google.com/sdk/docs/install)
2. You'll need to have authentication set up for your Google Cloud Storage and Google BigQuery accounts. You can do this by following the instructions in the [official documentation](https://cloud.google.com/docs/authentication/application-default-credentials#personal)
3. This script is programmed with [Python 3.9](https://www.python.org/downloads/release/python-390/)

### Installation <a name = "installation"></a>

1. Create a new virtual environment in your local machine: `virtualenv venv`
2. Activate the environment `source venv/Scripts/activate` (Windows) or `source venv/bin/activate`
3. Install all the requirements using pip or your preferred package manager: `pip install -r requirements.txt`
4. Create a `config.ini` with the [config schema](#config_schema), fill the variables.

After this steps your are ready to execute the script.

## Usage <a name = "usage"></a>

Once everything is correctly setup, to execute the script you need to run:

`python -m etl_owm_gcp`

### Config Schema <a name = "config_schema"></a>

Rename `config-default.ini` to `config.ini` and replace values between <> with your variables

```
[OPEN_WEATHER_MAP]
URL = http://api.openweathermap.org/
API_KEY = <YOUR OPENWEATHERMAP API KEY>
CITIES = <LIST OF CITIES SEPARATED BY COMMA>
UNITS = metric

[GOOGLE_CLOUD]
CREDENTIALS_FILE = <CREDENTIALS FILE PATH>
PROJECT_ID = <PROJECT-ID>
STORAGE_BUCKET = <BUCKET-ID>
BIGQUERY_DATASET = <DATASET-ID>

[LOGS]
ERROR = log/error.log

[OUTPUT]
PATH = tmp/weather_data.csv
```

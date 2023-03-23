import os
import logging
from datetime import datetime
import pandas as pd
from .api_request import request
from utils.configuration import Configuration


def collect_weather_data(owm_config = Configuration().get("OPEN_WEATHER_MAP"), cities = [], outfile = "tmp/weather_data.csv"):
    """Collect data from OpenWeatherMap API and save it into a given csv file"""
    
    OWM = owm_config

    # Sets the units of measurement
    units = OWM.get("UNITS")
    if units is None:
        units = "standard"

    # Set up lists to store the data
    data = []

    try:
        # Loop through the cities and get the weather data
        for city in cities:
            # Set up API request parameters
            params = {"q": city, "units": units}

            # Send API request
            response = request("GET", "/data/2.5/weather", params=params)

            # Get the data from the response
            if response == False:
                return False
            weather_data = response.json()

            # Extract the relevant information and add it to the list
            data.append({
                "Timestamp": datetime.now(),
                "City": city,
                "Temperature": weather_data["main"]["temp"],
                "Minimum Temperature": weather_data["main"]["temp_min"],
                "Maximum Temperature": weather_data["main"]["temp_max"],
                "Humidity": weather_data["main"]["humidity"],
                "Pressure": weather_data["main"]["pressure"],
                "Wind Speed": weather_data["wind"]["speed"]
            })

        # Create a pandas DataFrame from the data
        df = pd.DataFrame(data)

        # Save the DataFrame to a CSV file
        os.makedirs(os.path.dirname(outfile), exist_ok=True)
        df.to_csv(outfile, index=False)
        
        return True
    
    except Exception as e:
        logging.error(f"[Exception] {e} on {e.__traceback__.tb_frame} line {e.__traceback__.tb_lineno}")

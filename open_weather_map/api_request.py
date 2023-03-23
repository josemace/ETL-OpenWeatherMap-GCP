import logging 
import requests as req
from utils.configuration import Configuration

def request(method: str, uri: str, body = None, headers = None, with_auth=True, params = None, return_all_response=False):
    OWM = Configuration().get("OPEN_WEATHER_MAP")
    API_URL = OWM.get("URL")
    API_KEY = OWM.get("API_KEY")
    method = method.upper()
    
    if with_auth:
        if params == None:
            params = {}
        params["appid"] = API_KEY

    response = None
    if method == "GET":
        response = req.get(f"{API_URL}{uri}",headers=headers, params=params, data=body)
    elif method == "PUT":
        response = req.put(f"{API_URL}{uri}",headers=headers, params=params, data=body)
    elif method == "POST":
        response = req.post(f"{API_URL}{uri}",headers=headers, params=params, data=body)
    elif method == "DELETE":
        response = req.delete(f"{API_URL}{uri}",headers=headers, params=params, data=body)
    else:
        response = req.head(f"{API_URL}{uri}", params=params)

    if response.status_code == 200:
        return response
    elif 400 <= response.status_code <= 599:
        error, error_description = response.json().values()
        logging.error(f"[Code {response.status_code}] [{error}] {error_description}")
    return False

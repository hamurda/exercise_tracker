import os
import requests

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": 0,
}



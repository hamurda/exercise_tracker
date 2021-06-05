import os
import requests
import datetime as dt

# Nutritionix "Natural Language for Exercise" API
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_ENP = "https://api.sheety.co/4d884657710d6bbd0f940e24f186a0bb/workoutTracking/workouts"
EXERCISE_ENDP = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_AUTH = os.environ.get("SHEETY_AUTH")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

exercise_params = {
    "query": "ran 3 miles",
    # "gender": "female",
    # "weight_kg": 72.5,
    # "height_cm": 167.64,
    # "age": 30
}

response_exr = requests.post(url=EXERCISE_ENDP, json=exercise_params, headers=headers)
data = response_exr.json()

exercise_found = data['exercises'][0]['name']
duration = data['exercises'][0]['duration_min']
cal = data['exercises'][0]['nf_calories']

now = dt.datetime.now()
date = now.date()
time = now.time()

sheety_headers = {
    "Authorization": SHEETY_AUTH
}

sheety_params = {
    "workout":
        {
            "date": str(date),
            "time": str(time),
            "exercise": exercise_found,
            "duration": duration,
            "calories": cal,
        }
}

get_response_sheety = requests.get(url=SHEETY_ENP, headers= sheety_headers)
get_response_sheety.raise_for_status()
print(get_response_sheety.json())

# post_response_sheety = requests.post(url=SHEETY_ENP, json=sheety_params)
# post_response_sheety.raise_for_status()
# print(post_response_sheety.json())

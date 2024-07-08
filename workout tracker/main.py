import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
URL_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}
exercise = input("enter exercises you did ")
url_parameters = {
    "query": exercise
}

data = requests.post(url=URL_ENDPOINT, headers=headers, json=url_parameters)
workout_data = data.json()
# print(workout_data)
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in workout_data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    headers = {
        "Authorization": "Basic bnVsbDpudWxs",
    }

    sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs, auth=(USERNAME, PASSWORD))

    # print(sheet_response.text)

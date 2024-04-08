# Libraries
import requests
from datetime import datetime
# constants
from secrets import *


nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = f"https://api.sheety.co/{SHEETY_LOGIN}/{SHEETY_NAME}/{SHEETY_TYPE}"
exercise_text = input("Tell me which exercises you did: ")

headers = {
    # "Content-Type": "application/json",
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(nutritionix_endpoint, json=parameters, headers=headers)
result = response.json()


# generate a new row of data
today_date = datetime.now().strftime("%m/%d/%Y")
now_time = datetime.now().strftime("%X")
print(result)

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=headers)

    print(sheet_response.text)

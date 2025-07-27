import requests


API_ID = "d5120ff3"
API_KEY = 'ce1dfb1d73379a4f4797a0675ccacfb6'



GENDER = "MALE"
WEIGHT_KG = 60
HEIGHT_CM = 2
AGE = 20

APP_ID = API_ID
API_KEY = API_KEY

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
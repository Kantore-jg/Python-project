import requests
from datetime import datetime

MY_LAT = 51.489334
MY_LNG = -0.144055

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()
# print(data)

# longitude = data["iss_position"]["longitude"]
# latitude =data["iss_position"]["latitude"]
# iss_positon = (longitude,latitude)
# print(iss_positon)

parameters ={
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0,
    }

response =  requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"]
# .split("T")[1].split(":")[0]
sunset = data["results"]["sunset"]
# .split("T")[1].split(":")[0]

time_now = datetime.now()
print(sunset)
print(sunrise)
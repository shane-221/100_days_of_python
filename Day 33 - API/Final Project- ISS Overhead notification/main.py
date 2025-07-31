import requests
from datetime import datetime


#----------------------------------------------Constants---------------------------------------------------------------#
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

#----------------------------------------------- API Request ----------------------------------------------------------#
# Todo : Raise the request  for the ISS Position
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

# Todo: Raise the request for your position
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
    # Todo' Pull the hour in which the sun rises and sets
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(f"sunrise:{sunrise}")
#-----------------------------------Checking against the requests to send email----------------------------------------#
time_now = datetime.now()
print(time_now)


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.




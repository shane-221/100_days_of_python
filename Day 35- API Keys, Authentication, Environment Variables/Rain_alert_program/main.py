import requests



#-------------------------------------------------- Constants----------------------------------------------------------#
OWM_ENDPOINT= "https://api.openweathermap.org/data/2.5/forecast?"
API_KEY= "3e24f9a482c9a6d6cd7749d499de293e"

weather_paramas={
    "lon" : -0.127758,
    "lat" : 51.507351,
    "appid" : API_KEY,
    "cnt": 4
   }

#------------------------------------------------- Request the data----------------------------------------------------#
response =requests.get(url=OWM_ENDPOINT, params=weather_paramas )
response.raise_for_status()
print(response)

#------------------------------------------------ Storing and Using the data-------------------------------------------#
# Todo: storing the data as a json file
weather_data = response.json()
# Todo: getting the codes for all the items.
#print(weather_data["list"][0]["weather"][0]["id"])
weather_codes =[x["weather"][0]["id"]for x in weather_data["list"] ]

if 700 in weather_codes:
    print(" Bring an umbrella")

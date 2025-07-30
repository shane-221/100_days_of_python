import requests

MY_LAT=51.507351
MY_LNG = -0.127758


# Todo: Parameters
parameters ={
        "lat":MY_LAT,
        "lng":MY_LNG,
        "formatted": 0
}



# Todo: Need to provide the required parameters
response = requests.get(url= "https://api.sunrise-sunset.org/json", params= parameters)
response.raise_for_status()


# Todo: Getting the data as a JSON Format
data= response.json()

# Todo:
sunrise= data["results"]["sunrise"]
sunset = data ["results"]["sunset"]

print(sunset)
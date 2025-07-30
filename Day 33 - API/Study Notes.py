import requests


# Todo: Initialiting the request
response = requests.get(url = "http://api.open-notify.org/iss-now.json")

# Todo: raise for status tells you which error it is
print(response.raise_for_status())

# Todo: Getting the data back ito json format and accessing specific part sof the json 
data =response.json()["iss_position"]["longitude"]
print(data)
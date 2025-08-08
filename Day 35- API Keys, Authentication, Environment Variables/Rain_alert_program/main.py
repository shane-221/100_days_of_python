import requests
import smtplib
import os



#-------------------------------------------------- Constants----------------------------------------------------------#
OWM_ENDPOINT= "https://api.openweathermap.org/data/2.5/forecast?"
API_KEY= os.environ.get("API_KEY")
    # Check to see how it works
print(f"API_KEY loaded: {API_KEY}")

weather_paramas={
    "lon" : -0.127758,
    "lat" : 51.507351,
    "appid" : API_KEY,
    "cnt": 4
   }
MY_EMAIL= os.environ.get("MY_EMAIL")
PASSWORD= os.environ.get("PASSWORD")
TO_EMAIL=os.environ.get("TO_EMAIL")
#------------------------------------------------- Request the data----------------------------------------------------#
response =requests.get(url=OWM_ENDPOINT, params=weather_paramas )
response.raise_for_status()
print(response)

#------------------------------------------------ Storing and Using the data-------------------------------------------#
# Todo: storing the data as a json file
weather_data = response.json()
# Todo: getting the codes for all the items.
#print(weather_data["list"][0]["weather"][0]["id"])
weather_codes =[int(x["weather"][0]["id"]) for x in weather_data["list"] ]



#---------------------------------------------- Sending an email -----------------------------------------------------#
# Can use the email module to send email if it rains ---> run it in the moning using Python Anywhere and host the code
## on the cloud.

if 700 in weather_codes:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=TO_EMAIL,
                            msg=f"Subject: It will rain!!\n Bring an umbrella please")
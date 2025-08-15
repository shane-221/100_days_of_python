#---------------------------------------Import modules-----------------------------------------------------------------#
import requests
from datetime import datetime


#-------------------------------------------Constants that are universal to the code-----------------------------------#
# tODO : Header data for the calorie request
headers ={
    "x-app-key" :"345f31cc816e55e9990480a85fdc449e",
    "x-app-id": "8e74a439"
}
# Todo: Calorie constants
calorie_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
user_query= input("Tell me which exercises you did?")

# Todo: Sheet Constants
sheet_url= "https://api.sheety.co/9752de018a3428b69d12669130155572/workoutTracker/sheet1'"

#---------------------------------------------------Calorie request----------------------------------------------------#
# Todo : Parameters for the calorie API
exercise_parameters = {
    "weight_kg" : 80,
    "height_cm" : 194,
    "age": 26,
    "gender": "male",
    "query": user_query
                    }

# Todo: Request for the exercise parameters to get the calories and time
post_request = requests.post(url=calorie_url, headers=headers, json=exercise_parameters )
    # This is a response object. Then need to convert it into json to be usable
data =post_request.json()

#--------------------------------------------sheetly request-----------------------------------------------------------#
# Todo: Parameter for the Sheetly api to put data into the excel sheet.
date_now= datetime.now()
exercise = data["exercises"][0]["user_input"]
duration=  data["exercises"][0]["duration_min"]
calories  = data["exercises"][0]["nf_calories"]

print(exercise)
print(duration)
print(calories)


sheet_params= {"Date":f"{date_now}",
               "Time": f"{date_now}",
               "Exercise":{exercise},
               "Duration":{duration},
                "Calories":{calories}
                }

# Todo; Send request for the sheetly to google sheets
sheet_request= requests.post(url = sheet_url)


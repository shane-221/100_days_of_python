#---------------------------------------Import modules-----------------------------------------------------------------#
import requests


#-------------------------------------------Constants that are universal to the code-----------------------------------#

headers ={
    "x-app-key" :"345f31cc816e55e9990480a85fdc449e",
    "x-app-id": "8e74a439"
}

url = "https://trackapi.nutritionix.com/v2/natural/exercise"
user_query= input("Tell me which exercises you did?")

#---------------------------------------------------Parameters---------------------------------------------------------#
exercise_parameters = {
    "weight_kg" : 80,
    "height_cm" : 194,
    "age": 26,
    "gender": "male",
    "query": user_query
                    }




#-------------------------------------------------Requests-------------------------------------------------------------#
# Todo: Request for the calories
post_request = requests.post(url=url, headers=headers, json=exercise_parameters )


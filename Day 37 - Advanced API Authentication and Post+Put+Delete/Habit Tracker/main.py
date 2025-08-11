#---------------------------------------------Import functions---------------------------------------------------------#
import requests

#-----------------------------------------------Parameters for the request---------------------------------------------#
url_endpoint= "https://pixe.la/v1/users"
user_params ={
    "token":"qwertyuiop1998!",
    "username":"shane98",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
            }

#-------------------------------------------Post request---------------------------------------------------------------#
    # Todo: creating a new user using the arguments provided and the use of json data as a function. 
request = requests.post(url=url_endpoint,json=user_params)
print(request.text)
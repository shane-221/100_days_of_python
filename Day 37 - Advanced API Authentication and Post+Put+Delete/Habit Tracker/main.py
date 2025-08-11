#---------------------------------------------Import functions---------------------------------------------------------#
import requests
from openpyxl.formula.tokenizer import Token

#-----------------------------------------------Constants--------------------------------------------------------------#
TOKEN = "qwertyuiop1998!"
USERNAME = "shane98"
AGREE_TERMS_OF_SERVICE = "yes"
NOT_MINOR = "yes"
headers = {"X-USER-TOKEN":TOKEN}


#-----------------------------------------------Parameters for the request---------------------------------------------#
url_endpoint= "https://pixe.la/v1/users"
# user_params ={
#     "token": TOKEN,
#     "username":USERNAME,
#     "agreeTermsOfService": AGREE_TERMS_OF_SERVICE,
#     "notMinor":NOT_MINOR
#             }

graph_endpoint =f"{url_endpoint}/{USERNAME}/graphs"
graph_params ={
    "id":"graph1",
    "name": "Running graph",
    "unit":"KM",
    "type":"float",
    "color": "momiji"
}

#-------------------------------------------Post request---------------------------------------------------------------#
    # Todo: creating a new user using the arguments provided and the use of json data as a function.
# request = requests.post(url=url_endpoint,json=user_params)
# print(request.text)

#--------------------------------------Post request for a  graph-------------------------------------------------------#
request = requests.post(url=graph_endpoint,json=graph_params, headers= headers)
print(request.text)
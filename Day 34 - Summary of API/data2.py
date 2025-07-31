import requests
#------------------------------------------Constants-------------------------------------------------------------------#
AMOUNT= 30
#------------------------------------------API Request-----------------------------------------------------------------#
response= requests.get(url=f"https://opentdb.com/api.php?amount={AMOUNT}&type=boolean")

data = response.json()
dataset ={i["question"]:i["correct_answer"]for i in data["results"]}
print(dataset)
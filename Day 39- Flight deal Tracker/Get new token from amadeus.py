import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY= os.getenv("amadeus_api_key")
API_SECRET =os.getenv("amadeus_api_secret")
print( API_SECRET)
print(API_KEY)



amadeus_url= os.getenv("amadeus_bearer_token")
header = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
body = {
    'grant_type': 'client_credentials',
    'client_id': API_KEY,
    'client_secret': API_SECRET
}
try:
    connection =requests.post(url=amadeus_url, headers = header, data =body)
    print(f"Status Code:{connection.status_code}")
except Exception as e:
    print (f"There is an exception:{e}")
# Purpose:  This section looks at the IATA Codes and populates them.

import requests
import os
from dotenv import load_dotenv
load_dotenv()



# ----------------------------------------Sheetly key information------------------------------------------------------#
# Todo: Prep part for the initial request


SHEET_URL = os.getenv("sheet_url")
SHEET_TOKEN =os.getenv("sheetly_token")
sheetly_header ={"Authorization":SHEET_TOKEN}



#------------------------------------------Get request to sheetly to pull all the data----------------------------------#
# Todo: Sending a get request
try:
    data_iata_codes = requests.get(url= SHEET_URL,  headers=sheetly_header)
except Exception as e:
    print(F" There is an error:{e}")
finally:
    # Use list comprehension to update the data
    sheetly_data = data_iata_codes.json()



#-----------------------------------Getting Countries matched to Codes in Amadeus--------------------------------------#
# Todo: Getting a dictionary of interested countries:( line number: IATA Code)
countries_iata_code ={ x["city"]: (int(x["id"]),x["iataCode"]) for x in sheetly_data["prices"]}

for i in countries_iata_code:
    # Todo: First check to see if the IATA Codes are populated. If not you neeed to connect ot Amadeus and find the code

    payload_data={"price":{
        "iataCode": "Testing"}
    }
    if countries_iata_code[i][1]=="":
        send_iata_code_request = requests.put(url=  f"{SHEET_URL}/{countries_iata_code[i][0]}",
                                              headers=sheetly_header,
                                              json = payload_data)
        print( send_iata_code_request.status_code)






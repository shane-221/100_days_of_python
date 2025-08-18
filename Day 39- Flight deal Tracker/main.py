# Purpose:  This section looks at the IATA Codes and populates them.

import requests
import os


# ----------------------------------------Pulling the data from Sheetly------------------------------------------------#
# Todo: Prep part for the initial request
sheet_url= os.environ.get("sheetly_url")
sheetly_token =os.environ.get("sheetly_token")
sheetly_header ={"Authorization": sheetly_token}



# Todo: Sending a get request
try:
    data_iata_codes= requests.get(url= sheet_url,  headers=sheetly_header)
except Exception as e:
    print(F" There is an error:{e}")
finally:
    # Use list comprehension to update the data
    sheetly_data = data_iata_codes.json()



#-----------------------------------Getting Countries for  the Amadeus API---------------------------------------------#
# Todo: Getting a dictionary of interested countries and their prices as key valur pairs for comparison.
countries_iata_code ={ x["city"]: (int(x["id"]),x["iataCode"]) for x in sheetly_data["prices"]}

for i in countries_iata_code:
    # Todo: First check to see if the IATA Codes are populated. If not you neeed to connect ot Amadeus and find the code

    payload_data={"price":{
        "iataCode": "Testing"}
    }
    if countries_iata_code[i][1]=="":
        send_iata_code_request = requests.put(url=  f"{sheet_url}/{countries_iata_code[i][0]}",
                                              headers=sheetly_header,
                                              json = payload_data)
        print( send_iata_code_request.status_code)






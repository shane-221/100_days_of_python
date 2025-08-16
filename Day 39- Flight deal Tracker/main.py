# Purpose:  This section looks at the IATA Codes and populates them.

import requests

# ----------------------------------------Pulling the data from Sheetly------------------------------------------------#
# Todo: Prep part for the initial request
sheet_url= "https://api.sheety.co/9752de018a3428b69d12669130155572/me:FlightDeals/prices"
sheetly_token ="Basic bnVsbDpudWxs"
sheetly_header ={"Authorization": sheetly_token}

# Todo: Sending a get request
try:
    data_iata_codes= requests.get(url= sheet_url,  headers=sheetly_header)
except Exception as e:
    print(F" There is an error:{e}")
finally:
    # Use list comprehension to update the data
    iata_data = []



#------------------------------------------ Getting codes from the Amadeus API-----------------------------------------#
for i in iata_data["prices"]:
    print()




# ------------------------------------------Place the codes into the Sheetly API---------------------------------------#


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
    iata_data = []



#------------------------------------------ Getting codes from the Amadeus API-----------------------------------------#
for i in iata_data["prices"]:
    print()




# ------------------------------------------Place the codes into the Sheetly API---------------------------------------#


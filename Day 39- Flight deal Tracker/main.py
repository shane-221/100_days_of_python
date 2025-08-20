# Purpose:  This section looks at the IATA Codes and populates them.



from New_token_from_amadeus import *
from dotenv import load_dotenv
load_dotenv()
import requests
import os


# ----------------------------------------Sheetly key information------------------------------------------------------#
# Todo: Prep part for the initial request


SHEET_URL = os.getenv("sheet_url")
SHEET_TOKEN =os.getenv("sheetly_token")
sheetly_header ={"Authorization":SHEET_TOKEN}

amadeus_city_url =f"{os.getenv("amadeus_url")}/reference-data/locations"

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
# Todo: Getting a dictionary of interested countries:( line number: IATA Code) to be used in request etc
countries_iata_code ={ x["city"]: (int(x["id"]),x["iataCode"]) for x in sheetly_data["prices"]}

get_token = BearerToken()
get_header_token = {"Authorization": get_token.get_new_token()}

    # Placed outside the loop to make sure that rate limit is not met.
for i in countries_iata_code:
    # Todo: First check to see if the IATA Codes are populated. If not you neeed to connect ot Amadeus and find the code
    if countries_iata_code[i][1]=="":
        # Todo : Now in the conditional item. Need to check the current item against Amadeus
        city = {"keyword": i ,
                "subType": "CITY"}

        # Todo:sending request with the missing item and authorization.
        try:
            amadeus_request= requests.get(url= amadeus_city_url,params= city, headers = get_header_token )
            amadeus_request.raise_for_status()
            data = amadeus_request.json()

        except Exception as e:
            print(f" There is an error:{e}")

        # Todo: adjust the old country_iata_code with the new IATA Code:
        print(data["data"][0]["iataCode"])



        # # Todo: Sending the final data through sheetly to excel
        # send_iata_code_request = requests.put(url=  f"{SHEET_URL}/{countries_iata_code[i][0]}",
        #                                       headers=sheetly_header,
        #                                       json = payload_data)
        # print( send_iata_code_request.status_code)






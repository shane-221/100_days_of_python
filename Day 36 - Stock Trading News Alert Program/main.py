#------------------------------------------------Imports---------------------------------------------------------------#
import requests
import os

from unicodedata import digit

#---------------------------------------------------Constants ---------------------------------------------------------#
STOCK = "IBM"
COMPANY_NAME = "Tesla Inc"
API_KEY= os.environ.get("API_KEY")
url="http://www.alphavantage.co/query?"

#-------------------------------------------------Step 1 AND 2---------------------------------------------------------#
    #Todo: Creating the parameters withe the required arguments for data
price_parameters ={
        "apikey": API_KEY,
        "function":"GLOBAL_QUOTE",
        "symbol": STOCK
}
    # Todo: Sending the request FOR the data
price_request= requests.get(url=url, params= price_parameters)
data= price_request.json()
print(data)


    # Todo : Pulling the relevant variables out( Current Price, Yesterdays price,and changes

close_price=float((data["Global Quote"]["08. previous close"]).strip())
current_price= float((data["Global Quote"]["05. price"]).strip())
percent_change = float(round((((current_price- close_price)/ close_price)*100), 4))







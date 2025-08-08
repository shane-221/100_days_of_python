#------------------------------------------------Imports---------------------------------------------------------------#
import requests


#---------------------------------------------------Constants ---------------------------------------------------------#
STOCK = "IBM"
COMPANY_NAME = "Tesla Inc"
API_KEY= "JK6ZEULVQTWQL5E4"
url="http://www.alphavantage.co/query?"


#---------------------------------------------------Steps 1 and 2------------------------------------------------------#
    #Todo: Creating the parameters withe the required arguments
parameters ={
        "apikey": API_KEY,
        "function":"TIME_SERIES_DAILY",
        "symbol": STOCK
}
    # Todo: Sending the request
connection = requests.get(url=url, params= parameters)
connection.raise_for_status()
print (connection)

data= connection.json()
print(data)











## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


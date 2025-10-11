#------------------------------------------------Imports---------------------------------------------------------------#
import requests
import os



# #---------------------------------------------------Constants ---------------------------------------------------------#
STOCK = "IBM"
COMPANY_NAME = "IBM"
PRICE_API_KEY= os.environ.get("PRICE_API_KEY")
PRICE_url="http://www.alphavantage.co/query?"
#
NEWS_URL= "https://newsapi.org/v2/everything?"
NEWS_API_KEY=os.environ.get("NEWS_API_KEY")

#
# #-------------------------------------------------Step 1 AND 2---------------------------------------------------------#
    #Todo: Creating the parameters withe the required arguments for data
price_parameters ={
        "apikey": PRICE_API_KEY,
        "function":"GLOBAL_QUOTE",
        "symbol": STOCK
}
    # Todo: Sending the request FOR the data
price_request= requests.get(url=PRICE_url, params= price_parameters)
data= price_request.json()



    # Todo : Pulling the relevant variables out( Current Price, Yesterdays price,and changes

close_price=float((data["Global Quote"]["08. previous close"]).strip())
current_price= float((data["Global Quote"]["05. price"]).strip())
#
#----------------------------------------Step 3 and Step 4-------------------------------------------------------------#
percent_change = float(round((((current_price- close_price)/ close_price)*100), 4))
#
    # Todo: Calrifing condition to send the email
if percent_change<-10 or percent_change>10:
    pass

news_parameters={
            "q": STOCK,
            "apiKey":NEWS_API_KEY,
            "to": "2025-08-09",
            "from" : "2025-08-08",
            "language" :"en",
            "sort": "popularity",
            "pageSize": "2"
                }
    # Todo: News email request
news_request = requests.get(url=NEWS_URL, params=  news_parameters)
news_request.raise_for_status()
news_data = news_request.json()
    # Todo: Converting the data into a useful format: using list comprehesion to make it easier( Could use JSON as well)
article_list=[ x for x in news_data["articles"]]
with open(file= "./ File to Send", mode= "w") as file:
    f"{COMPANY_NAME}: {percent_change}"
    "Articles:\n"
    for i in article_list:
        f"""
        Title:{source["title"]}\n
            Name of the author:{source["author"]}\n
            Summary:{source["description"]}\n\n
        """



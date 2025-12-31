#------------------------------------------------Imports---------------------------------------------------------------#

import os
from API_Requests.stock_request_api import *
from API_Requests.news_request_api import *


#---------------------------------------------------Constants ---------------------------------------------------------#
STOCK = "IBM"
COMPANY_NAME = "IBM"
PRICE_API_KEY= os.environ.get("PRICE_API_KEY")
PRICE_url="http://www.alphavantage.co/query?"
#
NEWS_URL= "https://newsapi.org/v2/everything?"
NEWS_API_KEY=os.environ.get("NEWS_API_KEY")

#
#-------------------------------------------------Step 1 AND 2---------------------------------------------------------#

    # Todo : Running the API reuquest for price using Classes and Exception handling
stock =StockApi(STOCK, PRICE_API_KEY, PRICE_url)
price_data = stock.price_request()
print(price_data)

    # Todo : Pulling the relevant variables out( Current Price, Yesterdays price,and changes


close_price=float((price_data["Global Quote"]["08. previous close"]).strip())
current_price= float((price_data["Global Quote"]["05. price"]).strip())



#------------------------------------------Step 3 ---------------------------------------------------------------------#
percent_change = float(round((((current_price- close_price)/ close_price)*100), 4))

#--------------------------------------------------Step 4--------------------------------------------------------------#

# Todo: Calrifing condition to send the email
# if percent_change<-10 or percent_change>10:
    # Todo: News email request
news = NewsApi(stock, NEWS_API_KEY, NEWS_URL)
news_data = news.news_request()


#--------------------------------------------------Step 5--------------------------------------------------------------#

    # Given the conditions are met. The email needs to0 e sent to the individual.
#
# article_list=[ x for x in news_data["articles"]]
#
# with open(file= "./ File to Send", mode= "w") as file:
#     f"{COMPANY_NAME}: {percent_change}"
#     "Articles:\n"
#     for i in article_list:
#         f"""
#         Title:{source["title"]}\n
#             Name of the author:{source["author"]}\n
#             Summary:{source["description"]}\n\n
#         """


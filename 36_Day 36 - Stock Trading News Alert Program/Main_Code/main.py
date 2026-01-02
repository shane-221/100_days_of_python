#------------------------------------------------Imports---------------------------------------------------------------#

import os
from Structures.stock_request_api import *
from Structures.news_request_api import *
from dotenv import load_dotenv
load_dotenv(dotenv_path="../Storage_files/.env")
from Structures.company_website_section import *

#---------------------------------------------------Constants ---------------------------------------------------------#
STOCK = "IBM"
COMPANY_NAME = "IBM"
PRICE_API_KEY= os.getenv("PRICE_API_KEY")
PRICE_url=os.getenv("PRICE_url")

NEWS_URL= os.getenv("NEWS_URL")
NEWS_API_KEY=os.getenv("NEWS_API_KEY")

#
#-------------------------------------------------Step 1 AND 2---------------------------------------------------------#

    # Todo : Running the API request for price using Classes and Exception handling
stock =StockApi(STOCK, PRICE_API_KEY, PRICE_url)

    # Price data output would be the percentage change or the exit loop.
price_data = stock.price_request()
if price_data is None:
    # Printed the response through the api itself
    exit()
else:
    print(price_data)

# #--------------------------------------------------Step 4--------------------------------------------------------------#

# Todo: Clarifying condition to send the email
if price_data<-1 or price_data>1:
    # Todo: News email request
    news = NewsApi(STOCK, NEWS_API_KEY, NEWS_URL)
    news_data = news.news_request()
    # Need to exit the program if there are no news to present
    if news_data is None:
        exit()
    else:
        #--------------------------------------------------Step 5------------------------------------------------------#
        # Todo:  If there is news present--- Then need the email needs to be sent to the individual.
        CompanyData = CompanyWebsiteSection(stock=STOCK, price_change=price_data, articles = news_data)
        # This will store the html code into the company data. Now it needs to be placed into the correct section.


from datetime import timedelta
import requests
import datetime as dt
import json

class NewsApi:
    def __init__(self, stock, api_key, url):
        self.stock_name= stock
        self.api_key = api_key
        self.news_url = url

    def news_request(self):
        # Todo: Creating the parameters withe the required arguments for data
        news_parameters={
                    "q":self.stock_name,
                    "apiKey":self.api_key,
                    "to": dt.datetime.now().strftime("%Y-%m-%d"),
                    "from" : (dt.datetime.now()-timedelta(days=1)).strftime("%Y-%m-%d"),
                    "language" :"en",
                    "sort": "publishedAt",          # By the newest article
                    "pageSize": "2"
                        }

        # Todo: Sending the request FOR the data
        try:
            news_request = requests.get(url=self.news_url, params= news_parameters)
            data = news_request.json()
            if data["totalResults"]!=0:
                return data
            elif data["totalResults"]==0:
                print("No results Found")
                return None
            else:
                "There is an issue with the API request"
                return None
        except Exception as e:
            print( f"There was a News error. Code:{e}")
            return exit()

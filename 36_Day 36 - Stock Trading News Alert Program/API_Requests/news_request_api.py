from datetime import timedelta, datetime

import requests
import datetime as dt





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
                    "to": dt.datetime.now(),
                    "from" : dt.datetime.now()-timedelta(days=1),
                    "language" :"en",
                    "sort": "popularity",
                    "pageSize": "2"
                        }

        # Todo: Sending the request FOR the data
        try:
            news_request = requests.get(url=self.news_url, params= news_parameters)
            data = news_request.json()
            return data
        except Exception as e:
            print( f"There was a News error. Code:{e}")
            return None

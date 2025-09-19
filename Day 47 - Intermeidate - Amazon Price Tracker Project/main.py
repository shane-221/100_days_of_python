import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
load_dotenv()
import os

#--------------------------------------------------Constants-----------------------------------------------------------#
username="mathew.shane98@gmail.com"
#--------------------------------------------------Getting the Page data-----------------------------------------------#
website= requests.get(url= "https://appbrewery.github.io/instant_pot/")
data = website.text


soup= BeautifulSoup(data, "html.parser")
price_block = soup.find( class_= "aok-offscreen")
price = price_block.get_text()
price = price.replace("$", "")
price = float(price)

#
# password = os.getenv("password")
# print(username)
# print(password)

#----------------------------------Send email when value is below a number---------------------------------------------#
if price<int(100):
    connection =smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user =username,
                     password = os.getenv("password")
                     )
    connection.sendmail(from_addr=username,
                        to_addrs=username,
                        msg= "Ting is cheap"
                        )

    connection.close()




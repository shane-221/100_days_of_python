import requests
from bs4 import BeautifulSoup

#--------------------------------------------------Getting the Page data-----------------------------------------------#
website= requests.get(url= "https://appbrewery.github.io/instant_pot/")
data = website.text


soup= BeautifulSoup(data, "html.parser")
price_block = soup.find( class_= "aok-offscreen")
print(price_block.get_text())




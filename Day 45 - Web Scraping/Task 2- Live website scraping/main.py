import requests
from bs4 import BeautifulSoup


response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_website = response.text

soup = BeautifulSoup(yc_website, "html.parser")


#Todo: Finding all the headings
headings= soup.find(name ="a",class_ ="storylink")
print(headings.getText())
import requests
from bs4 import BeautifulSoup


response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_website = response.text

soup = BeautifulSoup(yc_website, "html.parser")


#Todo: Finding one of the headings, link and the upvotes
headings= soup.find(name ="a",class_ ="storylink")

upvote_function =soup.find(name="span", class_="score")
upvotes = upvote_function.getText()


article_upvotes = upvotes
article_text = headings.getText()
article_link =headings.get("href")

#Todo: Finding all of the headings, link and the upvotes
    # Same thing but just the find all function
headings= soup.find_all(name ="a",class_ ="storylink")

for article_tag in headings:
    
upvote_function =soup.find_all(name="span", class_="score")
upvotes = upvote_function.getText()


article_upvotes = upvotes
article_text = headings.getText()
article_link =headings.get("href")
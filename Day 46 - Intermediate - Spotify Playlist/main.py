import requests
import bs4
from bs4 import BeautifulSoup

year= input("Which year do you want to travel to? Type the date in this format - YYYY-MM-DD : ")
#---------------------------------------- Variables-------------------------------------------------------------------#
USER_AGENT ="Windows NT 10.0; Win64; x64"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

#-------------------------------------Using API to scrape the website--------------------------------------------------#
# Todo: get the website data
data = requests.get(url=  f"https://www.billboard.com/charts/hot-100/{year}", headers= header )
website = data.text

# Todo: Scraping the Website
soup = BeautifulSoup(website, "html.parser")
        # Pull all the 100 items
song_block =  soup.find_all( name = "div",
                        class_ = "o-chart-results-list-row-container"
                        )
song_names =[]
for i in song_block:
    heading = i.find(name ="h3")
    song_names.append(heading.get_text(strip= True))

songs_list = [ names.strip for names in song_names]




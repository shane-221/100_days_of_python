import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

year= input("Which year do you want to travel to? Type the date in this format - YYYY-MM-DD : ")
#---------------------------------------- Variables-------------------------------------------------------------------#
USER_AGENT ="Windows NT 10.0; Win64; x64"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

#-------------------------------------Get the songs list  by web scraping ---------------------------------------------#
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

#-----------------------------Spotipy: connect to spotify and get username --------------------------------------------#
# Since the code isw being run on behalf of a user. Need to specifically use a module that allows you to interact
##w with someone's account
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
                    client_id="42bb3e057650403a977df30a3da39f6a",
                    redirect_uri="https://example.com/callback",
                    client_secret="ee906458948f49c18301cbe00180da33",
                    scope= "playlist-modify-private"
                                    ))
user_id = sp.current_user()["display_name"]



#-------------------------------------Search Spotify for the Songs-----------------------------------------------------#
uri_list = []

for song in song_names:
    search = sp.search(q=f"{song}:{year}", type="track")
    uri_list.append(search["tracks"]["href"])

uri_list.insert(0,uri_list)
pprint.pp(uri_list)


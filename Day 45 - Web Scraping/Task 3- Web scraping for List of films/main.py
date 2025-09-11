import requests
from bs4 import BeautifulSoup



#Todo: ------------------------------------Getting the list of movies in TXT Format------------------------------------#
connection = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website = connection.text
print(website)


#Todo: ----------------------------------------Using beaultiful soup to get the data required--------------------------#

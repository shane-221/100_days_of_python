import requests
from bs4 import BeautifulSoup



#Todo: ------------------------------------Getting the list of movies in TXT Format------------------------------------#
connection = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website = connection.text


#Todo: ----------------------------------------Using beautiful soup to get the data required--------------------------#
movie_titles=[]
soup = BeautifulSoup(website, "html.parser")
heading =soup.find_all(name="h3" , class_="title")


for tag in heading:
    movie_name = tag.getText().split()
    movie_name = movie_name[1:]
    result =""
    for i in movie_name:
        result += i + " "
    movie_titles.append(result.strip(''))

movie_titles = [i.strip() for i in movie_titles]


with open("./Movie_List.txt", mode= "a") as file:
    n=0
    for i in movie_titles:
        n= n+1
        file.write(f"{n} :{i}\n")

# Todo: Importing beautiful soup verison 4
from bs4 import BeautifulSoup



# Todo:  Opening and collecting the data from the html file;
with open("./website.html") as file:
     contents = file.read()


# Todo: Using the beautuful soup module
                # notes class( MARKUP(I.E. the code for the html), parser( what language?))
soup = BeautifulSoup(contents,"html.parser" )
                        # In some cases you may need to use lmxl parser. Parser is just a way to read the website
                        # The soup acts as an object hat can tap into any part of the html code. Therefore allowing you
                        ## to tap into the html object using python code.

#---------------------------------------Functionalities----------------------------------------------------------------#

# Entire tag
print(soup.title)

# Tag function
print(soup.title.name)

# Tag string
print(soup.title.string)

# Can use prettify to place the indentations
print(soup.prettify())

# Can also get the first anchor tag/ li/p:
print(soup.li)
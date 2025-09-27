from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Todo:---------------------------------------------- Prep--------------------------------------------------------------#

    #Tells the webpage to stay open

chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option(name ="detach", value = True)

    #Specifying a custom location to store the data etc. Combines the current file with the one stated into a full
    #path
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
            #Specifies the correct file to be used.
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")


#Todo---------------------------------------------Running the website-------------------------------------------------#

driver = webdriver.Chrome( options= chrome_options)
driver.get("https://appbrewery.github.io/gym/")

# Todo--------------------------------------- Logging into the website-------------------------------------------------#
login_button =  driver.find_element(By.CLASS_NAME, value= "Navigation_rightSection__L2XbA")
login_button.click()

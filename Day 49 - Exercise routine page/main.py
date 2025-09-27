from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
load_dotenv()

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

            # Reaching the login page
login_button =  driver.find_element(By.CLASS_NAME, value= "Navigation_rightSection__L2XbA")
login_button.click()

            # Logging into the page
email= driver.find_element(By.CSS_SELECTOR, value = "input[id='email-input']")
email_id =os.getenv("USER_EMAIL")
email.send_keys(email_id)

password= driver.find_element(By.CSS_SELECTOR, value = "input[id='password-input']")
password_id =os.getenv("USER_PASSWORD")
password.send_keys(password_id)

login= driver.find_element(By.ID, value="submit-button")
login.click()

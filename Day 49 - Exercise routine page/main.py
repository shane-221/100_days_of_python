from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
load_dotenv()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


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
wait = WebDriverWait(driver, 2)
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

            # Wait for schedule page to load
wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))




# Todo---------------------------------------Booking classes-----------------------------------------------------------#



        # Todo:-------------- Getting all the important data prepared ------------------#
            # Choosing The day
date = driver.find_element(By.ID, value= "day-group-mon,-oct-6")
activities = date.find_elements(By.CLASS_NAME, value="ClassCard_card__KpCx5")


            # Adding the events of the daya into a dict
for i in activities:
                # Check to see if any classes are not fully booked and printing the message
    have_booked = str(i.get_attribute("data-user-booked")).strip().lower()
    fully_booked = str(i.get_attribute("data-class-status")).strip().lower()
    waitlisted = str(i.get_attribute("data-user-waitlisted")).strip().lower()

    event_data = i.get_attribute("id").split("-")                         # Getting the event and time data to present
    event = str(event_data[2]).strip().lower()
    time =str(event_data[-1]).strip().lower()

            # Todo:---------------------Click Functions --------------------------------------#
    try:
        all_clicks = i.find_element(By.CLASS_NAME, value="ClassCard_cardActions__tVZBm")
        button = all_clicks.find_element(By.CSS_SELECTOR, value="button")
        driver.execute_script("arguments[0].scrollIntoView(true);", button)
    except Exception as e:
        print (f" Could not find the Button for {event} at {time}: Error {e}")


            #Todo:----------------------Checking througgh the logic to click ther buttons--------------#
    if have_booked=="true":                                               # Check 1: have they booked it
        print(f"✓ Have booked : {event} on Mon, Oct 6 at {time}")

    else:
         if fully_booked=="full":                                         # Check 2: Can they book it ?
            print(f"✓ Event full : {event} on Mon, Oct 6 at {time}")
            response1 = input("Would you like to be waitlisted for this event? Yes or No?").lower().strip()
            if response1=="yes":
                button.click()
            else:
                pass
                                                                   # Check 3: Are they on the waitlist
         elif fully_booked == "available":
                print(f"✓ Event Available : {event} on Mon, Oct 6 at {time}")
                response2 = input("Would you like to book this event? Yes or No?").lower().strip()
                if response2=="yes":
                    button.click()
                else:
                    pass


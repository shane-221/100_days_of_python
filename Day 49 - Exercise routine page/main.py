from selenium import webdriver

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

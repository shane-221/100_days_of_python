from selenium import webdriver
from selenium.webdriver.common.by import By

# Setting the page so it stays open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("Detach", True)


# Getting the webdriver
driver= webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/instant_pot/")

# Finding stuff by classes
price_dollar= driver.find_element(By.CLASS_NAME, "a-price-whole").text
price_pennies= driver.find_element(By.CLASS_NAME, "a-price-fraction").text

print(f"{price_dollar}.{price_pennies}")


# Finding stuff by the name
search_bar = driver.find_element(By.NAME,"q")
print(search_bar.get_attribute("placeholder"))

#Finding stuff by ID
button = driver.find_element(By.ID, value = "submit")
print( button.size)

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By


# Getting the page to stay open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Getting the driver to work
driver=webdriver.Chrome(options =chrome_options)
driver.get("https://www.python.org/")

header = driver.find_element(By.CLASS_NAME, value="event-widget")
print( header.)

#driver.quit()
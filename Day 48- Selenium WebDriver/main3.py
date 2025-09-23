from selenium import webdriver
from selenium.webdriver.common.by import By

# Getting the driver to work
driver=webdriver.Chrome()
driver.get("https://www.python.org/")

header = driver.find_element(By.CLASS_NAME, value="shrubbery")
print(header)
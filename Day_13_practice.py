from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.qa-practice.com/")
assert driver.title == "Home Page | QA Practice"
print
input("Press Enter to close the browser.")
driver.quit()
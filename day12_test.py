from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/")
driver.find_element(By.CSS_SELECTOR, "input[class='DocSearch-Input']")
input("Press Enter to close the browser.")
driver.quit()
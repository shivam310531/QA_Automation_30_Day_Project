from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/")
driver.find_element(By.CSS_SELECTOR, "a[href='/downloads']").click()
input("Press Enter to close the browser.")
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/")
driver.find_element(By.CSS_SELECTOR, "a[href='/documentation']").click()
driver.find_element(By.ID,'m-documentationlegacy').click()
input("Press Enter to close the browser.")
driver.quit()
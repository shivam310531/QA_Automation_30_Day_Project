from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.qa-practice.com/")
driver.find_element(By.CSS_SELECTOR,"[href='/elements/checkbox/single_checkbox']").click()
print(driver.title)
input("Press Enter to close the browser.")
driver.quit()
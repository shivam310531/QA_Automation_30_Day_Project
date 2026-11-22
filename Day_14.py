from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 10)

button = wait.until(EC.element_to_be_clickable((By.ID, "submitBtn")))
button.click()
driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.qa-practice.com/")
driver.find_element(By.CSS_SELECTOR,"[href='/elements/checkbox/single_checkbox']").click()

input("Press Enter to close the browser.")
driver.quit()
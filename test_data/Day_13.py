from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CLASS_NAME, "fa.fa-2x.fa-sign-in").click()
input("Press Enter to close the browser.")
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.qa-practice.com/")
driver.find_element(By.CSS_SELECTOR,"[href='/elements/input/simple']").click()
driver.find_element(By.ID, "id_text_string").send_keys("Hello Shivam!")
input("Press Enter to close the browser.")
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.qa-practice.com/")
driver.find_element(By.CSS_SELECTOR,"[href='/elements/button/simple']").click()
driver.find_element(By.ID, "submit-id-submit").click()
input("Press Enter to close the browser.")
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.qa-practice.com/")
driver.find_element(By.CSS_SELECTOR,"[href='/elements/checkbox/single_checkbox']").click()
checkbox=driver.find_element(By.ID, "id_checkbox_0")
if not checkbox.is_selected():
    checkbox.click()
input("Press Enter to close the browser.")
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pytest
from selenium import webdriver
@pytest.fixture
def test_title():
    driver = webdriver.Chrome()
    driver.maximize_window()

    
    driver.get("https://www.qa-practice.com/")
    assert driver.title == "QA Practice"
   
    yield driver
    driver.quit()

import pytest 
from selenium import webdriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    
def test_title(driver):
   
    driver.get("https://www.qa-practice.com/")
    assert driver.title == "Home Page | QA Practice"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest 
from selenium import webdriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    
@pytest.mark.parametrize("username, password, expected[("tomsmith", "SuperSecretPassword!", "PASS"),("admin", "admin123", "FAIL"),("wrongadmin", "wrong123", "FAIL")]")

def test_title(driver, username, password, expected):
   
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "fa.fa-2x.fa-sign-in").click()

    if expected:
        assert "Login successful" in driver.page_source
    else:
        assert "Invalid" in driver.page_source

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest 
from selenium import webdriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
@pytest.mark.smoke
@pytest.mark.parametrize("username, password, expected",[("tomsmith", "SuperSecretPassword!", "True"),("admin", "admin123", "False"),("wrongadmin", "wrong123", "False")])

def test_title(driver, username, password, expected):
   
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "fa.fa-2x.fa-sign-in").click()

    if expected:
        assert "Welcome to the Secure Area. When you are done click logout below" in driver.page_source
    else:
        assert "Invalid" in driver.page_source


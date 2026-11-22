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

@pytest.mark.regression
def test_page_title(driver):

    driver.get("https://the-internet.herokuapp.com/login")
    assert "The Internet" in driver.title
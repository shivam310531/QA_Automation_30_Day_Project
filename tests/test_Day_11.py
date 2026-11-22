from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/")
actual_title = driver.title
expected_title = "Selenium"

if actual_title == expected_title:
    print("PASSED")
else:
    print("FAILED")

input("Press Enter to close the browser.")
driver.quit()
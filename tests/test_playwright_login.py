from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page =context.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_role("input", name = "username")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()
    
        


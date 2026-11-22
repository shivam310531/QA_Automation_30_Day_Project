from playwright.sync_api import sync_playwright
def test_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page =context.new_page()
        page.goto("https://the-internet.herokuapp.com/login")
        assert "The Internet" in page.title()
        browser.close()

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page =context.new_page()
        page.goto("https://the-internet.herokuapp.com/login")
        page.locator("#username").fill("tomsmith")
        page.locator("#password").fill("SuperSecretPassword!")
        page.locator("button[type='submit']").click()
        assert "secure" in page.url
        browser.close()
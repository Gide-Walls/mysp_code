from playwright.sync_api import sync_playwright
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    pages = browser.new_page()
    pages.goto("https://www.playwright.com/")

    pages.evaluate('window.open("https://www.baidu.com/")')

    pages.wait_for_timeout(20000)
    pages.click()
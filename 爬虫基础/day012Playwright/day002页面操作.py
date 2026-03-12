import time

from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False, channel='chrome')
    page = browser.new_page()
    # 等待机制
    page.set_default_timeout(60000)
    page.goto('https://www.baidu.com/')

    html = page.content()
    print("源码:", html)
    title = page.title()
    url = page.url
    print("url地址", url)
    time.sleep(15)

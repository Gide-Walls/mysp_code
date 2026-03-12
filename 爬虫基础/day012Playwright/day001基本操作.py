import time

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # 创建浏览器对象 默认打开是无头的 要在括号里面加东西就是有头的了
    browser = playwright.chromium.launch(headless=False)

    page = browser.new_page()
    page.goto('https://www.baidu.com')
    time.sleep(20)
    # 关闭浏览器
    browser.close()
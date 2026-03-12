import time

from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)

    page = browser.new_page()

    # page.set_extra_http_headers({"Cache-Contro1": "no-cache"})
    page.goto('https://www.baidu.com/?rsv_spt=1')

    # xpath定位 fill 一次性全部输入 type 是一个一个输入可以加时间
    # page.locator('//*[@id="kw"]').fill("你好") # 一次性输入
    # page.locator('//*[@id="kw"]').type("你好呀我是python", delay=1000)  # 延迟打字 模拟键盘一个一个输入


    #css选择器
    page.locator('#kw').fill('我爱python')
    page.locator('#su').click()
    input()

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.baidu.com/index.php?tn=75144485_4_dg&ch=1")
    # 找到输入框并且点击
    page.locator("#kw").click()
    page.keyboard.type(text='什么是python', delay=200)

    # 组合按键
    page.wait_for_timeout(2000)
    page.keyboard.press('Control+a')

    # 删除
    page.wait_for_timeout(2000)
    page.keyboard.press('Delete')
    page.keyboard.type('我是大好人',delay=2000)
    page.keyboard.press('Enter')
    page.wait_for_timeout(2000)

    input()

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    # 访问主页
    page.goto('https://im.qq.com/download')
    page.wait_for_timeout(1000)
    # 点击登录
    page.locator('#loginInfo').click()
    page.wait_for_timeout(5000)
    # 切换标签
    frame = page.frame_locator("iframe")
    # 点击标签
    page.wait_for_timeout(1000)
    frame.locator("#switcher_plogin").click()

    # 切换到打开的页面
    input()

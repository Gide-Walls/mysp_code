from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(r'D:\图灵课程学习\爬虫基础\day012Playwright\练习鼠标操作.html')

    page.drag_and_drop("#red-box","#green-box")
    page.wait_for_timeout(100000)

    input("输入任意字符退出")
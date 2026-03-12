from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://m.maoyan.com/asgard/board/4')

    # 使用 XPath 定位元素
    div_emts = page.locator('//div[@class="board-card clearfix"]')
    # 滚动到最后一个元素
    div_emts.last.scroll_into_view_if_needed()

    page.wait_for_timeout(10000)
    browser.close()
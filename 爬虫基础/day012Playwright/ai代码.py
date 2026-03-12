from playwright.sync_api import sync_playwright
import random
import time

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,  # 别用无头，更容易被识别
        args=[
            "--disable-blink-features=AutomationControlled",  # 关键：干掉webdriver
            "--start-maximized",
            "--no-sandbox",
            "--disable-dev-shm-usage",
        ],
        ignore_default_args=["--enable-automation"],
    )
    # 新建隐身上下文，每次都干净
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        viewport={"width": 1920, "height": 1080},
        locale="zh-CN",
        timezone_id="Asia/Shanghai",
    )
    # 注入JS彻底隐藏webdriver
    context.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
        window.navigator.chrome = {runtime: {}, loadTimes: () => {}};
        Object.defineProperty(navigator, 'plugins', {get: () => [1,2,3,4,5]});
        Object.defineProperty(navigator, 'languages', {get: () => ['zh-CN', 'zh']});
    """)
    page = context.new_page()
    page.goto("https://www.baidu.com")
    input()
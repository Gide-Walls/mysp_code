import time

from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://baidu.com')
# 打开新的页面
browser.execute_script("window.open()")
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.taobao.com')
browser.switch_to.window(browser.window_handles[0])
browser.get("https://www.vip.com")
time.sleep(2)
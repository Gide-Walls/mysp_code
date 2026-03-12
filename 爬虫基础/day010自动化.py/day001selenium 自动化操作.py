from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 创建浏览器对象
browser = webdriver.Chrome()
# webdriver.Firefox()
# webdriver.Edge()
# 基本操作
try:
    browser.get("https://www.baidu.com")

    # 定位输入框(id定位)加s是定位多个不加定位少的几个
    browser.find_element(By.ID, "chat-textarea").send_keys("你好呀")
    # 获取渲染之后的代码内容
    # print(browser.page_source)

    # 获取cookie
    print(browser.get_cookies())

    # 截屏看验证码
    browser.get_screenshot_as_file("baidu.png")

finally:
    time.sleep(2)
    browser.quit()

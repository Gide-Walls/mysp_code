from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# print("我是豆瓣")
browser = webdriver.Chrome()
browser.get('https://www.douban.com/')
time.sleep(2)
# 定位子页面
iframe = browser.find_element(By.XPATH, '//div[class="login"]/iframe')
# 切换子页面
time.sleep(2)
browser.switch_to.frame(iframe)

# 切换到输入框
browser.find_element(By.NAME, 'phone').send_keys('19536129937')
time.sleep(3)

browser.quit()

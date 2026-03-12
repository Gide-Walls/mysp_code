from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 查找节点
browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
# 定位标签
# s = browser.find_element_by_id(By.ID, "chat-textarea")
# s.send_keys('你好')
# s.send_keys(Keys.RETURN)
#
# time.sleep(4)

# 节点提取

# aa = browser.find_element(By.XPATH, '//*[@id="chat-textarea"]')
# aa.send_keys("你好")
# time.sleep(2)
# css也行

# 多节点查找


# 多节点查找
li_list = browser.find_elements(By.CSS_SELECTOR, '#hotsearch-content-wrapper li')
# print(li_list)
for li in li_list:
    # text 获取标签文本内容
    # get_attribute 获取属性内容
    print(li.find_element(By.XPATH, './/span[@class="title-content-title"]').text)
    print(li.find_element(By.XPATH, './a').get_attribute('href'))
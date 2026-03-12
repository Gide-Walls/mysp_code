import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# 访问百度首页
driver.get("https://www.baidu.com")

# 找百度首页真实存在的搜索框（id=kw）
wait = WebDriverWait(driver, 10)
search_box = wait.until(
    EC.presence_of_element_located((By.ID, "kw"))  # 改这里！用真实存在的id
)
driver.maximize_window()
# 输入内容
search_box.send_keys("测试")
print("找到百度搜索框，输入成功！")
print("页面标题：", driver.title)
time.sleep(10)
driver.quit()
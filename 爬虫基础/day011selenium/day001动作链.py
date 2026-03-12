import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# 动作链
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
# 获取页面 看看有没有定位到的
# print(driver.page_source)
time.sleep(2)
frame = driver.find_element(By.ID, 'iframeResult')
driver.switch_to.frame(frame)

sour = driver.find_element(By.ID, 'droppable')
targ = driver.find_element(By.ID, 'draggable')
actions = ActionChains(driver)
actions.drag_and_drop(sour, targ).perform()

time.sleep(2)
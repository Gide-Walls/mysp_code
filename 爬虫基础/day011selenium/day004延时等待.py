from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get('https://baidu.com')
# 延时等待
wait = WebDriverWait(browser, 2)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'chat-input-container')))

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
try:
    browser.get('https://baidu.com')

except TimeoutException:
    print('time out')
try:
    browser.find_element(By.ID,'asdasdasd')
    # 精准捕获
except NoSuchElementException:
    print('没有呀')
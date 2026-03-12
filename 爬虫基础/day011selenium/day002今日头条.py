from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get('https://www.toutiao.com/')



for i in range(10):
    time.sleep(1)
    driver.execute_script("window.scrollBy(0,{})".format(i*700))

time.sleep(5)
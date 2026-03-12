from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from lxml import etree
browser = webdriver.Chrome()
url = "https://pic.netbian.com/new/index_1527.html"
browser.get(url)
# time.sleep(5)
# src = browser.find_elements(By.XPATH, '//div[@class="slist"]/ul[@class="clearfix"]/li')
# for a in src:
#     # time.sleep(1)
#     print(a)
#     url = a.get_attribute('href')
#     title = a.find_element(By.XPATH,'//b').text
#     print(title)
#     print(url)

# 上面写法取值有问题的话使用
html = etree.HTML(browser.page_source)

src = html.xpath('//div[@class="slist"]/ul[@class="clearfix"]/li')
for a in src:
    print(a.xpath('.//a/@href')[0])
    print(a.xpath('.//b/text()')[0])

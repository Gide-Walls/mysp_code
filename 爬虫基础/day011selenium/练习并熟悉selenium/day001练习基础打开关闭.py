from selenium import webdriver

driver = webdriver.Chrome()
# 去百度看看
driver.get("https://www.baidu.com")

# 看看网页标题是什么

print(driver.title)

driver.quit()
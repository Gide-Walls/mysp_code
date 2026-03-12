from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

# 👇 加上这一句，就能用你“手动改好设置”的Chrome！
options.add_argument("--user-data-dir=UserData")

# 防百度检测
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)
driver.get("https://www.baidu.com")
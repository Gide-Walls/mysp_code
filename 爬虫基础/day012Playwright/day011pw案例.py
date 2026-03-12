from playwright.sync_api import sync_playwright
import time
import pymongo
class kaoyan:
    def __init__(self):
        self.mongo = pymongo.MongoClient('localhost', 27017)["kaoyan"]["data"]
        self.url = f"https://www.handebook.com/web/#/13363451598/document"
    def jiexi(self, page):
        time.sleep(5)
        element = page.locator('xpath=//div[@class="school-list"]')
        print(element)
        data_list = element.locator('xpath=.//div[@class="content-document"]').all()
        data_list_serve = []
        for data in data_list:
            dict_data = {"名字": data.locator('xpath=./span[1]').text_content(),
                         "价格": data.locator('xpath=./span[2]').text_content()}
            data_list_serve.append(dict_data)
        try:
            self.mongo.insert_many(data_list_serve)
        except Exception as e:
            print(e)
            print("插入失败")
        print(data_list_serve)

    def request_url(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(self.url)
            for i in range(10):
                self.jiexi(page)

                time.sleep(2)
                page_texy = page.locator('xpath=//button[@class="btn-next"]')
                if page_texy.count() == 0:
                    print("已经是最后一页了")
                    break
                page_texy.click()
                page.wait_for_timeout(3000)
if __name__ == '__main__':
    aaa = kaoyan()
    aaa.request_url()

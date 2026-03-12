from lxml import etree
import requests
import time

class doubanSpider(object):  # 修正类名拼写
    '''定义大类'''
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0"
        }
    
    def requsets_get(self):
        '''发送请求'''
        response=requests.get("https://book.douban.com/chart?subcat=all&p=1&updated_at=2026-02-02",headers=self.headers)
        return response.text
    def response_xpath(self):
        '''筛选数据'''
        tree=etree.HTML(self.requsets_get())
        books=[]
        book_name_list=tree.xpath('//li[contains(@class, "media") and contains(@class, "clearfix")]')
        for idx,li in enumerate(book_name_list,1):
            #提取书名
            book_name_xpath=li.xpath('.//a[@class="fleft"]/text()')[0]
            #提取信息
            book_lnfo=' '.join(li.xpath('//p[@class="subject-abstract color-gray"]/text()')[0].split())
            comment_count=li.xpath('.//span[@class="fleft ml8 color-gray"]/text()')[0].strip('()').strip()
            
            
            book_list={
                "序号":f"{idx}",
                "书名":book_name_xpath,
                "信息":book_lnfo,
                "评价数量":comment_count
            }
            books.append(book_list)
        print(books)
        for i in books:
            print(i)
if __name__ == '__main__':
    aaa=doubanSpider()
    aaa.response_xpath()

        
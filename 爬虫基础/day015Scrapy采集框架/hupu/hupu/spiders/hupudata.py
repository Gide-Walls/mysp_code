import json

import scrapy
from hupu.items import HupuItem
import time
from hupu.items import UncommentItem


class HupudataSpider(scrapy.Spider):
    name = "hupudata"
    # allowed_domains = ["www.hupu.com"]
    allowed_domains = ["hupu.com"]

    start_urls = ["https://www.hupu.com/"]

    def parse(self, response):
        hupu_url = "https://www.hupu.com/home/v1/news?pageNo={page}&pageSize=50"
        for page in range(1, 15):
            page_url = hupu_url.format(page=page)
            yield scrapy.Request(url=page_url, callback=self.parse_page, meta={'page_url': page})

    def parse_page(self, response):
        print(response.text)
        page_num = response.meta['page_url']
        print(f"正在解析{page_num}")
        print(time.time())
        try:
            data = json.loads(response.text)
            if data.get("msg"):
                data_list = data["data"]
                for items in data_list:
                    item = HupuItem()

                    item["title"] = items["title"]
                    item["content"] = items["content"]
                    item["topicName"] = items["topicName"]
                    item["pageNum"] = page_num
                    item["tid"] = items["tid"]
                    detail_url = "https://bbs.hupu.com/" + str(items["tid"]) + '.html'
                    item["detailUrl"] = detail_url
                    print(detail_url)
                    yield item
                    yield scrapy.Request(detail_url, callback=self.parse_detail, meta={'tid': items["tid"]})


        except Exception as e:
            print(f"响应解析错误{e}")

    def parse_detail(self, response):
        # print(response.text)
        from hupu.items import UncommentItem
        tid = response.meta['tid']
        title = response.xpath('//div[@class="thread-content-detail"]/p[1]/text()').extract()
        item = UncommentItem()
        text_list = []
        for text in title:
            text_list.append(text)
        item["title"] = text_list
        item["tid"] = tid

        yield item


if __name__ == '__main__':
    from scrapy import cmdline

    cmdline.execute("scrapy crawl hupudata".split())

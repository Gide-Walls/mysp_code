import scrapy
from lxml import etree
from scrapy.http import HtmlResponse
from douban_project.items import DoubanProjectItem
print("爬虫已经加载")


class DoubanSpiderSpider(scrapy.Spider):
    name = "douban_spider"
    allowed_domains = ["movie.douban.com"]  # 允许的域名
    start_urls = ["https://movie.douban.com/top250"]

    # def start_requests(self):
    #     for url in range(10):
    #         url = f"https://movie.douban.com/top250?start={url*25}"
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: HtmlResponse, **kwargs):
        print("爬虫已经执行")
        # print(response.text)
        # print(response.)
        # list_data = []
        li_list = list(response.xpath('//ol[@class="grid_view"]/li'))

        for li in li_list:
            item = {"名字": li.xpath('.//a//span[1]/text()').extract_first()}
            # yield 返回对象 要么是字典 baseitem 要么是requset对象 None
            yield item
        if response.xpath('//span[@class="next"]//a/@href').extract_first() is not None:
            print("不明白")
            next_url = response.urljoin(response.xpath('//span[@class="next"]//a/@href').extract_first())
            # 创建请求对象  callback 回调函数 指定那个函数进行处理
            yield scrapy.Request(next_url, callback=self.parse_detaile, meta={'item': item})

    def parse_detaile(self, response: HtmlResponse, **kwargs):
        print(response.url)
        print(response.meta['item'])


if __name__ == '__main__':
    from scrapy import cmdline

    cmdline.execute("scrapy crawl douban_spider".split())

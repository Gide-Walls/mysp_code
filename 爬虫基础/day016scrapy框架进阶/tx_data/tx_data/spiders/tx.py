import scrapy


class TxSpider(scrapy.Spider):
    name = "tx"
    allowed_domains = ["careers.tencent.com"]
    start_urls = ["https://careers.tencent.com"]

    def parse(self, response):
        pass

import scrapy


class HupudataSpider(scrapy.Spider):
    name = "hupudata"
    allowed_domains = ["www.hupu.com"]
    start_urls = ["https://www.hupu.com/"]

    def parse(self, response):
        pass

import scrapy
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


class TxSpider(scrapy.Spider):
    name = "tx"
    allowed_domains = ["careers.tencent.com"]

    # 关闭 robots.txt 限制（腾讯招聘的 robots.txt 会拦截爬虫）
    def start_requests(self):

        url = 'https://careers.tencent.com/search.html?query={}'
        for i in range(1, 5):
            # page = context.new_page()
            url1 = url.format(i)
            yield scrapy.Request(url=url1, callback=self.parse,
                                 )

    def parse(self, response):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False, args=['--no-sandbox'])
            context = browser.new_context(
                locale="zh-CN",
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            # context = browser.new_context()
            page = context.new_page()
            page.goto(response.url)
            page.wait_for_selector(".job-recruit-title",timeout=1000)
            html = page.content()
            print(html)



if __name__ == '__main__':
    from scrapy import cmdline

    cmdline.execute('scrapy crawl tx'.split())

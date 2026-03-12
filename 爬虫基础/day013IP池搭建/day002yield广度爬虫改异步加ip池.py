import aiohttp
import time
from lxml import etree
from fake_useragent import UserAgent
import asyncio
from aiohttp import ClientSession


class Spider:
    def __init__(self):
        self.url = 'https://qq.ip138.com/train/'
        self.ua = UserAgent()
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Referer': 'https://www.ip138.com/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': self.ua.random,
            'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        self.cookies = {
            'Hm_lvt_ecdd6f3afaa488ece3938bcdbb89e8da': '1772708440',
            'HMACCOUNT': 'D83BF4CCC382C9ED',
            'Hm_lvt_e3699341295209ce778322a870fa2bab': '1772708470',
            'Hm_lpvt_ecdd6f3afaa488ece3938bcdbb89e8da': '1772708509',
            'Hm_lpvt_e3699341295209ce778322a870fa2bab': '1772717534',
        }
        self.session = None
        self.semaphore = asyncio.Semaphore(2)  # 控制并发数

    async def init_session(self):
        """初始化异步session"""
        self.session = aiohttp.ClientSession(
            headers=self.headers,
            cookies=self.cookies
        )

    async def fetch(self, url, layer="未知层"):
        """通用请求函数（替代原来的三层请求函数）"""
        for i in range(3):
            try:
                async with self.semaphore:
                    res = await self.session.get(url)
                    if res.status == 200:
                        res.encoding = 'utf-8'
                        return await res.text()
                    else:
                        print(f"【{layer}】请求{url}失败，状态码：{res.status}")
            except Exception as e:
                print(f"【{layer}】{url} 请求异常：{e}，重试第{i + 1}次")
            await asyncio.sleep(1)
        return None

    def parse_home(self, html_text):
        """解析主页，yield 出所有省份URL（生成器）"""
        html = etree.HTML(html_text)
        dl_list = html.xpath('//dl')
        for dl in dl_list:
            region = dl.xpath('./dt/text()')[0]
            province_dd = dl.xpath('./dd')
            for dd in province_dd:
                pro_name = dd.xpath('./a/text()')[0]
                pro_url = "https://qq.ip138.com" + dd.xpath('./a/@href')[0]
                # 用yield吐出，不存列表
                yield {
                    "地区": region,
                    "省份": pro_name,
                    "省份URL": pro_url
                }

    def parse_province(self, html_text):
        """解析省份页，yield 出所有火车站URL（生成器）"""
        html = etree.HTML(html_text)
        div_box = html.xpath('//div[@class="box"]')
        for div in div_box:
            abc = div.xpath('.//span/text()')[0]
            href_list = div.xpath('.//li/a')
            for href in href_list:
                station_url = "https://qq.ip138.com/" + href.xpath('./@href')[0]
                station_name = href.xpath('./text()')[0]
                # 用yield吐出，不存列表
                yield {
                    "拼音前缀": abc,
                    "车站名": station_name,
                    "车站URL": station_url
                }

    def parse_station(self, html_text):
        """解析车站页，yield 出车次数据（生成器）"""
        html = etree.HTML(html_text)
        tr_list = html.xpath('//tbody/tr')
        for tr in tr_list:
            car_num = tr.xpath('./td[2]/text()')
            start_station = tr.xpath('./td[3]/a/text()')
            start_time = tr.xpath('./td[4]/text()')
            # 用yield吐出每条车次数据
            yield {
                "车次": car_num[0] if car_num else "",
                "始发地": start_station[0] if start_station else "",
                "发车时间": start_time[0] if start_time else ""
            }

    async def crawl(self):
        """核心爬取逻辑（串联所有生成器）"""
        # 1. 爬主页
        home_html = await self.fetch(self.url, "主页")
        if not home_html:
            print("主页爬取失败，终止任务")
            return

        # 2. 遍历主页生成器（省份URL）
        for pro_data in self.parse_home(home_html):
            print(f"\n开始爬取：{pro_data['地区']}-{pro_data['省份']}")
            # 3. 爬省份页
            pro_html = await self.fetch(pro_data["省份URL"], f"{pro_data['省份']}")
            if not pro_html:
                print(f"{pro_data['省份']} 爬取失败，跳过")
                continue

            # 4. 遍历省份页生成器（火车站URL）
            for station_data in self.parse_province(pro_html):
                # 5. 爬车站页
                station_html = await self.fetch(station_data["车站URL"], f"{station_data['车站名']}")
                if not station_html:
                    print(f"{station_data['车站名']} 爬取失败，跳过")
                    continue

                # 6. 遍历车站页生成器（车次数据）
                for train_data in self.parse_station(station_html):
                    # 最终的车次数据，统一yield出来
                    yield {
                        "省份": pro_data["省份"],
                        "车站": station_data["车站名"],
                        **train_data  # 合并车次数据
                    }
            await asyncio.sleep(2)  # 省份间加个延迟，避免被封

    async def main(self):
        """主函数"""
        await self.init_session()
        # 遍历核心生成器，拿到所有车次数据
        async for train_info in self.crawl():
            # 这里可以统一处理数据（打印/存库/导出）
            print(f"【最终数据】{train_info}", flush=True)

        # 关闭session
        await self.session.close()


if __name__ == "__main__":
    start_time = time.time()
    spider = Spider()
    asyncio.run(spider.main())
    print(f"\n总耗时：{time.time() - start_time:.2f}秒")
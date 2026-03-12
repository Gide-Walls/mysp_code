import requests
import time
from lxml import etree
from fake_useragent import UserAgent
import asyncio


class Spider:
    def __init__(self):
        self.url = 'https://qq.ip138.com/train/'
        self.ua = UserAgent()
        self.random = self.ua.random
        # self.proxy = {"http": "101.37.27.102:80",
        #               "https": "01.37.27.102:80"}
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
            # 'Cookie': 'Hm_lvt_ecdd6f3afaa488ece3938bcdbb89e8da=1772708440; HMACCOUNT=D83BF4CCC382C9ED; Hm_lvt_e3699341295209ce778322a870fa2bab=1772708470; Hm_lpvt_ecdd6f3afaa488ece3938bcdbb89e8da=1772708509; Hm_lpvt_e3699341295209ce778322a870fa2bab=1772717534',
        }
        self.cookies = {
            'Hm_lvt_ecdd6f3afaa488ece3938bcdbb89e8da': '1772708440',
            'HMACCOUNT': 'D83BF4CCC382C9ED',
            'Hm_lvt_e3699341295209ce778322a870fa2bab': '1772708470',
            'Hm_lpvt_ecdd6f3afaa488ece3938bcdbb89e8da': '1772708509',
            'Hm_lpvt_e3699341295209ce778322a870fa2bab': '1772717534',
        }
        self.session = requests.Session()
        self.session.cookies.update(self.cookies)
        self.q = asyncio.Queue()

    # 主页请求
    def requests_get(self):
        """发送请求"""
        res = self.session.get(self.url, headers=self.headers)
        res.encoding = 'utf-8'
        return res.text

    # 第二层 链接发送请求
    def requests_province(self, url):
        # 省份链接请求
        res = self.session.get(url, headers=self.headers)
        res.encoding = 'utf-8'
        return res.text

    # 获取车次加xpath解析
    def train(self, url):
        time.sleep(2)
        res = self.session.get(url, headers=self.headers)
        res.encoding = 'utf-8'
        html = etree.HTML(res.text)
        tr = html.xpath('//tbody/tr')
        car_data = []
        for tr in tr:
            car = tr.xpath('./td[2]/text()')
            start = tr.xpath('./td[3]/a/text()')
            start_time = tr.xpath('./td[4]/text()')
            car_data.append({"车次": car,
                             "始发地": start,
                             "发车时间": start_time})
        print(car_data)

    # 第二层各个火车站解析出url 进行请求(用train)并打印出来
    def tow_analysis(self, data):
        html = etree.HTML(data)
        div_box = html.xpath('//div[@class="box"]')
        station_list = []
        for div in div_box:
            abc = div.xpath('.//span/text()')[0]  # 获取汉字拼音开头
            href_list = div.xpath('.//li/a')  # 获取链接列表
            station_dict_list = []
            for href in href_list:
                href_data = "https://qq.ip138.com/" + href.xpath('./@href')[0]
                station = href.xpath('./text()')[0]
                station_dict_list.append({
                    'href': href_data[0],
                    'station': station,
                })
                time.sleep(2)
                self.train(href_data)
            station_list.append({abc: station_dict_list})
        print(station_list)

    # 获取第二层的各个省份+ 链接 调用了tow_analysis函数 去解析出url
    def analysis(self, res):
        # 主页转成html
        html = etree.HTML(res)
        # 地区标签
        dl = html.xpath('//dl')
        dict_data = []
        for tr in dl:
            # 地区
            region_list = tr.xpath('./dt/text()')[0]
            # 省份list
            province_list = tr.xpath('./dd')
            dict_pro = []
            # 获取省份 加 链接
            for province in province_list:
                link = province.xpath('./a/@href')[0]
                pro = province.xpath('./a/text()')[0]
                link_url = "https://qq.ip138.com" + link
                dict_pro.append({'省份': pro, '链接': link_url})
                res = self.requests_province(link_url)
                self.tow_analysis(res)  # 解析各个省份的 里面的城市
                time.sleep(5)
            dict_data.append({region_list: dict_pro})
        return dict_data

    # 获取各个省份链接
    # def station_url(self, dict_data):
    #     for region in dict_data:
    #
    #         for key, value in region.items():
    #
    #             print(key)  # key是地区
    #             for province in value:
    #                 province_name = province["省份"]
    #                 province_url = province["链接"]
    #                 print(province_name, province_url)

    def main(self):
        res = self.requests_get()  # 获取主页的各个地区的url  省份的
        self.analysis(res)
        # self.station_url(data)
        # print(data)


spider = Spider()
spider.main()

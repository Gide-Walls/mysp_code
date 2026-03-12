import requests
import json
from lxml import etree
import time
import pymongo
class kuai():
    def __init__(self):
        self.s = requests.session()
        cookies = {
            'path': '/',
            '__tst_status': '2216981987#',
            'EO_Bot_Ssid': '2654470144',
            'channelid': 'wrtg_q2_q2',
            'sid': '1772516809068712',
            '_ss_s_uid': 'b16e6649bfc7b2f18afa12f62f85c146',
            '_gcl_au': '1.1.263140937.1772516813',
            '_ga': 'GA1.1.1723298457.1772516813',
            'path': '/',
            '_c_WBKFRo': 'C6SsN3GfWqtI75GInfyPYFYgV0YMV3Nnd7RSvOvi',
            '_nb_ioWEgULi': '',
            'sessionid': '87a0aa5ba9535b149a9799950905c49a',
            '_uetsid': 'ddbf4c2017a011f1b7085fd6f4a12d30|1bw0w9b|2|g43|0|2254',
            '_uetmsclkid': '_uet95f91d2b25d6161d3ee474820200a884',
            '_uetvid': '5753aeb016c411f19f47a1b24fcc62d4|18y171c|1772693520564|3|1|bat.bing.com/p/conversions/c/z',
            '_ga_DC1XM0P4JL': 'GS2.1.s1772693523$o5$g0$t1772693523$j60$l0$h0',
        }
        self.s.cookies.update(cookies)
        self.s.headers.update({
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://www.kuaidaili.com/free/dps/2',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36', })
        self.mongo = pymongo.MongoClient('localhost', 27017)["kuaidaili"]["ip"]


    def request_url(self, idx):
        try:
            url = f'https://www.kuaidaili.com/free/dps/{idx}'
            res = self.s.get(url)
            return res
        except Exception as e:
            print(e)

    def Analysis(self, res):
        html = etree.HTML(res.text)
        tr = html.xpath('//tbody[@class="kdl-table-tbody"]/tr')
        ip_list = []
        for trs in tr:
            ip = trs.xpath('./td[1]/text()')[0]
            port = trs.xpath('./td[2]/text()')[0]
            http_https = trs.xpath("./td[normalize-space()='HTTP' or normalize-space()='HTTP(S)']/text()")[0].strip()

            ip_list.append({'ip': ip, 'port': port, 'http_https': http_https})
        self.mongo.insert_many(ip_list)
        print(ip_list)

    def main(self):
        for idx in range(1, 15):
            time.sleep(2)

            res = self.request_url(idx)
            if res.status_code == 200:
                self.Analysis(res)


if __name__ == '__main__':
    keys = kuai()
    keys.main()

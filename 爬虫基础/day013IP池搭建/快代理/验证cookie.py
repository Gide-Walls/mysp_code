import requests
import json
from pymongo import MongoClient
import time

class ver:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client['kuaidaili']
        self.collection = self.db['ip']
        self.headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://www.kuaidaili.com/free/dps/1',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
            # 'cookie': 'path=/; __tst_status=2931901435#; EO_Bot_Ssid=2154233856; channelid=wrtg_q2_q2; sid=1772516809068712; _ss_s_uid=b16e6649bfc7b2f18afa12f62f85c146; _gcl_au=1.1.263140937.1772516813; _ga=GA1.1.1723298457.1772516813; path=/; _c_WBKFRo=C6SsN3GfWqtI75GInfyPYFYgV0YMV3Nnd7RSvOvi; _nb_ioWEgULi=; sessionid=87a0aa5ba9535b149a9799950905c49a; _uetsid=ddbf4c2017a011f1b7085fd6f4a12d30|1bw0w9b|2|g43|0|2254; _uetmsclkid=_uet95f91d2b25d6161d3ee474820200a884; _uetvid=5753aeb016c411f19f47a1b24fcc62d4|1f1i5mf|1772700841738|8|1|bat.bing.com/p/conversions/c/z; _ga_DC1XM0P4JL=GS2.1.s1772700367$o6$g1$t1772700844$j8$l0$h0',
        }

    def read(self):
        response = None
        datas = self.collection.find()
        for data in datas:
            time.sleep(1)
            ip = data['ip']
            http = data['port']
            proxy = {"http": f"{ip}:{http}",
                     "https": f"{ip}:{http}"}
            try:
                response = requests.get('https://baidu.com', proxies=proxy, headers=self.headers,timeout=1)
            except Exception as e:
                print(e)
            if response is not None:
                if response.status_code == 200:

                    print(f"{ip}和{http}没有问题")
            else:
                print("ip是坏的")
if __name__ == '__main__':
    ver = ver()
    ver.read()

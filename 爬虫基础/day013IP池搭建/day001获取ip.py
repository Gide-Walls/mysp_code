import requests
from lxml import etree
import json
class IP:
    def __init__(self):
        self.url = 'https://proxy5.net/cn/free-proxy/china'
        # cookies 过期的话更换一下就行
        self.headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://cn.bing.com/',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
            'sec-ch-ua-arch': '"x86"',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-full-version': '"145.0.7632.159"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Google Chrome";v="145.0.7632.159", "Chromium";v="145.0.7632.159"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"19.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
            'cookie': '_gcl_au=1.1.158616284.1772678306; _ga=GA1.1.1658097651.1772678306; _ym_uid=1772678308379759893; _ym_d=1772678308; _ym_isad=2; _ym_visorc=w; cf_clearance=uhWpO5TNHthv6GmxRYiM1DXfutDROuav909TQZ6q25E-1772678472-1.2.1.1-gJFX4lWIOk9IZBb.NFZ6fjMS3Uhbn9GkBt5mNik_cWcrezUcxpQlVihnuwqem.ovgpAOqBbWL9_hReX2HVmF.Hx1l_apKCxXAr1FLHrudSvtWUG9VgBPvQkJ_gy2UjAx0eAGjtNsCX8XMDu.TRIm_ZiGVslcWzOHoVV_OWxjv6NM4N8DKdfrvXI_UpPMZd2U.u9QAF8dzQPCyGtShigsVFOf6TJgn.Vu9XAluGfqHupFoVydQvNo7G42DwKPwHuT; WHMCSy551iLvnhYt7=fb5qfeut72rt0steqkih8sti3d; _ga_2ZGKN4M0P5=GS2.1.s1772678306$o1$g1$t1772678501$j40$l0$h0',
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    def get_ip(self):
        response = self.session.get(self.url)
        # print(response.text)
        return response.text
    def analysis(self, res):
        html = etree.HTML(res)
        print(html)
        tr_list = html.xpath('//tbody/tr')
        print(tr_list)
        ip_list = []
        for tr in tr_list:
            ip_dict = {}
            ip_dict["ip"] = tr.xpath('./td/strong/text()')

            ip_dict["port"] = tr.xpath('./td[2]/text()')

            ip_dict["http_or_https"] = tr.xpath('./td[3]/text()')
            ip_list.append(ip_dict)
        # print(ip_list)
        return ip_list

    def serve_data(self, result):
        with open(r"serve_ip/ip_data.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
    def main(self):
        res = self.get_ip()
        print(res)
        result = self.analysis(res)
        self.serve_data(result)
        print("写入完成")
if __name__ == '__main__':
    ip = IP()
    ip.main()

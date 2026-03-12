import pymongo
from selenium import webdriver
import time


class VIP:
    def __init__(self):
        # --- 1. 数据库初始化 ---
        # 连接本地 MongoDB 数据库
        self.mong = pymongo.MongoClient('localhost', 27017)
        # 指定数据库名为 'VIP'，集合（表）名为 'shop'
        self.db = self.mong['VIP']['shop']

        # --- 2. 浏览器配置 Options ---
        # 创建 Chrome 浏览器的配置对象
        options = webdriver.ChromeOptions()

        # 隐藏“Chrome 正受到自动测试软件的控制”提示
        options.add_experimental_option('useAutomationExtension', False)
        # 去掉“请停用开发者模式”扩展提示和控制台日志
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        # 设置不加载图片（加快爬取速度，可选）
        # prefs = {'profile.managed_default_content_settings.images': 2}
        # options.add_experimental_option('prefs', prefs)

        # --- 3. 启动浏览器 ---
        # 使用配置好的 options 启动浏览器
        # 统一使用 self.browser 作为浏览器对象
        self.browser = webdriver.Chrome(options=options)

        # 启动后最大化窗口
        self.browser.maximize_window()

        # --- 4. Cookie 数据 ---
        # 存储登录态的 Cookie，用于模拟登录
        # 注意：这里的 Cookie 可能已过期，需要实时抓取
        self.cookies = {
    'vip_first_visitor': '1',
    'vip_address': '%257B%2522pid%2522%253A%2522102101%2522%252C%2522cid%2522%253A%2522102101105%2522%252C%2522pname%2522%253A%2522%255Cu8fbd%255Cu5b81%255Cu7701%2522%252C%2522cname%2522%253A%2522%255Cu672c%255Cu6eaa%255Cu5e02%2522%257D',
    'vip_province': '102101',
    'vip_province_name': '%E8%BE%BD%E5%AE%81%E7%9C%81',
    'vip_city_name': '%E6%9C%AC%E6%BA%AA%E5%B8%82',
    'vip_city_code': '102101105',
    'vip_wh': 'VIP_BJ',
    'vip_ipver': '31',
    'mars_cid': '1772412209598_6dc1a9c929615bd26ec05eea99f1c3c8',
    'mars_sid': '9f56dbec17714fa9908603d0f73cb966',
    'mst_area_code': '104104',
    'mars_pid': '0',
    'visit_id': '6E2CF4D3EBD2869BC5E18EC77A5B062E',
    'VIP_QR_FIRST': '1',
    'vip_sec_fp_vvid': 'ZTk4YzdjZTQtOThjNS00MTQ5LWJmMTAtZWUzZDc4ODdkN2YzMTc3MjQxMjIwOTUyMMl/Y2M=',
    'pc_fdc_area_id': '102101105',
    'pc_fdc_source_ip': '1',
    'is_default_area': '1',
    'smidV2': '20260302084341ca67355c54f9f01968bb8a071eca421400ceea543cfe14940',
    'vip_access_times': '%7B%22list%22%3A1%7D',
    'VipRUID': '657722323',
    'VipRNAME': 'ph_*****************************10b',
    'VipDegree': 'D1',
    'user_class': 'b',
    'vip_sec_fp_vid': '657722323',
    'VipUINFO': 'luc%3Ab%7Csuc%3Ab%7Cbct%3Ac_new%7Chct%3Ac_new%7Cbdts%3A0%7Cbcts%3A0%7Ckfts%3A0%7Cc10%3A0%7Crcabt%3A0%7Cp2%3A0%7Cp3%3A1%7Cp4%3A0%7Cp5%3A0%7Cul%3A3105',
    '.thumbcache_f65dad1092aa9e66c73b4823b4493a2f': 'j3ORqS20IRBPU4Nb1sj30Y7JtnOZi472sogcIfJ3PKvWbAzr/K0frVOqlk9tXNkTwDnHHyeRLTeq+Q1rJmNJ8w%3D%3D',
    'vipshop_passport_src': 'https%3A%2F%2Fwww.vip.com%2F',
    'vpc_uinfo': 'fr1352%3A0%2Cfr674%3AD1%2Cfr766%3A0%2Cfr1870%3A0%2Cfr1622%3A0%2Cfr896%3A0%2Cfr398%3A0%2Cfr408%3A0%2Cfr251%3AA%2Cfr1195%3A0%2Cfr848%3A0%2Cfr1196%3A0%2Cfr1055%3A0%2Cfr902%3A0%2Cfr1054%3A0%2Cfr901%3A0%2Cfr980%3A0%2Cfr1570%3A0%2Cfr713%3A0%2Cfr1575%3A0%2Cfr1051%3A0%2Cfr1053%3A0%2Cfr1052%3A0%2Cfr259%3AS0-4%2Cfr1655%3A0%2Cfr1864%3A0%2Cfr884%3A0%2Cfr863%3A0%2Cfr1862%3A0%2Cfr1527%3A0%2Cfr1799%3A0%2Cfr344%3A0%2Cfr249%3AA1%2Cfr328%3A3105%2Cfr1544%3A0%2Cfr1543%3A0%2Cfr1521%3A0',
    'vip_sec_fp_smtoken': 'BVMJy4/lrs4xggcx+1S92+iU4ALIl5gVGT/bziXDr1uqvkwObD6o+4QkPz/rapIq2rmYqoLJCqhKVYAOpPQWgpg==',
    '_jzqco': '%7C%7C%7C%7C%7C1.1233541264.1772412222102.1772412222102.1772412446636.1772412222102.1772412446636.0.0.0.2.2',
    'tfs_fp_token': 'BVMJy4/lrs4xggcx+1S92+iU4ALIl5gVGT/bziXDr1uqvkwObD6o+4QkPz/rapIq2rmYqoLJCqhKVYAOpPQWgpg%3D%3D',
    'vip_sec_fp_wtk': 'cwEAAzBqMYV6l0A1NuSuiAj83JZsTwNTaJCGTGURlT0-aVHbhpR4qtUX-H-dTU-qS-_77LswOxfqTZaWfMfgJVY0IxB5Nmg',
    'pg_session_no': '9',
    'vip_tracker_source_from': '',
    'tfs_fp_timestamp': '1772413740219',
    'waitlist': '%7B%22pollingId%22%3A%223CA8022E-2720-4AC1-8D4A-49BDCB68485E%22%2C%22pollingStamp%22%3A1772413852733%7D',
    'domain': '.vip.com'
        }

    def send_request(self):
        # 1. 先访问主站（必须是 http://www.vip.com），建立域名上下文
        self.browser.get('https://www.vip.com')
        time.sleep(3)  # 给页面一点时间加载

        # 2. 添加 Cookie 时，必须强制指定 domain
        for k, v in self.cookies.items():
            try:
                # 明确指定 domain 为 .vip.com，确保子域名共享
                self.browser.add_cookie({
                    'name': k,
                    'value': v,
                    'domain': '.vip.com'  # ⬅️ 这一行是核心
                })
            except Exception as e:
                # 有些 Cookie 可能因为域不匹配报错，我们忽略它继续
                print(f"添加 Cookie {k} 失败: {e}")
                pass

        # 3. 刷新页面，此时应该保持登录状态
        self.browser.refresh()
        time.sleep(5)  # 多等一会儿，看会不会闪退

    def main(self):
        # --- 执行任务 ---
        # 调用请求函数
        self.send_request()


# --- 程序入口 ---
# 创建 VIP 类的实例
vip = VIP()
# 调用 main 方法开始运行
vip.main()

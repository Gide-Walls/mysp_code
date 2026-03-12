import requests
import re
cookies = {
    'acw_tc': '2f67a48f17704582337667115edfc429bcf272c2618bf39936bcd430a11cb2',
    'track_id': '203afc82507be2e0614413668421bf13c82f70853d31064b26bda04deb9c1071a%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22track_id%22%3Bi%3A1%3Bs%3A55%3A%224b0e4bc2def3f2d4fac8de4f0c6075e069870c80ba2858.34751117%22%3B%7D',
    '__root_domain_v': '.houzi8.com',
    '_qddaz': 'QD.182370458276007',
    '_qdda': '2-1.3t0f2d',
    '_qddab': '2-hz59jg.mlc55lhg',
    'lastSE': 'baidu',
    'user_source': '938d6df6cf78cfa92ec9f3560e481be78db15c03543dab8010399687e82068b9a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22user_source%22%3Bi%3A1%3Bi%3A1%3B%7D',
    'user_source_permanent': 'c94a58d3f3c9ae2a4357f23e9a97df55f56d3d6833b5d140506d2b3ded7b7320a%3A2%3A%7Bi%3A0%3Bs%3A21%3A%22user_source_permanent%22%3Bi%3A1%3Bi%3A1%3B%7D',
    'todayViewMark': '869ad589fae6c88a6771e92dcd4c6244ecb5a7f270c1b784ad38801ba6646923a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22todayViewMark%22%3Bi%3A1%3Bi%3A1%3B%7D',
    '_search_kw': '81d9dbe5408c199f8f7b700576caf8cd37d0063bf1145c8becd03dc71f6c0379a%3A2%3A%7Bi%3A0%3Bs%3A10%3A%22_search_kw%22%3Bi%3A1%3Bs%3A0%3A%22%22%3B%7D',
    'Hm_lvt_bb1a215c22b753f9361786dbc9433727': '1770458336',
    'HMACCOUNT': '2E19AF7687D7BA0D',
    '_c_WBKFRo': 'ntXTqcsDqmIqsJBjEfCDO581pnyEISNSxl8rFejG',
    '_nb_ioWEgULi': '',
    'Hm_lpvt_bb1a215c22b753f9361786dbc9433727': '1770458356',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.baidu.com/link?url=JAex5Vbewu3qOEr9l8dgA5PC7gYfvAhiTHoPwaOynaZ3Z-Ti3J-qdH27mZ9Ei7pb&wd=&eqid=98cc6594000766e10000000369870c6b',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    # 'cookie': 'acw_tc=2f67a48f17704582337667115edfc429bcf272c2618bf39936bcd430a11cb2; track_id=203afc82507be2e0614413668421bf13c82f70853d31064b26bda04deb9c1071a%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22track_id%22%3Bi%3A1%3Bs%3A55%3A%224b0e4bc2def3f2d4fac8de4f0c6075e069870c80ba2858.34751117%22%3B%7D; __root_domain_v=.houzi8.com; _qddaz=QD.182370458276007; _qdda=2-1.3t0f2d; _qddab=2-hz59jg.mlc55lhg; lastSE=baidu; user_source=938d6df6cf78cfa92ec9f3560e481be78db15c03543dab8010399687e82068b9a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22user_source%22%3Bi%3A1%3Bi%3A1%3B%7D; user_source_permanent=c94a58d3f3c9ae2a4357f23e9a97df55f56d3d6833b5d140506d2b3ded7b7320a%3A2%3A%7Bi%3A0%3Bs%3A21%3A%22user_source_permanent%22%3Bi%3A1%3Bi%3A1%3B%7D; todayViewMark=869ad589fae6c88a6771e92dcd4c6244ecb5a7f270c1b784ad38801ba6646923a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22todayViewMark%22%3Bi%3A1%3Bi%3A1%3B%7D; _search_kw=81d9dbe5408c199f8f7b700576caf8cd37d0063bf1145c8becd03dc71f6c0379a%3A2%3A%7Bi%3A0%3Bs%3A10%3A%22_search_kw%22%3Bi%3A1%3Bs%3A0%3A%22%22%3B%7D; Hm_lvt_bb1a215c22b753f9361786dbc9433727=1770458336; HMACCOUNT=2E19AF7687D7BA0D; _c_WBKFRo=ntXTqcsDqmIqsJBjEfCDO581pnyEISNSxl8rFejG; _nb_ioWEgULi=; Hm_lpvt_bb1a215c22b753f9361786dbc9433727=1770458356',
}
try:
    response = requests.get('https://houzi8.com/peiyue.html', cookies=cookies, headers=headers)
    response.encoding=response.apparent_encoding
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"请求失败{e}")
else:
    file_oath="respones_html.html"
    with open("爬虫基础\day005数据提取方法\资料.html","w",encoding=('utf-8')) as f:
        f.write(response.text)
        print("文字成功写入")


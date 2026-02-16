import requests
import re
import os
class Sprder(object):
    '''一个爬虫大类'''
    def __init__(self):
        self.url='https://houzi8.com/peiyue.html'
        self.cookies = {
    'track_id': '2c51405a401dbcabf93c3be72210209805609ce9c0e4209f1b611ae00ab4d66ba%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22track_id%22%3Bi%3A1%3Bs%3A55%3A%229cbdb07078e7c45d1e77a3fe447943db69872200861af8.05469243%22%3B%7D',
    'user_source_permanent': 'ec72e66ff8937b7269a3b0e32735307d45c3216a8698bd9784db7b7d63d57599a%3A2%3A%7Bi%3A0%3Bs%3A21%3A%22user_source_permanent%22%3Bi%3A1%3Bs%3A5%3A%2224233%22%3B%7D',
    'Hm_lvt_bb1a215c22b753f9361786dbc9433727': '1770463809',
    'HMACCOUNT': '4A9AF316C4627FCF',
    '__root_domain_v': '.houzi8.com',
    '_qddaz': 'QD.485170464377620',
    'lastSE': 'baidu',
    '_c_WBKFRo': 'DTlbFrsMFNLYORsFh8gJEKShWI6WcPYuBdoVya9k',
    '_nb_ioWEgULi': '',
    'acw_tc': '2f67a48f17704826371301410edfe1c02bf44f5cdadbde63883714a8264f4e',
    'user_source': '6e0c573f80366faa3099852e9d60a0cbd40a7e0d6df2fbdbbdff544a120ce61aa%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22user_source%22%3Bi%3A1%3Bs%3A5%3A%2224233%22%3B%7D',
    'todayViewMark': '869ad589fae6c88a6771e92dcd4c6244ecb5a7f270c1b784ad38801ba6646923a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22todayViewMark%22%3Bi%3A1%3Bi%3A1%3B%7D',
    'Hm_lpvt_bb1a215c22b753f9361786dbc9433727': '1770482637',
    '_qdda': '2-1.lshkp',
    '_qddab': '2-fsr2pf.mlcjnesq',
}
        self.headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.baidu.com/other.php?sc.Ks0000jTlPXflbDSWqA-gaklW2IBjkqsPxm7Pa8mC9AV10fTB-2LpB1mQwaZNP8JiV0vCABLx3LbaAl9HYl22IzV28qgJjDtg6UYNh_4iIBzWsQRO2eeHYWNi227lELaZEFp1T_LBRtvbRz9naq5nOZI4Y5Fi0ZiQMXlCHmWEYjAiVEfCEWvDFd9rC6GGzk0Osqb26WijLX8qktqu_F50Ej8xWbF.7b_NR2Ar5Od66JI63geDfmYEYmDqtDXFWFvur57i_nYQZHb_tU0.TLFWgv-b5Hczn1D0TLFWpyfqnWc1nfKk5UoEdq5iqnjy0ZwV5UoEdq5iqnjy0ZN1ugFxIZ-suHYs0A7bgLw4TARqP6KLULFb5UoEdq5iqnjy0ZFWIWYs0ZNzU7qGujYkPHTvPHfsn1bk0Addgv-b5HDLnHbvP1DY0AdxpyfqnHfvPWm4rjT0UgwsU7qGujYkn101P6KsI-qGujYs0A-bm1dcfbD0TA-b5Hck0APGujYkPHn0ug9sgLwGUyRqnHT3n104Pjfsn0K1mNqhUA7M5H00mLFW5HcYrHfd&ck=7661.30.75.254.404.499.366.317&dt=1770458219&wd=%E7%8C%B4%E5%AD%90%E9%9F%B3%E4%B9%90&tpl=tpl_13036_38394_0&l=1576540391&ai=0_429046584_1_0&us=linkVersion%3D1%26compPath%3D10048.0-10063.1-10065.1-10058.3%26label%3D%25E4%25B8%25BB%25E6%258C%2589%25E9%2592%25AE%26linkType%3D%26linkText%3D%25E8%25BF%259B%25E5%2585%25A5%25E6%259B%25B2%25E5%25BA%2593',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    # 'cookie': 'track_id=2c51405a401dbcabf93c3be72210209805609ce9c0e4209f1b611ae00ab4d66ba%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22track_id%22%3Bi%3A1%3Bs%3A55%3A%229cbdb07078e7c45d1e77a3fe447943db69872200861af8.05469243%22%3B%7D; user_source_permanent=ec72e66ff8937b7269a3b0e32735307d45c3216a8698bd9784db7b7d63d57599a%3A2%3A%7Bi%3A0%3Bs%3A21%3A%22user_source_permanent%22%3Bi%3A1%3Bs%3A5%3A%2224233%22%3B%7D; Hm_lvt_bb1a215c22b753f9361786dbc9433727=1770463809; HMACCOUNT=4A9AF316C4627FCF; __root_domain_v=.houzi8.com; _qddaz=QD.485170464377620; lastSE=baidu; _c_WBKFRo=DTlbFrsMFNLYORsFh8gJEKShWI6WcPYuBdoVya9k; _nb_ioWEgULi=; acw_tc=2f67a48f17704826371301410edfe1c02bf44f5cdadbde63883714a8264f4e; user_source=6e0c573f80366faa3099852e9d60a0cbd40a7e0d6df2fbdbbdff544a120ce61aa%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22user_source%22%3Bi%3A1%3Bs%3A5%3A%2224233%22%3B%7D; todayViewMark=869ad589fae6c88a6771e92dcd4c6244ecb5a7f270c1b784ad38801ba6646923a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22todayViewMark%22%3Bi%3A1%3Bi%3A1%3B%7D; Hm_lpvt_bb1a215c22b753f9361786dbc9433727=1770482637; _qdda=2-1.lshkp; _qddab=2-fsr2pf.mlcjnesq',
}
    def sprder_get(self):
        '''请求发送'''

        response=requests.get(self.url,headers=self.headers,cookies=self.cookies)
        return response.text
    
    def response_re(self):
        '''正则筛选出数据'''

        re_host=r'title:"([^"]+)".*?preview_url_o:"([^"]+\.mp3)"'

        get_data=self.sprder_get()

        results=re.findall(re_host,get_data,re.DOTALL)

        return results
    def response_write(self):
        results=self.sprder_get()
        with open(r"爬虫基础\day005数据提取方法\html文件资料\day001数据.html","w",encoding="utf-8")as f:
            f.write(results)
    
    def for_data(self):

        results=self.response_re()
        print(f"共匹配到 {len(results)} 条数据：")

        for idx,(title, mp3_url) in enumerate(results,1):
            title_name=f"{title}.mp3"
            mp3_url1=mp3_url.replace(r'\u002F','/')
            dao_data=r"爬虫基础\day005数据提取方法\整合知识点\音乐下载"
            print(idx,title,mp3_url)

            request_get_music=requests.get(mp3_url1)

            with open(f"{dao_data}/{title_name}","wb") as f:
                f.write(request_get_music.content)

if __name__ == '__main__':
    aaa=Sprder()
    # aaa.for_data()
    aaa.response_write()
    aaa.for_data()





    
    

    






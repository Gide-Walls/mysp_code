import requests
import json
import time
import queue
from pymongo import MongoClient
import threading
import random
class Spader(object):
    def __init__(self):
        self.url=r'https://talent-holding.alibaba.com/position/search'
        self.headers={'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'bx-v': '2.5.11',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://talent-holding.alibaba.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://talent-holding.alibaba.com/off-campus/position-list?lang=zh',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36'}
        self.parasm={
    '_csrf': '68346f66-ee32-4af2-b2a5-ff8a3e2881e4'}
        self.cookies= {
    'cna': '9c8YIkL7ylECAd9lXORvbtHc',
    'xlly_s': '1',
    'XSRF-TOKEN': '68346f66-ee32-4af2-b2a5-ff8a3e2881e4',
    'prefered-lang': 'zh',
    'SESSION': 'QTU0QkJDNTVCMUFDN0Y0MTM2MkM2NkJGOUI1QTY4NzQ=',
    'tfstk': 'gJ9s-twJ-P46Z9ntkPoUPc0s1YXjYDkzWosvqneaDOBODtTHPsy2XK8jcUY1gF-xsmMXlEimjn3MlK_p-IR2XVXXhnx7QNBVQZHXqF_NghLqhZKlBsANuN7fhnYSY4krUhxGn93rzYyhUL4lElFAXr5LJgBfX5UaU0-Gnt3UY-hrFhYZgT7cMtnCpisOXtCOD9nC4iWYBseT9yQhDtBAWZCdvgSbMPeTBDtd-iBAX1LApDsVJZBAHEKKh7y1Yc_HfmgWK4nQBLxOR-evBxf1P1N4h-_dX1tDmwsFYps11aCjxN2MBe-vQdfnWP6DYQTXME3_QMAy7dfe1y3fyC8MIOvqzSWH6FJCsH07INOpSEBwe0Pcxs_69dCQD-KCCZTkGFg_sNdwR_jd9oMlYU7pjddImyK9zN6Ov6k-VHCvTdfkQ2e1eQxNQILx5RSHaFJGTCa14CyPPzSUGk1uhM_rADN0iOR28qhHlMOc6MjEuDiQanfOxMQD3DNIm1IhYnoIA7-c.',
    'isg': 'BDs7z0Y31tDVhOpn_Nx2hsy1yh-lkE-SW8lAwC34djpbjFputWMa40yKpizCn6eK',
}     
        self.q=queue.Queue()
        self.q_response=queue.Queue(maxsize=5)
    def put_num(self):
        '''添加翻页参数'''
        for i in range(1,45):
            self.q.put(i)
    def requset_data(self):
        '''获取完整data'''
        try:
            i=self.q.get()
        except queue.Empty:
            raise
        passjson_data = {
            'channel': 'group_official_site',
            'language': 'zh',
            'batchId': '',
            'categories': '',
            'deptCodes': [],
            'key': '',
            'pageIndex': i,
            'pageSize': 10,
            'regions': '',
            'subCategories': '',
            'shareType': '',
            'shareId': '',
            'myReferralShareCode': '',
                        }
        return passjson_data
    def request_post(self,data):
        '''发送请求'''
        response=requests.post(self.url,cookies=self.cookies,params=self.parasm,headers=self.headers,json=data)  
        return response.json()
    def seav_res(self):
        '''保存函数'''
        with MongoClient('localhost', 27017) as client: 
            db = client['my_database'] 
            collection = db['my_collection']
            while True:            
                try:
                    data=self.q_response.get(timeout=3)
                    collection.insert_one(data)
                except queue.Empty:
                    if all(not t.is_alive()for t in threads):
                        break    
    def main(self):
        '''入口函数'''
        while True:
            delay=random.uniform(1,2)
            time.sleep(delay)
            try:
                data=self.requset_data()
                response=self.request_post(data)
                self.q_response.put(response)
            except queue.Empty:
                print("url队列空了")
                break   
if __name__ == '__main__':
    aaa=Spader()
    aaa.put_num()
    threads=[threading.Thread(target=aaa.main)for _ in range(3)]
    for i in threads:
        i.start()
    t=threading.Thread(target=aaa.seav_res)
    t.start()
    
    t.join()
    print("保存完成")
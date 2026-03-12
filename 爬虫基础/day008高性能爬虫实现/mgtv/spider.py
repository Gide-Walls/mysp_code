import time
import requests
import threading
import random
import queue
import json
from pymongo import MongoClient
import redis
import hashlib
class Spider(object):
    '''大类'''
    def __init__(self):
        #url
        self.url=r"https://pianku.api.mgtv.com/rider/list/pcweb/v3"
        #获取cookie
        self.session=requests.session()
        self.session.headers={
            "user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
        }
        self.session.get(r"https://www.mgtv.com/lib/3")
        #连接数据库
        self.mongo_client = MongoClient("mongodb://localhost:27017/")
        self.collection = self.mongo_client["mgtv_db"]["video_data"]
        self.redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
        self.de=self.redis_client.delete("quchon")
        #创建队列
        self.q=queue.Queue()
        self.put_q()
        self.q_get_data=queue.Queue(maxsize=10)
    def md5_encode(self,data):
        '''md5加密成哈希'''
        return hashlib.md5(str(data).encode()).hexdigest()
    def put_q(self):
        '''翻页pn'''
        for i in range(1,8):
            self.q.put(i)
    def get_data(self):
        '''params数据往队列添加'''
        try:
            pn=self.q.get(timeout=1)
            params = {
                'allowedRC': '1',
                'platform': 'pcweb',
                'channelId': '3',
                'pn': str(pn),
                'pc': '80',
                'hudong': '1',
                '_support': '10000000',
                'kind': 'a1',
                'edition': '182',
                'area': 'a1',
                'year': 'all',
                'chargeInfo': 'a1',
                'sort': 'c2',
                }
            return params
        except queue.Empty:
            raise
    
    def requset_get(self):
        '''请求发送'''
        parasm=self.get_data()
        
        response=self.session.get(self.url,params=parasm)
        # print(response.text)
        self.q_get_data.put(response.json())

    def filter_data(self,request_threads):
        '''数据筛选'''
        while True:
            try:
                original_data=self.q_get_data.get(timeout=3)
                try:
                    for times in original_data["data"]["hitDocs"]:
                        dict_data={}
                        dict_data["kind"]=",".join(times["kind"]) if isinstance(times["kind"],list) else str(times["kind"])
                        dict_data["story"]=times["story"]
                        dict_data["subtitle"]=times["subtitle"]
                        dict_data["title"]=times["title"]
                        dict_data["year"]=times["year"]
                        md5=self.md5_encode(dict_data)
                        if not self.redis_client.sismember("quchon",md5):
                            self.redis_client.sadd("quchon",md5)
                            self.collection.insert_one(dict_data)
                            print("写入成功")
                        else:
                            print("重复数据")
                            
                except Exception as e:
                    print(f"单条数据插入失败报错{e}")
            except queue.Empty:
                if all(not t.is_alive() for t in request_threads):
                    self.redis_client.delete("quchon")
                    print("程序正常关闭")
                    break
    def res(self):
        '''控制请求数量'''
        while True:
            try:
                by=random.uniform(0.3,1)
                time.sleep(by)
                self.requset_get()
                
            except queue.Empty:
                break
if __name__ == '__main__':
    aaa=Spider()
    threader=[]
    for _ in range(2):
        t=threading.Thread(target=aaa.res)
        threader.append(t)
        t.start()
    sta=threading.Thread(target=aaa.filter_data,args=(threader,))
    sta.start()
    sta.join()
print("采集完成")
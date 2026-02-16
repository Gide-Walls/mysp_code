from concurrent.futures import ThreadPoolExecutor
from requests_get_1 import request_dir
from read_local_file import default
from requests_get_list_2 import requests_get_2
from def_path import seve_content
import threading  # 新增：排队锁的工具
import random     # 新增：随机等多久的工具
import time  
request_lock = threading.Lock()

#获取响应
response=request_dir()
#里面是列表
day_url_name=default(response)
print(day_url_name)

def process_one(item):
    
    day,url,name=item
    with request_lock:
        delay=random.uniform(1,3)
        time.sleep(delay)
        
        result=f"{name}\n{requests_get_2(url)}"
        seve_content(day,result)
    
with ThreadPoolExecutor(3)as executor:
    executor.map(process_one,day_url_name)
    

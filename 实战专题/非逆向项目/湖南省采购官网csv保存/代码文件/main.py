
from request_need import url_headers_data
from request_post import request_posts
from save import write_csv_header,write_csv_data
import queue
import threading
import time
q=queue.Queue()
q_response=queue.Queue(maxsize=5)
request_lock = threading.Lock()
write_csv_header()
task_list=[url_headers_data(i) for i in range(1,11)]
for task in task_list:
    q.put(task)

def star():
    '''生产响应'''

    x=q.get(timeout=3)
    url = x[0]          # 提取URL：第0个元素
    headers = x[1]      # 提取headers：第1个元素
    data = x[2]
    
    print(x)
    json_data=request_posts(url,headers,data)
    # print(json_data)
    q_response.put(json_data)
        
def seav_csv():
    '''消费响应'''
    while True:
        try:
            data=q_response.get(timeout=3)
            for i in data:
                row = [
                        i["RN"],
                        i["AREA_NAME"],
                        i["TITLE"],
                        i["STAFF_DATE"]
                    ]
                print(row)
                write_csv_data(row)
        except queue.Empty:
            if all(not t.is_alive() for t in threads):
                break
if __name__ == '__main__':
    
    threads=[]
    def res():
        while True:
            try:
                with request_lock:
                    star()
                time.sleep(0.5)
            except queue.Empty:
                break
             
        
    for _ in range(3):
        t=threading.Thread(target=res)
        threads.append(t)
        t.start()
    tsave=threading.Thread(target=seav_csv)
    tsave.start()
    tsave.join()
        
        
    

import queue
import threading
from requsets_get_url import requsets_get
from file_save import w_html
from lxml_get_xpath import lxml_get_xpaths

url_list=[f"https://www.gushiwen.cn/mingjus/default.aspx?page={i+1}&tstr=&astr=&cstr=&xstr="for i in range(4)]
q_response=queue.Queue(maxsize=2)
q=queue.Queue()

#循环会卡死主线程q=queue.Queue()设置数量为2的时候
for i in url_list:
    q.put(i)
    
    
def fetch():
    '''发送请求'''
    while not q.empty():
        url=q.get(timeout=2)
        print(threading.current_thread().name,"生产者线程开始工作",url)
        response=requsets_get(url)
        q_response.put((url,response))
        q.task_done()
def parse():
    '''解析数据'''
    for _ in range(len(url_list)):
        print("消费者线程开始工作",threading.current_thread().name)
        url,res=q_response.get()
        lxml_get_xpaths(res)
        w_html(url,res)
        q_response.task_done()
if __name__ == '__main__':
    t1=threading.Thread(target=fetch)
    t2=threading.Thread(target=parse)
    t1.start()
    t2.start()
    
    q.join()
    q_response.join()
   
    print("工作完成")
# def run():
#     '''run方法'''
#     url=q.get()
#     print(threading.current_thread().name,"正在爬",url)
#     response=requsets_get(url)
#     w_html(url,response)
#     lxml_get_xpaths(response)
#     print(threading.current_thread().name,"完成爬",url)
# for i in range(3):
#     t=threading.Thread(target=run)
#     t.start()




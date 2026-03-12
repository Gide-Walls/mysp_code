import requests
from retrying import retry

@retry(stop_max_attempt_number=3)
def get_url(url):
    print(url)
    res=requests.get(url,timeout=0.01)
    return res
def parse_data():
    try:
        url="https://www.baidu.com/"
        get_url(url)
    except:
        #日志
        print("报错的网址是",url)



parse_data()
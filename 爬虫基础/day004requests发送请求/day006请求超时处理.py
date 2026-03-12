import requests
url="https://www.baidu.com/"

#设置超时 时间如果 1秒钟还没响应对象那么报错
req=requests.get(url,timeout=1)#timeout=1设置请求时间
print(req)
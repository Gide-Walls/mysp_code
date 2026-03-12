import requests


#session() 会话保持  自动储存cookie 自动把响应的cookie带着
session=requests.session()

#首页url
url1="https://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice"

haerdes={
    
    "user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
}


res=session.get(url1,headers=haerdes)
data = {
    'column': 'szse_main_latest',
    'pageNum': '1',
    'pageSize': '30',
    'sortName': '',
    'sortType': '',
    'clusterFlag': 'true'
}

# res1=requests.post(url1,data,headers=haerdes)
# print(res1.request.headers)
res1=session.post(url1,data,headers=haerdes)
print(res1.request.headers)

#两种请求方式

import requests
#第一种
# url="https://www.baidu.com/s?ie=UTF-8&wd=python"
# response=requests.get(url)
# print(response.text)


#第二种 加问号添加数据
url="https://www.baidu.com"
params={
    "query":"python"
}
response=requests.get(url,params=params)
# 1
# response.encoding="utf-8"
# print(response.text)

# 2
print(response.content.decode("utf-8"))
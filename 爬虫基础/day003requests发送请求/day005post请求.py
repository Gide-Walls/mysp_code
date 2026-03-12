import requests
import json
url="https://www.cninfo.com.cn/new/disclosure"

headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
}
data={
"column":"szse_main_latest",
"pageNum":1,
"pageSize":30,
"sortName":"sortType"
"clusterFlag""true"
}
response=requests.post(url=url,data=data,headers=headers)
# print(response.content.decode("utf-8"))
# data 请求体
# print(json.loads(response.text))
print(response.json())


# 在Python中 json是单引号
#在python中   字典是双引号
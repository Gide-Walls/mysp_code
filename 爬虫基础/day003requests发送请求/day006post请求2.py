import requests


# 获取资源资源地址
url = 'https://www.ccgp-anhui.gov.cn/portal/category'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
}
data = {
    'categoryCode': 'anhuiCategory102',
    'pageNo': 5,
    'pageSize': 15,
    '_t': 1756820627000
}
# 发送请求
# 关注载荷 有时候是column=szse_main_latest&pageNum=1&pageSize=30&sortName=&sortType=&clusterFlag=true 没关系
#有时候是 {"code":"anhuiCategory12","subCodes":["anhuiCategory102"],"isStick":true}这种 
#要用 json=data 解决
response = requests.post(url, headers=headers, json=data)
print(response.text)
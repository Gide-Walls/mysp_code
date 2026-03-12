import requests
url="https://baidu.com"
#伪装的请求 获取浏览器一致的内容
headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
}
response=requests.get(url,headers=headers)

# 请求头
print(response.request.headers)
print(response.text)
#{'User-Agent': 'python-requests/2.32.5', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
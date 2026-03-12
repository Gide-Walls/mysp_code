import requests
import time

# 不使用代理，直接访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    # 'Referer': 'https://qq.ip138.com/'
}

proxy = {"http": "http://101.37.27.102:80",
                      "https": "http://101.37.27.102:80"}
url = "http://httpbin.org.get"

# 添加适当延迟
time.sleep(2)

try:
    response = requests.get(url, headers=headers, timeout=2, proxies=proxy)
    # response.encoding = 'gbk'

    if response.status_code == 200:
        print("✅ 访问成功")
        # 处理页面内容
    else:
        print(f"状态码: {response.status_code}")

except Exception as e:
    print(f"请求失败: {e}")
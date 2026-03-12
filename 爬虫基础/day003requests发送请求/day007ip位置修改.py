import requests

proxies = {
    "http": "http://127.0.0.1:7890",
    "https": "http://127.0.0.1:7890"
}
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}
try:
    response = requests.get("https://2025.ip138.com/", headers=headers, proxies=proxies)
    response.encoding = 'utf-8'
    print(response.text)
except requests.RequestException as e:
    print(f"请求发生错误: {e}")
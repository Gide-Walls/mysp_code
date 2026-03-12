import json
import requests
def read():
    with open(r"serve_ip/ip_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        return data
def for_data(read, func):
    data = read
    for i in data:
        ip = i["ip"][0]
        port = i["port"][0]
        func(ip, port)
def request_get(ip, ids):
    yes_ip = []
    url = "http://httpbin.org.get"
    proxy = {"http": f"{ip}:{ids}",
             "https": f"{ip}:{ids}"}
    res = None
    try:
        res = requests.get(url, proxies=proxy, verify=False,timeout=0.1)
    except Exception as e:

        print("ip有问题")
    if res is not None:
        if res.status_code == 200:
            yes_ip.append({
                "ip": ip,
                "ids": ids,
            })
        else:
            print("ip不可用")
        print(yes_ip)
if __name__ == '__main__':
    read_data = read()
    for_data(read_data, request_get)

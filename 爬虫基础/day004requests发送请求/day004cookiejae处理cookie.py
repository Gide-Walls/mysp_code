import requests


url="https://www.baidu.com/"
response=requests.get(url)
# print(response.content.decode("utf-8"))
# print(response.cookies)
# #用get提取
# print(response.cookies.get("BDORZ"))


#cookiejae 手动获取cookie
cookie_data=requests.utils.dict_from_cookiejar(response.cookies)
print(cookie_data["BDORZ"])
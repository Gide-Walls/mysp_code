# import requests

# # content- 万能二进制

# # text- 文本阅读

# # json()- JSON 专用

# # raw- 流式处理
# url="https://img1.baidu.com/it/u=1973472985,1487310875&fm=253&app=138&f=JPEG?w=927&h=800"

# headers={
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
# }
# a=requests.get(url,headers=headers)
# with open("小朋友.jpg","wb")as f:
#     f.write(a.content)


import requests
import json

# 目标url
url="https://www.baidu.com"


# 向目标url发送请求

# response=requests.get(url)

# # 单独打印状态码结果是 <Response [200]>
# print(response)
# #单独查看响应状态码 200
# print(response.status_code)

#查看响应体 str 字符串的数据类型  
# 页面或者文本数据用这个
# print(response.text)

# # content 是bytes 字符类型
# print(response.content)

# # 查看响应头
# print(response.headers)

# #查看响应cookei
# print(response.cookies)

# #查看json对象 把json对象转换成字典
# # response.json()
# cookies_dict = requests.utils.dict_from_cookiejar(response.cookies)
# print(json.dumps(cookies_dict, indent=2, ensure_ascii=False))

response=requests.get(url)
# response.encoding="utf-8"#网页上查看 编码格式然后指定
# print(response.text)

print(response.content.decode("utf=8"))
# content 是bytes数据 可以进行解码decode("utf=8"))指定解码




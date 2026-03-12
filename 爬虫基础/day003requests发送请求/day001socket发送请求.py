import socket
import re

#图片地址 url=https://img1.baidu.com/it/u=1973472985,1487310875&fm=253&app=138&f=JPEG?w=927&h=800
url="https://img1.baidu.com/it/u=1973472985,1487310875&fm=253&app=138&f=JPEG?w=927&h=800"


http_request='GET' + url + "HTTP/1.1\r\n" + 'user-agent : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36\r\n\n'
# 获取网址

# 请求体

# 要加一个 host
# 发送请求
#创建套接字对象
client = socket.socket()

# 创建连接 两个参数 ip地址 和 端口
client.connect(("img1.baidu.com",80))
client.send(http_request.encode())


# 获取到数据
data=client.recv(1024)
print(data)
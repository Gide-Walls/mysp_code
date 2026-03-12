import socket
import ssl

url = "https://img1.baidu.com/it/u=1973472985,1487310875&fm=253&app=138&f=JPEG?w=927&h=800"

# 提取主机和路径
host = "img1.baidu.com"
path = "/it/u=1973472985,1487310875&fm=253&app=138&f=JPEG?w=927&h=800"

# 构建请求
request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"

# 创建连接（HTTPS）
context = ssl.create_default_context()
sock = socket.socket()
secure_sock = context.wrap_socket(sock, server_hostname=host)
secure_sock.connect((host, 443))

# 发送请求并接收数据
#一般取1024 然后循环拼接就好
secure_sock.send(request.encode())
data = secure_sock.recv(8192)
secure_sock.close()

# 提取图片数据（跳过HTTP头）
content = data.split(b"\r\n\r\n", 1)[1] if b"\r\n\r\n" in data else data

# 保存图片
with open("image.jpg", "wb") as f:
    f.write(content)
print("图片下载完成")
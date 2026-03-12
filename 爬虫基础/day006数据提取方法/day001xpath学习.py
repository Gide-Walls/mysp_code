import requests

url=r"https://www.gushiwen.cn/mingjus/default.aspx?page=1&tstr=&astr=&cstr=&xstr="


headers={
    "user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
}

response=requests.get(url=url,headers=headers)

def w_html():
    path_1=r"爬虫基础\day006数据提取方法\数据"
    with open(f"{path_1}/古诗文.html","w",encoding="utf-8")as f:
        f.write(response.text)
w_html()
print("文件写入成功")



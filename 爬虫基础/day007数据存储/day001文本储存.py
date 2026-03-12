# import requests
from itertools import zip_longest
from bs4 import BeautifulSoup
#文本储存
url=r"https://www.zhihu.com/explore"

hearders={
    "user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
}

# response=requests.get(url,hearders)
with open(r"爬虫基础\day007数据存储\请求数据保存\知乎.html","r",encoding="utf-8")as f:
    html_read=f.read()
soup=BeautifulSoup(html_read,"lxml")
result=soup.select('.css-4cffwv .css-1g4zjtl a')
results=soup.select(".css-4cffwv .css-1g034g9")
for i,x in zip_longest(result,results,fillvalue='无数据'):
    title=i.get_text()
    pinglun=x.get_text()
    print(title,pinglun)
    

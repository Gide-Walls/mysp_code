import requests
from lxml import html
import json
url="https://www.4399.com/flash/gamehw.htm"
headers={
    "user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
}

# response=requests.get(url,headers=headers)
# response.encoding='gbk'

# with open(r"爬虫基础\day007数据存储\请求数据保存\四399.html","w",encoding='utf-8')as f:
#     html_weite=f.write(response.text)







with open(r"爬虫基础\day007数据存储\请求数据保存\四399.html","r",encoding="utf-8")as f:
    html_read=f.read()

# print(html_read)

tree=html.fromstring(html_read)
titlse=tree.xpath('//ul[@class="tm_list"]/li')
game_list=[]
for i in titlse:
    hrefs=i.xpath('./a/@href')[0]
    game_name=i.xpath('./a/b/text()')[0]
    addrss_jpg=i.xpath('.//img/@lz_src') or i.xpath('.//img/@src')
    addrss_jpgs=addrss_jpg[0]
    
    game_list.append({
        "游戏名称":game_name,
        "链接":hrefs,
        '图片链接':addrss_jpg
    })
with open(r"爬虫基础\day007数据存储\请求数据保存\四399json.json",'w',encoding='utf-8')as f:
    f.write(json.dumps(game_list,ensure_ascii=False,indent=2,separators=(',',":")))


    
# print(game_list)
print(len(game_list))


from lxml import html
import csv
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
with open(r"爬虫基础\day007数据存储\请求数据保存\四399.csv","w",newline="",encoding="utf-8-sig")as f:
    headers=["游戏名称","链接","图片链接"]
    writer=csv.DictWriter(f,fieldnames=headers)
    writer.writeheader()
    for item in game_list:
        writer.writerow(item)
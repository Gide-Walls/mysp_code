import asyncio
from lxml import etree
import aiohttp
url='https://pvp.qq.com/web201605/herodetail/yuanliuzhizi_support.shtml'
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
}
async def aiohttp_get():
    async with aiohttp.ClientSession()as session:
        async with session.get(url,headers=headers)as resp:
            text=await resp.read()
            texts=text.decode('gbk')
            print(texts)
            return texts    
result=asyncio.run(aiohttp_get())
tree=etree.HTML(result)
list_div_5=tree.xpath(r"//div[@class='show-list']")
name1=tree.xpath(r"//h2/text()")[0]
data_list=[]
print(name1)
for i in list_div_5:
    name=i.xpath(r".//p[1]/b/text()")#技能名称
    mame_skill=i.xpath(r"./p[2]/text()")#技能介绍
    span_text1=i.xpath(r".//p[1]/span[1]/text()")[0]#冷却
    span_text2=i.xpath(r".//p[1]/span[2]/text()")[0]#消耗
    #判断name为空时就可以跳过最后空缺的技能了
    if name:
        data_list.append((name,span_text1,span_text2,mame_skill))
#元组套列表套元组
final=(name1,data_list)
print(final)

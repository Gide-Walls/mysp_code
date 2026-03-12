import asyncio
from lxml import etree
import aiohttp
import json
from pymongo import MongoClient
# url='https://pvp.qq.com/web201605/herodetail/yuange.shtml'
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
}
async def aiohttp_get(url,semaphore):
    '''请求发送'''
    async with semaphore:
        async with aiohttp.ClientSession()as session:
            async with session.get(url,headers=headers)as resp:
                text=await resp.read()
                texts=text.decode('gbk')
                return texts  
def url_list_data():
    '''获取url列表'''
    with open(r'爬虫基础\day009高配置爬虫实现\王者英雄资料\信息文件\英雄名称url.json',"r",encoding='utf-8')as f:
        url=json.load(f)
    data_list=[]
    for itme in url:
        url_str=itme["url"]
        data_list.append(url_str)
    return data_list  
def parse_hero(result):
    '''解析函数'''
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
            data_list.append({
                '技能名称':name,
                '冷却':span_text1,
                '消耗':span_text2,
                '技能介绍':mame_skill,
            })
    #元组套列表套元组
    final={name1:data_list}
    print(final)
    return final
async def main():
    '''入口函数'''
    client = MongoClient("localhost", 27017)
    db = client["wangzhe"]
    collection = db["dict_hero_skills"]
    semaphore=asyncio.Semaphore(5)
    url_list=url_list_data()
    for i in range(0,len(url_list),3):
        
        coutent=url_list[i:i+3]
        task=[]
        for url in coutent:
            task.append(aiohttp_get(url,semaphore))
        result=await asyncio.gather(*task)
        for html in result:
            资料=parse_hero(html)
            
            
            collection.insert_one(资料)
        await asyncio.sleep(2)
asyncio.run(main()) 
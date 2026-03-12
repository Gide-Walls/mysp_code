from lxml import html
import asyncio
import aiohttp
import json
url="https://pvp.qq.com/web201605/herolist.shtml"
headers={
    "user_agent":"'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'"
}
async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers=headers) as res:
            text=await res.read()
            html=text.decode('gbk')
            with open(r"爬虫基础\day009高配置爬虫实现\王者英雄资料\信息文件\英雄主页.html","w",encoding='gbk')as f:
                f.write(html)
            


 
async def main():
    await fetch()
if __name__ == '__main__':
    asyncio.run(main())
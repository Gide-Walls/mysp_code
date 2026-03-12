from lxml import html
import asyncio
import aiohttp
import json
url="https://pvp.qq.com/zlkdatasys/heroskinlist.json"
headers={
    "user_agent":"'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'"
}
async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers=headers) as res:
            text=await res.read()
            texts=text.decode('gbk')
            print("原始响应内容：", texts)
            data=json.loads(texts)
            print(data)
            with open(r"爬虫基础\day009高配置爬虫实现\王者英雄资料\信息文件\英雄.json","w",encoding='utf-8')as f:
                json.dump(data,f,ensure_ascii=False,indent=2,separators=(',',':'))
async def main():
    await fetch()
if __name__ == '__main__':
    asyncio.run(main())
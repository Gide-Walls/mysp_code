import asyncio
import aiomysql
import aiohttp
from lxml import etree

class QiChe():
    def __init__(self):
        self.url="https://chejiahao.autohome.com.cn/Authors/AuthorListMore?orderType=3&page={}&userCategory=13"
        self.headers={
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
        }
    async def get_data(self,session,pool,page):

        response=await session.post(self.url.format(page))
        html_data=await response.text()
        # print(await response.text())

        html=etree.HTML(html_data)
        div_list=html.xpath(r'//div[@class="list-box"]')
        for div in div_list:
            itme={}
            itme["author"]=div.xpath(r'.//div[@class="list-title"]/text()')[0]
            itme["intro"]=div.xpath(r'.//div[@class="list-mes"]/text()')[0]
            itme["fans"]=div.xpath(r'.//div[@class="list-num"]/span[@class="num"]/text()')[0]
            itme["works"]=div.xpath(r'.//div[@class="list-num"]/span[@class="num"][2]/text()')[0]
            await self.insert_data(itme,pool)

        return response.text()
    async def insert_data(self,itme,pool):
        async with pool.cursor()as cursor:
            sql = 'INSERT INTO qiche (id, author, intro, fans, works) VALUES (%s, %s, %s, %s, %s)'
            try:
    # 执行 SQL 插入操作
    # id 传入 0，数据库会自动按自增规则生成 ID
    # item 是包含数据的字典，需确保键名正确
                await cursor.execute(sql, (
                    0,
                    itme['author'],
                    itme['intro'],
                    itme['fans'],
                    itme['works']
                ))

                # 提交事务到数据库
                await pool.commit()
                print('数据插入成功...')

            except Exception as e:
                # 如果发生错误，打印错误信息
                print(f'数据插入失败: {e}')

                # 执行回滚操作，撤销本次事务中的所有更改
                await pool.rollback()


    async def main(self):
        pool = await aiomysql.connect(host="127.0.0.1",port=3306,user="root",password="root",db="test_db",loop=loop)
        cursor=await pool.cursor()
        create_sql = '''
                CREATE TABLE IF NOT EXISTS qiche(
                    id int primary key auto_increment not null,
                    author VARCHAR(255) NOT NULL,
                    intro VARCHAR(255) NOT NULL,
                    fans VARCHAR(255) NOT NULL,
                    works VARCHAR(255) NOT NULL
                );
                '''
        await cursor.execute(create_sql)

        async with aiohttp.ClientSession(headers=self.headers) as session:
            tasks = []
            for page in range(20,30):
                await asyncio.sleep(5)
                res = await self.get_data(session,pool,page)
                task = asyncio.create_task(res)
                tasks.append(task)

            await asyncio.wait(tasks)

        await cursor.close()
        pool.close()
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    qiche = QiChe()
    loop.run_until_complete(qiche.main())

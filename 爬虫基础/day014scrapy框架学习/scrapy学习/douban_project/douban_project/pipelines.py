# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class DoubanProjectPipeline:
    # 爬虫开始时候执行一次
    # def __init__(self):
    #     self.db = None
    #     self.cursor = None

    def open_spider(self, spider):
        self.db = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", database="test_db",
                                  charset="utf8")
        self.cursor = self.db.cursor()
        sql = '''
        CREATE TABLE IF NOT EXISTS douban(
            id int primary key auto_increment not null,
            quote VARCHAR(255) NOT NULL,
            rating VARCHAR(255) NOT NULL,
            title VARCHAR(255) NOT NULL 
        )
        '''
        try:
            self.cursor.execute(sql)
            # self.connection.commit()  # 提交事务
            print("CREATE TABLE SUCCESS.")
        except Exception as ex:
            # self.connection.rollback()  # 回滚事务
            print(f"CREATE TABLE FAILED, CASE:{ex}")

    def process_item(self, item, spider):

    # print("1111", item)
        sql = ''' INSERT INTO DOUBAN(id ,quote,rating,title) VALUES(%s,%s,%s,%s)
                  '''
        try:
            self.cursor.execute(sql, (0, 0, 0, item["名字"]))
            self.db.commit()
            print("数据插入成功")
        except Exception as ex:
            print(f"数据插入失败{ex}")
            # 数据进行回滚
            self.db.rollback()



    def close_spider(self, spider):
        # 爬虫结束时候调用一次
        self.db.close()

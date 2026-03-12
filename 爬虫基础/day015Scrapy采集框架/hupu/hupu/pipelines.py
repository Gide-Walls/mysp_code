# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from hupu.items import HupuItem
from hupu.items import UncommentItem
import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client['hupu']
class HupuPipeline:

    def process_item(self, item, spider):
        if isinstance(item, HupuItem):
            db['主页新闻'].insert_one(dict(item))
            print(item)
        return item


class HupuCrawler:
    def process_item(self, item, spider):
        if isinstance(item, UncommentItem):
            db["评论"].insert_one(dict(item))
            print(item)
        return item
class MongodbClosePipeline:
    def close_spider(self, spider):
        client.close()
        print("数据库已关闭")

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HupuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tid = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    topicName = scrapy.Field()
    pageNum = scrapy.Field()
    detailUrl = scrapy.Field()


class UncommentItem(scrapy.Item):
    tid = scrapy.Field()
    title = scrapy.Field()

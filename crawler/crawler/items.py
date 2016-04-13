# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DoubanBookItem(scrapy.Item):
    book_title = scrapy.Field()
    book_link = scrapy.Field()
    book_comment = scrapy.Field()
    book_price = scrapy.Field()

class Next_Url(scrapy.Item):
    url = scrapy.Field()

class DomzItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

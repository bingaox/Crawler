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
    book_title = scrapy.Item()
    book_link = scrapy.Item()
    book_comment = scrapy.Item()
    book_price = scrapy.Item()


class DomzItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

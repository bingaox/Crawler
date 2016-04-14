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
    book_author = scrapy.Field()
    # book_publish_house = scrapy.Field()
    # book_pre_author = scrapy.Field()
    # book_translator = scrapy.Field()
    # book_publish_year = scrapy.Field()
    # book_page_num = scrapy.Field()
    # book_price = scrapy.Field()
    # book_stytle = scrapy.Field()
    # book_type = scrapy.Field()
    # book_isbn = scrapy.Field()
    book_score = scrapy.Field()

    book_remark = scrapy.Field()

class Next_Url(scrapy.Item):
    url = scrapy.Field()

class DomzItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

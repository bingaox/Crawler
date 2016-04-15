# -*- coding: utf-8 -*-
import codecs
import json
import sqlite3
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


class DoubanBookPipeline(object):
    def __init__(self):
        self.file = codecs.open('a.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self,spider):
        self.file.close()

class DoubanBookDBPipeline(object):
    def __init__(self):
        self.conn = sqlite3.connect('C:\\Users\\ASUS\\Desktop\\bingo\\DoubanBook')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        item = (item['book_title'].decode('utf-8'),item['book_author'].decode('utf-8'),item['book_score'].decode('utf-8'))
        self.cur.execute("insert into DoubanBook values (?,?,?)",item)
        self.conn.commit()
    def spider_closed(self,spider):
        self.conn.close()
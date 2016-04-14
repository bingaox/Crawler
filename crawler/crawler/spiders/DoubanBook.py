# -*- coding: utf-8 -*-
import scrapy
from crawler.items import Next_Url
from crawler.items import DoubanBookItem
class DoubanbookSpider(scrapy.Spider):
    name = "DoubanBook"

    url = 'https://www.douban.com/tag/%E7%BC%96%E7%A8%8B/book'
    allowed_domains = ["douban.com"]
    start_urls = (
        'https://book.douban.com/tag/?view=cloud',
    )
    def parse(self, response):
        try:
            print 'adafsdfasgasgafsgasfgasgag'
            all_target_url = response.xpath('//*[@id="content"]/div/div[1]/div[2]/div//@href').extract()
            print all_target_url
            for url in all_target_url:
                a =  url.replace('?focus=','')
                yield scrapy.Request(a,self.parse_target)
        except:
            pass
    def parse_target(self, response):

        try:
            print '...................'
            next_url =  self.url + response.selector.xpath("//*[@id='content']/div/div[1]/div[2]/span[4]/a/@href").extract()[0]
            yield scrapy.Request(next_url,self.parse)
        except:
            pass

        try:

            all_target_url = response.xpath("///dd/a//@href").extract()
            for url in all_target_url:
                print url
                yield scrapy.Request(url, self.parse_info)
        except:
            pass


    def parse_info(self,response):
        item = DoubanBookItem()
        try:
            item['book_title'] = response.xpath('//*[@id="wrapper"]/h1/span/text()').extract()[0].encode('utf-8')

        except:
            item['book_title'] = '无此信息'.encode('utf-8')

        try:
            a = ''
            for i in response.xpath('//*[@id="info"]/span[1]//text()').extract():
                a = a+i
            item['book_author'] = a.encode('utf-8').encode('utf-8')
        except:
            item['book_author'] = '无此信息'.encode('utf-8')
        try:
            item['book_score'] = response.xpath('//*[@id="interest_sectl"]/div/div[2]/strong//text()').extract()[0].encode('utf-8')
        except:
            pass

        yield item





# -*- coding: utf-8 -*-
import scrapy
from crawler.items import DomzItem

class DomzSpider(scrapy.Spider):
    name = "Domz"
    allowed_domains = ["dmoz.org"]
    start_urls = (
        'http://www.dmoz.org/Computers/Programming/Languages/Python/Books/',
        'http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/',
    )

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        for sel in response.xpath('//ul/li'):
            item = DomzItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item

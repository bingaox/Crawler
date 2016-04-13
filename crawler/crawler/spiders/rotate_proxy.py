#-*-coding:utf-8-*-
import random
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware
from scrapy import log
class RotateProxyMiddleware(HttpProxyMiddleware):
    def process_request(self, request, spider):
        proxy = random.choice(self.proxy_list)
        if proxy:
            request.meta['proxy'] = proxy
            log.msg('Current proxy:'+proxy, level='INFO')
            print("*************************************已使用代理设置*********************************")

    proxy_list = [
        "http://219.243.15.99:3128",
        "http://183.203.208.167:8118",
        "http://183.203.208.179:8118",
    ]
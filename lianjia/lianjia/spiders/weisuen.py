# -*- coding: utf-8 -*-
import scrapy
from traceback import format_exc
import pymysql
from lxml import etree
import re
from ..util.parse import housedetail, \
        urllastparse, \
        urlhousparse
from pyquery import PyQuery
from scrapy.http import Request
from ..items import LianjiaItem
import datetime

class WeisuenSpider(scrapy.Spider):
    name = 'weisuen'
    allowed_domains = ['lianjia.com']
    host = 'gz.lianjia.com'
    #start_urls = ['http://gz.lianjia.com/']
    xzarea_url_format ='https://gz.lianjia.com/{}'
    xzarea_code= list('yuexiu','liwan','panyu','baiyun','huangpugz','conghua','zengcheng','huadou','nansha')
    xzarea_code.append('tianhe')


    def start_requests(self):
        start_urls = ['https://gz.lianjia.com/ershoufang/{}/'.format(code) for code in self.xzarea_code]

        for url in start_urls:
            print(url)
            yield Request(url)
        pass


    def parse(self, response):
     #   jpy = PyQuery(response.text)
     #   li_list = jpy('body > div.content > div.leftContent > div.resultDes.clear > h2').items()
     #   if not li_list:
     #       return
        for pn in range (101,105):
            print("url",response.url+'pg{}'.format(pn))
            url = response.url+'pg{}'.format(pn)
            yield Request(url, callback=self.urlparse,
                          errback=self.err_back
                          )


    def urlparse(self, response):
        isgo = urllastparse(response)
        if isgo == "no":
            return
        url_list = urlhousparse(response)
        for url in url_list:
            yield Request(url, callback=self.house_detail_page,
                          errback=self.err_back
                          )


    def house_detail_page(self,response):
        data = housedetail(response)
        item = LianjiaItem()
        item.update(data)
        item['id'] = response.url.split('/')[4].replace('html', '')

        yield item

    def ershoufang_house_page(self):
        _ = self

        pass

    def err_back(self, e):
        _ = e
        self.logger.error(format_exc())  # 打出报错信息


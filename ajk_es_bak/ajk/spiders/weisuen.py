# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from traceback import format_exc
from ..items import AjkItem
from ..util.parse import housedetail, \
        urllastparse, \
        urlhousparse

import re


class WeisuenSpider(scrapy.Spider):
    name = 'weisuen'
    allowed_domains = ['anjuke.com']
    #start_urls = ['http://anjuke.com/']
    xzarea_codelist = ('zh','gz')
    xzarea_code = list(xzarea_codelist)

    def start_requests(self):
        start_urls = ['https://{}.anjuke.com/sale/'.format(code) for code in self.xzarea_code]

        for url in start_urls:
            print(url)
            yield Request(url)
        pass

    '城市遍历楼盘列表地址'
    def parse(self, response):
        for pn in range(1, 30):
            print("url", response.url + 'p{}/'.format(pn))
            url = response.url + 'p{}/'.format(pn)
            yield Request(url, callback=self.urlparse,
                          errback=self.err_back
                          )
        pass

    def urlparse(self, response):
        url_list = urlhousparse(response)
        for url in url_list:
            print('url',url)
            urllen=len(url)
            houseid=re.findall(r'\d+', url)
            print(str(houseid[0]))
            urllen1= urllen-(len(str(houseid))+1)
            url = url[:urllen1]
            url = url+'canshu-'+str(houseid[0])+'.html'
            print('lasturl',url)
            yield Request(url, callback=self.house_detail_page,
                          errback=self.err_back
                          )

    '楼盘具体信息查询'
    def house_detail_page(self,response):
        data = housedetail(response)
        item = AjkItem()
        item.update(data)
        #item['id'] = response.url.split('/')[4].replace('html', '')
        #print('projname',item['projname'])
        yield item
        pass



    def err_back(self, e):
        _ = e
        self.logger.error(format_exc())  # 打出报错信息
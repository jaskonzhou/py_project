# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery
from ..items import FsjwItem
from ..items import projareaItem
from scrapy.http import Request
import re

class WeifsSpider(scrapy.Spider):
    name = 'weifs'
    allowed_domains = ['fsjw.gov.cn']
    start_urls = ['http://fsfc.fsjw.gov.cn/search/index.do?ys=0&od=-SORT;-STIME;-LASTMODIFYTIME;RELEVANCE']


    def parse(self, response):
        item = FsjwItem()
        jpy = PyQuery(response.text)
        li_list = jpy('#content > div.new-house > div.col-2-1 > dl ').items()
        print(response.url)
        for it in li_list:
            strproj = it(' dd > h3 > a')

            item ["projname"] = strproj.text()
            print(item ["projname"])
            strprice = it('dd > h3 > strong > em')


            item["avgprice"] = float(strprice.text().replace("￥","").replace("价格待定","0.00"))
         #   print(item["avgprice"])
            item['projid'] = strproj.attr('value')
            strunqynum=it('dd > p:nth-child(5) > em:nth-child(2)').text()
            if len(strunqynum) == 0:
                strunqynum = 0
            item['unqynum'] = strunqynum
            strqynum = it('dd > p:nth-child(5) > em:nth-child(1)').text()
            if len(strqynum) == 0:
                strqynum = 0
            item['qynum'] = strqynum
            strcompany =it(' dd > p:nth-child(3)')
            item['company'] = strcompany.text()
            projurl="http://fsfc.fsjw.gov.cn/hpms_project/roomView.jhtml?id="+item['projid']
            if item['projid']:  # 判断url是否为空
                yield Request(projurl,
                              callback=self.detail_parse,
                              #meta={'item': projurl},  # 使用meta参数，把item传给detail_parse()
                              #priority=10,  # 优先级设为10
                              #dont_filter=True  # 强制不过滤)
                              )
            yield item

            for i in range(1, 274):
                urls ='http://fsfc.fsjw.gov.cn/search/index.do?ys=0&od=-SORT;-STIME;-LASTMODIFYTIME;RELEVANCE'+'&p='+str(i)

                yield Request(urls,
                              callback=self.parse,
                              dont_filter=False  # 强制不过滤)
                              )



        pass

    def detail_parse(self, response):
     #   print("url", response.url)
        item = projareaItem()
        item['projid'] = re.findall(r'\d+',response.url)
        jpy = PyQuery(response.text)
        adminarea = jpy('#content > div.lp-list-con > div.dis-in-b.float-left.width-860 > div.wzjs-box > table  > tr:nth-child(3) > td:nth-child(2) ').text()
     #   print("adminarea", adminarea)
        item['xzarea'] = adminarea
        yield item
        # li_list = jpy('#content > div.lp-list-con > div.dis-in-b.float-left.width-860 > div.wzjs-box>table > tbody >tr ').items()
        # for it in li_list:
        #     adminarea = it('  td > label')
        #     print("adminarea",adminarea)
        #     yield item
     #   print(response.text)
      #  item = response.meta['item']  # 接收item
     #   adminarea= jpy('#content > div.lp-list-con > div.dis-in-b.float-left.width-860 > div.wzjs-box > table > tbody > tr:nth-child(4) > td:nth-child(2)> label').text()
            #   adminarea = jpy('#content > div.lp-list-con > div.dis-in-b.float-left.width-860 > div.wzjs-box > table > tbody > tr:nth-child(1) > td > strong > span').text()

    #   print("行政区域",adminarea)



    def err_callback(self,e):
        _=self
        print("callbackERR:",e)

# -*- coding: utf-8 -*-
import scrapy
from housegz.items import HousegzItem
from lxml import etree


class WeisuenSpider(scrapy.Spider):
    name = 'weisuen1'
    allowed_domains = ['housing.gzcc.gov.cn']
    start_urls = ['http://housing.gzcc.gov.cn/search/project/project_detail.jsp?changeproInfoTag=1&changeSellFormtag=1&pjID=100000019095&name=fdcxmxx']
 #   start_urls = ['http://slide.news.sina.com.cn/s/slide_1_2841_103185.html']
    def parse(self, response):
        """解析大学详情页面的信息"""
        item = HousegzItem()
        # 先获取一个父节点，以减少重复代码


        a = response.xpath("//div[@id='con_one_1']")
        b = b=a.xpath("/html/head/title/text()").extract()
        item["title"] = b
        # 获取标题·
     #   item["title"] = response.xpath("//html/head/title/text()")
     #   title = wiki_content.xpath("/html/head/title/text()").extract()
        item["urlname"] = response.xpath("/html/head/title/text()").extract()
      #  print(item["title"])
     #   print(item["urlname"])
#c=a.xpath("/html/*/title")

        divs = a.xpath("//div[@class='tab_style01_td']/text()")

        contents = etree.XML(divs)

        for content in contents:
            print(content.text)

        '''''
        for div in divs:

            item['urlname'] = div.xpath('/td[1]/text()').extract()[0]
        #    item['var2'] = div.xpath('table/tbody/tr[*]/td[3]/p/span[2]/text()').extract()[0]
        #    item['var3'] = div.xpath('table/tbody/tr[*]/td[4]/p/text()').extract()[0]
            print('1')
            print(item["urlname"])
            return item
        
        # 获取左边的列
        keys = wiki_content.xpath('./div[@class="infobox"]/table//tr/td[1]/p/text()')
        # 获取右边的每一个单元格
        cols = dom.xpath('//*[@id="wikiContent"]/div[@class="infobox"]/table//tr/td[2]')
        # 因为有的单元格中存在多行，所以用逗号连接起来
        values = [','.join(col.xpath('.//text()')) for col in cols]
        # 用title作为key，存储成字典
        info = {title: dict(zip(keys, values))}
        print(info)
        '''
        pass

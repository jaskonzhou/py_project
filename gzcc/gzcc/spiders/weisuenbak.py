# -*- coding: utf-8 -*-
import scrapy
from gzcc.items import GzccItem

class WeisuenSpider(scrapy.Spider):
    name = 'weisuen'
    allowed_domains = ['gzcc']
   # COOKIES_ENABLED = False
    ROBOTSTXT_OBEY = False
    start_urls = ['http://housing.gzcc.gov.cn/search/project/project_detail.jsp?changeproInfoTag=1&changeSellFormtag=1&pjID=100000019095&name=fdcxmxx']
    '''
    class AutopjtPipeline(object):
        def __init__(self):
            # 打开mydata.json文件
            self.file = codecs.open("E:/scrapy/gzcc/gzcc/mydata.json", "wb", encoding="utf-8")

        def process_item(self, item, spider):
            i = json.dumps(dict(item), ensure_ascii=False)
            # 每条数据后加上换行
            line = i + '\n'
            # 写入数据到mydata.json文件中
            self.file.write(line)
            return item

        def close_spider(self, spider):
            # 关闭mydata.json文件
            self.file.close()
    '''

    def clean(s):
        """去除字符串两边的空格"""
        return s.strip() if s else ''

    def parse(self, response):
        item=GzccItem()
        rows = dom.xpath("//div[@id='content']//tr[position()>1]")
        for row in rows:
            # 提取每行的文本，并用clean函数进行处理
            item["urladdr"] = map(clean, response.xpath('./td//text()'))
            for column in columns:
                print(column, end=',')
            print()
        pass
'''''
       # item["urladdr"] = response.xpath("//td[@class='tab_style01_td']/text()")
            item["urladdr"] = response.xpath("/html/body/div/table[1]/tbody/tr[3]/td[2]/text()")
        item["urlname"]=response.xpath("//html/body/hl/text()")
       # for j in range(0, len(item["urlname"])):
        print((item["urladdr"]))
        print((item["urlname"]))
        

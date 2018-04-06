# -*- coding: utf-8 -*-
import scrapy
from gzcc.items import GzccItem
import lxml.etree
from w3lib.html import remove_tags

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
    #dom = lxml.etree.HTML(filter(html))
    # 先获取一个父节点，以减少重复代码
    wiki_content = response.xpath('//div[@id="con_one_1"]')[0]

    keys = wiki_content.xpath('./div[@class="content"]/table//tr/td[1]/p/text()')
    # 获取右边的每一个单元格
    cols = dom.xpath('//*[@id="con_one_1"]/div[@class="content"]/table//tr/td[2]')
    # 因为有的单元格中存在多行，所以用逗号连接起来
    values = [','.join(col.xpath('.//text()')) for col in cols]
    # 用title作为key，存储成字典
    info = {title: dict(zip(keys, values))}
    print(info)
    pass

'''''
       # item["urladdr"] = response.xpath("//td[@class='tab_style01_td']/text()")
            item["urladdr"] = response.xpath("/html/body/div/table[1]/tbody/tr[3]/td[2]/text()")
        item["urlname"]=response.xpath("//html/body/hl/text()")
       # for j in range(0, len(item["urlname"])):
        print((item["urladdr"]))
        print((item["urlname"]))
'''''

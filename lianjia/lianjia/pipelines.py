# -*- coding: utf-8 -*-
import json
import codecs
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LianjiaPipeline(object):
    def process_item(self, item, spider):
        i = json.dumps(dict(item), ensure_ascii=False)
        line = i + '\n'
        print(line)
        self.file.write(line)
        return item
        return item

    def close_spider(self, spider):
        self.file.close()

    def __init__(self):
        self.file = codecs.open("E:/scrapy/lianjia/mydata1.json", "wb", encoding="utf-8")

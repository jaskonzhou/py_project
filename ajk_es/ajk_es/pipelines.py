# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import json
import codecs
import pymysql

class AjkEsPipeline(object):

    def process_item(self, item, spider):
        i = json.dumps(dict(item), ensure_ascii=False)
        line = i + '\n'
        print(line)
        self.file.write(line)
        return item




    def close_spider(self, spider):
        self.file.close()

    def __init__(self):
        self.file = codecs.open("E:/scrapy/ajk_es/mydata1.json", "wb", encoding="utf-8")


class AjkesPipelinejson(object):

    def process_item(self, item, spider):
        db = pymysql.connect("39.108.212.34", "root", "123456,a", "housegz", charset="utf8")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 插入数据库
        sql1 = "insert into s_aj_esales(projname,price,area,position,url) "
        sql1 = sql1 + " VALUES (%s,%s,%s,%s,%s)"
        print("sql1", sql1)
        cursor.execute(sql1,
                       [item['projname'], item['price'], item['area'], item['position'],
                         item['url']])

        # 提交
        db.commit()
        cursor.close()
        db.close()
        return item


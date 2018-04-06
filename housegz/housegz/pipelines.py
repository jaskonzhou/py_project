# -*- coding: utf-8 -*-
import json
import codecs
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HousegzPipeline(object):
    def process_item(self, item, spider):

        db = pymysql.connect("39.108.212.34", "root", "123456,a", "housegz", charset="utf8")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 插入数据库
        sql1 = "insert into s_d_trade(projid,sysnum,sysarea,srgnum,swsnum,srgarea,swsarea,stoday_zrgnum, stoday_zrgarea,"
        sql1 = sql1 + "stoday_tfz,rgdate,stoday_shoprgnum,stoday_sharea,stoday_tfsh,projname,company,houseprice,shprice,adminarea,presaleno) "
        sql1 = sql1 + " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        print ("sql1",sql1)
        cursor.execute(sql1,
                       [item['projid'], item['sysnum'], item['sysarea'], item['srgnum'], item['swsnum'], item['srgarea'],
                        item['swsarea'], item['stoday_zrgnum'],item["stoday_zrgarea"], item['stoday_tfz'],
                        item["rgdate"], item['stoday_shoprgnum'],item["stoday_sharea"], item['stoday_shtfsh'],item['projname'],item['company'],
                        item['houseprice'],item['shprice'],item['adminarea'],item['presaleno']])

        # 提交
        db.commit()
        cursor.close()
        db.close()
    #    print(item)
        return item
    '''''    
        i = json.dumps(dict(item),ensure_ascii=False)
        line = i + '\n'
        print(line)
        self.file.write(line)
        return item
    '''
    def close_spider(self,spider):
        self.file.close()

    def __init__(self):
        self.file = codecs.open("E:/scrapy/housegz/mydata1.json", "wb", encoding="utf-8")

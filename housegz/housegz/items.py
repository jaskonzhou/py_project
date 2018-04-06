# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HousegzItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    projid = scrapy.Field()
    projname = scrapy.Field()
    company = scrapy.Field()
    sysnum = scrapy.Field()
    sysarea = scrapy.Field()
    srgnum = scrapy.Field()
    swsnum = scrapy.Field()
    srgarea = scrapy.Field()

    swsarea = scrapy.Field()
    stoday_zrgnum = scrapy.Field()
    stoday_zrgarea = scrapy.Field()

    stoday_tfz = scrapy.Field()
    rgdate = scrapy.Field()
    stoday_shoprgnum = scrapy.Field()
    stoday_sharea = scrapy.Field()
    stoday_shtfsh = scrapy.Field()
    houseprice = scrapy.Field()
    shprice = scrapy.Field()
    adminarea = scrapy.Field()
    presaleno = scrapy.Field()

    pass

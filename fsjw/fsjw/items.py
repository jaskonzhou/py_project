# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FsjwItem(scrapy.Item):
    # define the fields for your item here like:
    company = scrapy.Field()
    projname = scrapy.Field()
    avgprice = scrapy.Field()
    projid = scrapy.Field()
    adminarea = scrapy.Field()
    qynum = scrapy.Field()
    unqynum = scrapy.Field()
    xzarea = scrapy.Field()
    pass

class projareaItem(scrapy.Item):
    # define the fields for your item here like:

    projid = scrapy.Field()

    xzarea = scrapy.Field()
    pass

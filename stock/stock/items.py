# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class StockItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    xuhao = scrapy.Field()
    jysj= scrapy.Field()
    rz_ye= scrapy.Field()
    rz_mre= scrapy.Field()
    rz_che= scrapy.Field()
    rz_rzjmr= scrapy.Field()
    rq_ye= scrapy.Field()
    rq_mre= scrapy.Field()
    rq_che= scrapy.Field()
    rq_rzjmr= scrapy.Field()
    rzrqye= scrapy.Field()

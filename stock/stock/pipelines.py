# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class StockPipeline(object):
    def __init__(self):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root',
                      password='fanyubin', db='stock', charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = "insert into gupiao values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                            item['xuhao'], item['jysj'], item['rz_ye'], item['rz_mre'], item['rz_che'], item['rz_rzjmr'], item['rq_ye'],
                            item['rq_mre'], item['rq_che'], item['rq_rzjmr'], item['rzrqye'])
        self.cursor.execute(sql)

        return item

    def close_spider(self, spider):
        self.cursor.execute('commit')
        self.cursor.close()
        self.conn.close()

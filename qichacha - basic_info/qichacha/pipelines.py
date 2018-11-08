# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class QichachaPipeline(object):
    def open_spider(self,spider):
        # 链接数据库，把数据写入本地mysql数据库
        self.conn = pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='123456',db='qichacha',charset='utf8')
        # 获取游标
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        #sql语句
        sql = "INSERT INTO wen(“此处为要插入mysql数据库的对应字段”) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (“此处为插入字段对应的值”)

        try:
            self.cursor.execute(sql)
            # 提交
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

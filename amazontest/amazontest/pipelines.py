# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class AmazontestPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()
    def create_connection(self):
        self.conn=sqlite3.connect('amazon.db')
        self.curr=self.conn.cursor()
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS amazon_tb""")
        self.curr.execute("""create table amazon_tb(
                        product_name text,
                        product_author text,
                        product_price text
                        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item
    def store_db(self,item):
        self.curr.execute("""insert into amazon_tb values(?,?,?)""",(
            item['product_name'][0],
            item['product_author'][0],
            item['product_price'][0],
            item['product_imglink'][0]
        ))
        self.conn.commit()
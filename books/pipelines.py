# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
import sqlite3


class SQLitePipeline:
    def open_spider(self, spider):
        self.connection = sqlite3.connect("books.db")
        self.c = self.connection.cursor()
        self.c.execute('''
            CREATE TABLE all_books(
                name TEXT,
                price TEXT,
                available TEXT
            )''')

        self.connection.commit()


    def close_spider(self, spider):
        self.connection.close()


    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO all_books (name, price, available) VALUES(?, ?, ?)
            ''', (
                item.get('name'),
                item.get('price'),
                item.get('availability')
            ))
        self.connection.commit()
        return item

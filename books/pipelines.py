# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging


class BooksPipeline:
    def open_spider(self, spider):
        logging.warning("SPIDER OPENDED FROM PIPELINE")


    def close_spider(self, spider):
        logging.warning("SPIDER CLOSED FROM PIPELINE")


    def process_item(self, item, spider):
        return item

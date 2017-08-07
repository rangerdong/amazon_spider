# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from amazon_spider.items import ReviewDetailItem
from amazon_spider.sql import ReviewDetail


class AmazonSpiderPipeline(object):
    def __init__(self):
        self.sql = ReviewDetail()

    def process_item(self, item, spider):
        if isinstance(item, ReviewDetailItem):
            item['star'] = item['star'].split('out of 5 stars')[0].strip()
            item['date'] = item['date'].split('on')[1].strip()
            self.sql.insert_detail_item(item)
            print('save reivew:', item)
        #     pass
        pass

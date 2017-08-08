# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from amazon_scrapy.sql import ReviewSql
from amazon_scrapy.items import ReviewDetailItem
from amazon_scrapy.items import ReviewProfileItem


class AmazonScrapyPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item, ReviewProfileItem):
            a = ReviewSql()
            a.insert_profile_item(item)
            print('save review profile--[asin]:', item['asin'], '[title]:', item['title'])
            pass
        if isinstance(item, ReviewDetailItem):
            a = ReviewSql()
            a.insert_detail_item(item)
            print('save review detail--[asin]:', item['asin'], '[reviewID]:', item['review_id'])
            pass
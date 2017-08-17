from datetime import datetime

import scrapy

from pydispatch import dispatcher
from scrapy import signals

from amazon_spider.helper import Helper
from amazon_spider.items import SalesRankingItem


class SalesRankingSpider(scrapy.Spider):
    name = 'sales_ranking'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.asins = []
        dispatcher.connect(self.load_asin, signals.engine_started)

    def start_requests(self):
        for asin in self.asins:
            yield scrapy.Request('https://www.amazon.com/dp/%s' % asin, self.parse, meta={'asin':asin})

    def parse(self, response):
        print()
        product_detail = response.xpath('//div/table').re(r'#\d* in .* \(.*See Top.*\)')
        if len(product_detail) != 0:
            item = SalesRankingItem()
            key_rank_str = product_detail[0]
            key_rank_tuple = Helper.get_rank_classify(key_rank_str)
            # print(key_rank_tuple[0], key_rank_tuple[1])
            item['rank'] = key_rank_tuple[0]
            item['classify'] = key_rank_tuple[1]
            item['sk_id'] = 1
            yield item
        else:
            raise Exception('catch asin[%s] sales ranking error' % response.meta['asin'])

    def load_asin(self):
        self.asins = ['B00MNV8E0C']



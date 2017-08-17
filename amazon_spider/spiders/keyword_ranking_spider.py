import scrapy
from pydispatch import dispatcher
from scrapy import signals
from scrapy.exceptions import CloseSpider

from amazon_spider.items import KeywordRankingItem


class KeywordRankingSpider(scrapy.Spider):
    name = 'keyword_ranking'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.asin_key = {}
        self.found = False
        dispatcher.connect(self.init_scrapy, signals.engine_started)

    def start_requests(self):
        for asin, key in self.asin_key.items():
            yield scrapy.Request('https://www.amazon.com/s/?field-keywords=%s' % key, self.load_first_page, meta={'asin': asin})

    def parse(self, response):
        result_li = response.xpath('//li[@data-asin]')
        for result in result_li:
            data_asin = result.xpath('./@data-asin').extract()[0]
            if data_asin == response.meta['asin']:
                item = KeywordRankingItem()
                data_id = result.xpath('./@id').extract()[0]
                item_id = data_id.split('_')[1]
                item['skwd_id'] = 1
                item['rank'] = int(item_id) +1
                item['page'] = response.meta['page']
                self.found = True
                yield item
                raise CloseSpider(reason='find this item, id is' + item_id)


    def load_first_page(self, response):
        page = response.css('#bottomBar span.pagnDisabled::text').extract()[0]
        asin = response.meta['asin']
        page_num = 1
        while page_num <= int(page):
            yield scrapy.Request(response.url + '&page=%s' % page_num, self.parse, meta={'asin': asin, 'page':page_num})
            page_num += 1

        # print(self.found)
        # if self.found is not True:
        #     item = KeywordRankingItem()
        #     item['skwd_id'] = 1
        #     item['rank'] = 0
        #     item['page'] = 0
        #     yield item

    def init_scrapy(self):
        self.asin_key = {'B002TSMTL4': 'echo'}

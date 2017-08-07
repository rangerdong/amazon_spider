import scrapy
from amazon_spider.items import ReviewDetailItem
from scrapy import log


class ReviewSpider(scrapy.Spider):
    name = 'review'

    def __init__(self, asin, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.asin = asin
        self.start_urls = ['https://www.amazon.com/product-reviews/%s' % asin]

    def parse(self, response):
        reviews = response.css('.review-views .review')
        for row in reviews:
            item = ReviewDetailItem()
            item['asin'] = self.asin
            item['review_id'] = row.css('div::attr(id)')[0].extract()
            item['reviewer'] = row.css('.author::text')[0].extract()
            item['title'] = row.css('.review-title::text')[0].extract()
            item['date'] = row.css('.review-date::text')[0].extract()
            item['star'] = row.css('.review-rating span::text')[0].extract()
            item['content'] = row.css('.review-text::text')[0].extract()
            yield item


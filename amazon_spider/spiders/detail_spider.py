import math
import scrapy

from amazon_spider.items import ReviewProfileItem
from amazon_spider.items import ReviewDetailItem
from amazon_spider.helper import Helper
from amazon_spider.sql import ReviewSql


class ReviewSpider(scrapy.Spider):
    name = 'detail'

    def __init__(self, asin, daily=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.asin = asin
        self.daily = True if int(daily) == 1 else False   # 判断是否是每日更新
        self.start_urls = [
            'https://www.amazon.com/product-reviews/%s?sortBy=recent&filterByStar=three_star' % self.asin,
            'https://www.amazon.com/product-reviews/%s?sortBy=recent&filterByStar=two_star' % self.asin,
            'https://www.amazon.com/product-reviews/%s?sortBy=recent&filterByStar=one_star' % self.asin
        ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.get_detail)

    def parse(self, response):
        reviews = response.css('.review-views .review')
        for row in reviews:
            item = ReviewDetailItem()
            item['asin'] = self.asin
            item['review_id'] = row.css('div::attr(id)')[0].extract()
            item['reviewer'] = row.css('.author::text')[0].extract()
            item['title'] = row.css('.review-title::text')[0].extract()
            item['review_url'] = row.css('.review-title::attr(href)')[0].extract()
            item['date'] = Helper.get_date_split_str(row.css('.review-date::text')[0].extract())
            item['star'] = Helper.get_star_split_str(row.css('.review-rating span::text')[0].extract())
            content = row.css('.review-data .review-text::text').extract()
            item['content'] = content[0] if len(content) > 0 else ''
            yield item

    def get_detail(self, response):
        # 获取页面数
        page = response.css('ul.a-pagination li a::text')

        i = 1

        if len(page) < 3:  # 若找到的a标签总数小于3 说明没有page组件 只有1页数据
            yield scrapy.Request(url=response.url + '&pageNumber=1', callback=self.parse)
        else:
            if self.daily:
                # 获取评价总数
                total = response.css('.AverageCustomerReviews .totalReviewCount::text').extract()  # 获取评价总数
                now_total = Helper.get_num_split_comma(total[0])
                last_total = ReviewSql.get_last_review_total(self.asin)
                if last_total is not False:
                    sub_total = int(now_total) - int(last_total)
                    page_num = math.ceil(sub_total / 10)
                    print('there is no item to update' if page_num == 0 else 'update item page_num is %s' % page_num)
                else:
                    page_num = Helper.get_num_split_comma(page[len(page) - 3].extract())  # 获得总页数
            else:
                page_num = Helper.get_num_split_comma(page[len(page) - 3].extract())  # 获得总页数
            while i <= int(page_num):
                yield scrapy.Request(url=response.url + '&pageNumber=%s' % i,
                                     callback=self.parse)
                i = i+1

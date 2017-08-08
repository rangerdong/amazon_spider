import scrapy

from amazon_scrapy.items import ReviewProfileItem

from amazon_scrapy.items import ReviewDetailItem
from amazon_scrapy.helper import Helper


class ReviewSpider(scrapy.Spider):
    name = 'review'

    def __init__(self, asin, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.asin = asin
        self.start_urls = ['https://www.amazon.com/product-reviews/%s' % asin]

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], callback=self.get_profile)

    def parse(self, response):
        reviews = response.css('.review-views .review')
        for row in reviews:
            item = ReviewDetailItem()
            item['asin'] = self.asin
            item['review_id'] = row.css('div::attr(id)')[0].extract()
            item['reviewer'] = row.css('.author::text')[0].extract()
            item['title'] = row.css('.review-title::text')[0].extract()
            item['date'] = Helper.get_date_split_str(row.css('.review-date::text')[0].extract())
            item['star'] = Helper.get_star_split_str(row.css('.review-rating span::text')[0].extract())
            item['content'] = row.css('.review-data .review-text::text')[0].extract()
            yield item

    def get_profile(self, response):
        item = ReviewProfileItem()

        # 获取平均评价数值
        average = response.css('.averageStarRatingNumerical a span::text').extract()  # 获取平均评价值
        item['review_rate'] = Helper.get_star_split_str(average[0])   # 获取平均值
        # 获取评价总数
        total = response.css('.AverageCustomerReviews .totalReviewCount::text').extract()   # 获取评价总数
        # review_total = total[0].split(',')
        # if len(review_total) > 1:
        #     item['review_total'] = review_total[0] + review_total[1]
        # else:
        #     item['review_total'] = review_total

        item['review_total'] = Helper.get_num_split_comma(total[0])
        # 获取产品名称
        product = response.css('.product-title h1 a::text').extract()
        item['product'] = product[0]
        # 获取产品 brand
        item['brand'] = response.css('.product-by-line a::text').extract()[0]
        item['seller'] = item['brand']
        # 获取各星评价数
        review_summary = response.css('.reviewNumericalSummary .histogram '
                                      '#histogramTable .histogram-review-count::text').extract()
        pct = list(map(lambda x: x[0:-1], review_summary))

        item['pct_five'] = pct[0]
        item['pct_four'] = pct[1]
        item['pct_three'] = pct[2]
        item['pct_two'] = pct[3]
        item['pct_one'] = pct[4]
        item['asin'] = self.asin

        page = response.css('ul.a-pagination li a::text')
        # last_page = page[len(page)-3].extract()
        page_num = Helper.get_num_split_comma(page[len(page)-3].extract())    # 获得总页数
        # item['asin'] = page_num
        yield item
        i = 1
        while i <= int(page_num):
            yield scrapy.Request(url=self.start_urls[0]+'?pageNumber=%s' % i, callback=self.parse)
            i = i+1

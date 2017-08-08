import pymysql
from amazon_scrapy import settings


class ReviewSql:

    def __init__(self):
        db_conf = settings.MYSQL
        db_conf['cursorclass'] = pymysql.cursors.DictCursor
        self.conn = pymysql.connect(**db_conf)
        self.conn.autocommit(1)
        self.cursor = self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        self.cursor.close()

    def insert_profile_item(self, item):
        sql = "INSERT INTO `review_profile`(`asin`, `product`, `brand`, `seller`, `review_total`, `review_rate`, `pct_five`, `pct_four`, `pct_three`, `pct_two`, `pct_one`) " \
              "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %\
              (item['asin'], item['product'], item['brand'], item['seller'], item['review_total'], item['review_rate'],
               item['pct_five'], item['pct_four'], item['pct_three'], item['pct_two'], item['pct_one'])
        try:
            if self.check_exist_profile(item['asin']):
                pass
            else:
                self.cursor.execute(sql)
                self.conn.commit()
        except:
            self.conn.rollback()
        pass

    def check_exist_profile(self, asin):
        sql = "SELECT * FROM `review_profile` WHERE (`asin` = '%s')" % (asin)
        try:
            result = self.cursor.execute(sql)
            self.conn.commit()
            if result:
                return True
            else:
                return False
        except:
            self.conn.rollback()
        pass

    def insert_detail_item(self, item):
        sql = "INSERT INTO `review_detail`(`asin`, `review_id`, `reviewer`, `star`, `date`, `title`, `content`) " \
              "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
              (item['asin'], item['review_id'], item['reviewer'], item['star'], item['date'], item['title'], item['content'])
        try:
            if self.check_exist_detail(item['asin'], item['review_id']):
                pass
            else:
                self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
        pass

    def check_exist_detail(self, asin, review_id):
        sql = "SELECT * FROM `review_detail` WHERE `asin` = '%s' AND `review_id`='%s'" % (asin, review_id)
        try:
            result = self.cursor.execute(sql)
            self.conn.commit()
            if result:
                return True
            else:
                return False
        except:
            self.rollback()
        pass





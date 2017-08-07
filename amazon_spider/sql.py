import pymysql
from amazon_spider import settings


class ReviewDetail:

    def __init__(self):
        conf = settings.MYSQL
        conf['cursorclass'] = pymysql.cursors.DictCursor
        self.conn = pymysql.connect(**conf)
        self.cursor = self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        self.cursor.close()

    def insert_detail_item(self, item):
        sql = "INSERT INTO `review_detail`(`asin`, `review_id`, `reviewer`, `star`, " \
              "`date`, `title`, `content`)" \
              "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
              (item['asin'], item['review_id'], item['reviewer'], item['star'],
               item['date'], item['title'], item['content'])
        try:
            # if self.check_exist_detail(item['asin'], item['review_id']):
            #     pass
            # else:
                self.cursor.execute(sql)
                self.conn.commit()
        except:
            self.conn.rollback()

    def check_exist_detail(self, asin, review_id):
        sql = "SELECT * FROM `review_detail` WHERE `asin`='%s' AND `review_id`='%s'" % (asin, review_id)
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        if result:
            return True
        else:
            return False

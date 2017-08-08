import datetime


class Helper(object):

    @classmethod
    def get_num_split_comma(cls, value):
        num = value.split(',')
        if len(num) > 1:
            return num[0] + num[1]
        else:
            return value

    @classmethod
    def get_star_split_str(cls, value):
        rate = value.split('out of 5 stars')   # 分割字符串
        return rate[0].strip()

    @classmethod
    def get_date_split_str(cls, value):
        return value.split('on')[1].strip()

    @classmethod
    def convert_date_str(cls, date_str):
        return datetime.datetime.strptime(date_str, '%B %d, %Y')

    @classmethod
    def delay_forty_days(cls):
        now = datetime.datetime.now()
        delay14 = now + datetime.timedelta(days=-40)  # 计算往前40天之后的时间
        return delay14

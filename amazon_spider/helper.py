
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

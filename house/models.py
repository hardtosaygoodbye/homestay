from django.db.models import *
from user.models import User

class House(Model):
    desc = CharField('房屋名称', max_length = 15)
    cover = URLField('封面', max_length = 100)
    city = CharField('所在城市', max_length = 10)
    address = CharField('地址', max_length = 100)
    price = DecimalField('价格', max_digits = 10, decimal_places = 2)
    area = CharField('面积', max_length = 10)
    facility = CharField('设施', max_length = 100)
    phone = CharField('联系电话', max_length = 11)
    comment_num = IntegerField('评价人数', default = 0)
    comment_score = DecimalField('评分', max_digits = 5, decimal_places = 1)
    statuses = (
        (0, '空闲'),
    )
    status = IntegerField('订单状态', choices = statuses, default = 0)
    def __str__(self):
        return self.title



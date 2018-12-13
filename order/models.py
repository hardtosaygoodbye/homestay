from django.db.models import *

class Order(Model):
    statuses = (
        (0, '待付款'),
        (1, '已完成'),
        (2, '已取消'),
    )
    status = IntegerField('订单状态', choices = statuses, default = 0)
    create_time = DateTimeField(auto_now_add = True)
    price = DecimalField('订单价格', max_digits = 10, decimal_places = 2)
    name = CharField(max_length = 10, blank = True)
    phone = CharField(max_length = 11)
    id_card = CharField(max_length = 18)
    person_num = CharField(max_length = 5)
    check_in_date = DateField(null = True, blank = True)
    check_out_date = DateField(null = True, blank = True)
    

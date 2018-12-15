from django.db.models import *
from uuid import uuid4

class User(Model):
    phone = CharField('手机号', max_length = 11)
    password = CharField('密码', max_length = 15)
    def __str__(self):
        return self.phone

class Authority(Model):
    user = OneToOneField(User, on_delete = CASCADE, primary_key = True)
    token = UUIDField(default = uuid4)

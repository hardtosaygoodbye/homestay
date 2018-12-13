from django.db.models import *
from uuid import uuid4

class User(Model):
    phone = CharField('手机号', max_length = 11)
    def __str__(self):
        return self.phone

class SMS(Model):
    phone = CharField(max_length = 11, primary_key = True)
    code = CharField(max_length = 6)
    def __str__(self):
        return self.phone + ' - ' + self.code

class Authority(Model):
    user = OneToOneField(User, on_delete = CASCADE, primary_key = True)
    token = UUIDField(default = uuid4)

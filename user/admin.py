from django.contrib import admin
from .models import *

admin.site.site_header = '悦租房'
admin.site.site_title = '悦租房后台'

admin.site.register(User)
admin.site.register(Authority)

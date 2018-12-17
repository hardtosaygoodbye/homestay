from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^order/$', OrderView.as_view()),
    url(r'^discuss_order/$', DiscussOrderView.as_view()),
    url(r'^pay_order/$', PayOrderView.as_view()),
]

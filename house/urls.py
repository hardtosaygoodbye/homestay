from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^house_list/$', HouseListView.as_view()),
    url(r'^house_detail/$', HouseDetailView.as_view()),
]

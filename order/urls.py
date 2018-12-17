from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^order/$', OrderView.as_view()),
]

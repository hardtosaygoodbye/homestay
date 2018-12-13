from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^sms/$', SMSView.as_view()),
    url(r'^login/$', LoginView.as_view()),
    url(r'^current_user/$', CurrentUserView.as_view()),
]

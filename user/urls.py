from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^sign_up/$', SignUpView.as_view()),
    url(r'^sign_in/$', SignInView.as_view()),
    url(r'^current_user/$', CurrentUserView.as_view()),
]

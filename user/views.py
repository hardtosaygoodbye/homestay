from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from random import randint
from django.http import Http404
from .serializers import *

def token2user(token):
    try:
        authority = Authority.objects.get(token = token)
    except:
        raise Http404
    return authority.user
    
class SMSView(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        if not phone:
            return Response({'detail':'phone required'}, 404)
        if len(phone) != 11:
            return Response({'detail':'手机号格式错误'}, 400)
        code = str(randint(100000, 999999))
        sms = SMS(phone = phone, code = code)
        sms.save()
        return Response({'code':0, 'detail':'验证码发送成功'})

class LoginView(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        code = request.data.get('code')
        if not (phone and code):
            return Response({'detail':'phone,code required'}, 400)
        if len(phone) != 11:
            return Response({'detail':'手机号格式错误'}, 400)
        if len(code) != 6:
            return Response({'detail':'验证码格式错误'}, 400)
        try:
            sms = SMS.objects.get(phone = phone, code = code)
        except:
            return Response({'detail': '验证码错误'}, 400)
        users = User.objects.filter(phone = phone)
        if len(users) == 0:
            # 注册
            user = User(phone = phone)
            user.save()
            authority = Authority(user = user)
            authority.save()
            userSerializer = UserSerializer(user)
            return Response({'code':0, 'user':userSerializer.data, 'token':\
            authority.token})
        elif len(uses) == 1:
            # 登录
            user = users[0]
            authority = Authority(user = user)
            authority.save()
            userSerializer = UserSerializer(user)
            return Response({'code':0, 'user':userSerializer.data,\
            'token':authority.token})
        else:
            return Response({'detail':'异常'}, 400)

class CurrentUserView(APIView):
    def get(self, request):
        token = request.GET.get('token')
        if not token:
            return Response({'detail':'token required'}, 404)
        user = token2user(toekn)
        userSerializer = UserSerializer(user)
        return Response({'code':0, 'user':userSerializer.data})
    def patch(self, request):
        token = request.GET.get('token')
        user = toekn2user(token)
        userSerializer = UserSerializer(user, data = request.data,\
        partial = True)
        if not userSerializer.is_valid():
            return Response(userSerializer.errors, 404)
        userSerializer.save()
        return Response({'code':0, 'user':userSer.data})


            


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
    
# 登录
class SignInView(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        password = request.data.get('password')
        if not (phone and password):
            return Response({'detail': 'phone,password required'}, 400)
        if len(phone) != 11:
            return Response({'detail': '手机号格式错误'}, 400)
        try:
            user = User.objects.get(phone = phone, password = password)
        except:
            return Response({'detail': '密码错误，或账号不存在'}, 400)
        authority = Authority(user = user)
        authority.save()
        userSerializer = UserSerializer(user)
        return Response({'code': 0, 'user': userSerializer.data,\
        'token': authority.token})

# 注册
class SignUpView(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        password = request.data.get('password')
        if not (phone and password):
            return Response({'detail': 'phone, password required'}, 400)
        if len(phone) != 11:
            return Response({'detail': '手机号格式错误'}, 400)
        users = User.objects.filter(phone = phone)
        if len(users) == 1:
            return Response({'detail': '该手机号已经有人注册'}, 400)
        user = User(phone = phone, password = password)
        user.save()
        authority = Authority(user = user)
        authority.save()
        userSerializer = UserSerializer(user)
        return Response({'code':0, 'user': userSerializer.data,\
        'token': authority.token})

# 当前用户信息
class CurrentUserView(APIView):
    def get(self, request):
        token = request.GET.get('token')
        if not token:
            return Response({'detail':'token required'}, 404)
        user = token2user(token)
        userSerializer = UserSerializer(user)
        return Response({'code':0, 'user':userSerializer.data})
    def put(self, request):
        token = request.GET.get('token')
        user = toekn2user(token)
        userSerializer = UserSerializer(user, data = request.data,\
        partial = True)
        if not userSerializer.is_valid():
            return Response(userSerializer.errors, 404)
        userSerializer.save()
        return Response({'code':0, 'user':userSer.data})


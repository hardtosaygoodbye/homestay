from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
import datetime
from house.models import *
from user.views import token2user
from house.models import *
import decimal
from .serializers import *

class OrderView(APIView):
    def get(self, request):
        token = request.GET.get('token')
        status = request.GET.get('status')
        user = token2user(token)
        orders = Order.objects.filter(status = status, user = user)
        orderSerializers = OrderSerializer(orders, many = True)
        return Response({"code":0 ,"orders": orderSerializers.data})

    def post(self, request):
        token = request.data.get('token')
        house_id = request.data.get('house_id')
        name = request.data.get('name')
        id_card = request.data.get('id_card')
        person_num = request.data.get('person_num')
        check_in_date = request.data.get('check_in_date')
        check_out_date = request.data.get('check_out_date')
        phone = request.data.get('phone')
        if not (house_id and name and id_card and person_num and check_in_date\
        and check_out_date):
            return Response({'detail':'Parameters are missing'}, 400)
        check_in_date = datetime.datetime.strptime(check_in_date, '%Y-%m-%d')
        check_out_date = datetime.datetime.strptime(check_out_date, '%Y-%m-%d')
        try:
            house = House.objects.get(pk = house_id)
        except:
            return Response({'detail':'未找到该住房'}, 400)
        user = token2user(token)
        stay_days = (check_out_date-check_in_date).days
        for i in range(stay_days):
            date = check_in_date + datetime.timedelta(days = i)
            houseOccupy = HouseOccupy(
                house = house,
                date = date,
                user = user
            )
            houseOccupy.save()
        order = Order(
            status = 0,
            price = stay_days * house.price,
            name = name,
            phone = phone,
            id_card = id_card,
            person_num = person_num,
            check_in_date = check_in_date,
            check_out_date = check_out_date,
            user = user,
            house = house
        )
        order.save()
        return Response({"code":0, "detail":"预定成功"})

class DiscussOrderView(APIView):
    def post(self, request):
        token = request.data.get('token')
        order_id = request.data.get('order_id')
        msg = request.data.get('msg')
        score = request.data.get('score')
        score = decimal.Decimal(score)
        user = token2user(token)
        try:
            order = Order.objects.get(pk = order_id)
        except:
            return Response({"detail":"该订单未找到"}, 400)
        order.save()
        house = order.house
        comment = Comment(
            msg = msg,
            score = score,
            user = user,
            house = house
        )
        comment.save()
        comment_num = house.comment_num
        comment_score = house.comment_score
        total_score = (comment_num * comment_score + score) / (comment_num + 1)
        house.comment_num += 1
        house.comment_score = total_score
        house.save()
        return Response({"code":0, "detail":"评价成功"})

class CancelOrderView(APIView):
    def post(self, request):
        token = request.data.get('token')
        order_id = request.data.get('order_id')
        try:
            order = Order.objects.get(pk = order_id)
        except:
            return Response({"detail": "该订单未找到"})
        order.status = 2
        order.save()
        return Response({"code":0, "detail":"订单取消成功"})

class PayOrderView(APIView):
    def post(self, request):
        token = request.data.get('token')
        order_id = request.data.get('order_id')
        try:
            order = Order.objects.get(pk = order_id)
        except:
            return Response({"detail": "该订单未找到"})
        order.status = 1
        order.save()
        return Response({"code":0, "detail":"订单付款完成"})
        

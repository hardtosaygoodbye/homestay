from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
import datetime
from house.models import *
from user.views import token2user

class OrderView(APIView):
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
            day = check_in_date + datetime.timedelta(days = i)
        order = Order(
            status = 0,
            price = stay_days * house.price,
            name = name,
            phone = phone,
            id_card = id_card,
            person_num = person_num,
            check_in_date = check_in_date,
            check_out_date = check_out_date,
            user = user
        )
        order.save()
        return Response({"code":0, "detail":"预定成功"})

        

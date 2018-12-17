from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from datetime import datetime
from house.models import *

class OrderView(APIView):
    def post(self, request):
        house_id = request.data.get('house_id')
        name = request.data.get('name')
        id_card = request.data.get('id_card')
        person_num = request.data.get('person_num')
        check_in_date = request.data.get('check_in_date')
        check_out_date = request.date.get('check_out_date')
        if not (house_id and name and id_card and person_num and check_in_date\
        and check_out_date):
            return Response({'detail':'Parameters are missing'}, 400)
        check_in_date = datetime.strptime(check_in_date, '%Y-%m-%d')
        check_out_date = datetime.strptime(check_out_date, '%Y-%m-%d')
        try:
            house = House.objects.get(pk = house_id)
        except:
            return Response({'detail':'未找到该住房'}, 400)
        if house.status != 0:
            return Response({'detail':'该房间已被预定'}, 400)


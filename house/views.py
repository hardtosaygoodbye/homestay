from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from datetime import datetime

class HouseListView(APIView):
    def get(self, request):
        keyword = request.GET.get('keyword')
        check_in_date = request.GET.get('check_in_date')
        check_out_date = request.GET.get('check_out_date')
        check_in_date = datetime.strptime(check_in_date, '%Y-%m-%d')
        check_out_date = datetime.strptime(check_out_date, '%Y-%m-%d')
        houses = House.objects.filter(
            Q(desc__icontains = keyword)|Q(city__icontains = keyword)
        ).exclude(
            occupy__date__range = (check_in_date,check_out_date)
        )
        houseSerializers = HouseSerializer(houses, many = True)
        return Response({'code':0, 'houses':houseSerializers.data})

class HouseDetailView(APIView):
    def get(self, request):
        house_id = request.GET.get('house_id')
        try:
            house = House.objects.get(house_id = house_id)
        except:
            return Response({'detail':'未找到相关房屋信息'})
        serializer = HouseDetailSerializer(house)
        return Response({'code':0, 'house':serializer.data})

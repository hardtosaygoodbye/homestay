from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class HouseListView(APIView):
    def get(self, request):
        keyword = request.GET.get('keyword')
        houses = House.objects.filter(
            Q(desc__icontains = keyword)|Q(city__icontains = keyword),
            status = 0
        )
        serializers = HouseSerializer(books, many = True)
        return Response({'code':0, 'houses':serializers.data})

class HouseDetailView(APIView):
    def get(self, request):
        house_id = request.GET.get('house_id')
        try:
            house = House.objects.get(house_id = house_id)
        except:
            return Response({'detail':'未找到相关房屋信息'})
        serializer = HouseDetailSerializer(house)
        return Response({'code':0, 'house':serializer.data})

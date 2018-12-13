from rest_framework.serializers import *
from .models import *

class HouseSerializer(ModelSerializer):
    class Meta:
        model = House
        fields = ['id', 'cover', 'desc', 'address', 'comment_score', 'price']

class HouseDetailSerializer(ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'

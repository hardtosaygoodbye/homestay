from rest_framework.serializers import *
from .models import *

class OrderSerializer(ModelSerializer):
    house_desc = SerializerMethodField()
    def get_house_desc(self, obj):
        return obj.house.desc
    class Meta:
        model = Order
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


from rest_framework.serializers import *
from .models import *

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


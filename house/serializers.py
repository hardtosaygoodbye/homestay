from rest_framework.serializers import *
from .models import *
from order.models import *
from order.serializers import *

class HouseSerializer(ModelSerializer):
    class Meta:
        model = House
        fields = ['id', 'cover', 'desc', 'address', 'comment_score', 'price']

class HouseDetailSerializer(ModelSerializer):
    comments = SerializerMethodField()
    def get_comments(self, obj):
        comments = Comment.objects.filter(house__id = obj.id)
        return CommentSerializer(comments, many = True).data
    class Meta:
        model = House
        fields = '__all__'

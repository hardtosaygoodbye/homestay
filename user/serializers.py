from rest_framework.serializers import *
from .models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

from rest_framework import serializers
from .models import UserInfo

#All existing models have been serialized

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = UserInfo
        fields = '__all__'
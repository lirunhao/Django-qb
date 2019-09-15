from rest_framework import serializers, viewsets
from rest_framework.serializers import HyperlinkedModelSerializer

from user.models import UserModel


# 序列化类
class UserModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'name', 'phone')


# API视图类
class UserAPIView(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

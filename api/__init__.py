from rest_framework import routers

from api.goods import GoodsAPIView
from .user import UserAPIView

# 声明api路由
api_router = routers.DefaultRouter()

# 向api路由中注册ViewSet
api_router.register('users', UserAPIView)
api_router.register('goods', GoodsAPIView)

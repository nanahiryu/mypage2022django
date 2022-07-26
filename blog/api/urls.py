# coding: utf-8

from rest_framework import routers
from .views import CategoryViewSet, DiaryViewSet


router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'diary', DiaryViewSet)

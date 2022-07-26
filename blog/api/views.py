# coding: utf-8

import django_filters
from rest_framework import viewsets, filters

from ..models import Category, Diary
from .serializer import CategorySerializer, DiarySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DiaryViewSet(viewsets.ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer

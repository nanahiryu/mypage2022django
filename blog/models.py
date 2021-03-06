from django.utils import timezone
from django.db import models
from mdeditor.fields import MDTextField

# Create your models here.


class Category(models.Model):
    name = models.CharField('タイトル', max_length=255, unique=True)

    def __str__(self):
        return self.name


class DiaryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(created_at__lte=timezone.now)


class Diary(models.Model):
    """日記"""
    title = models.CharField('タイトル', max_length=64)
    subtitle = models.CharField('サブタイトル', max_length=256, default="ないしょのはなし")
    # text = models.TextField('本文')
    text = MDTextField()
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name='カテゴリ')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    objects = DiaryQuerySet.as_manager()

    def __str__(self):
        return self.title

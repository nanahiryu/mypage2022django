from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class AboutSkills(models.Model):
    name = models.CharField('スキル名', max_length=64)
    stars = models.IntegerField(
        '星の数', validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        verbose_name = 'スキル'
        verbose_name_plural = 'スキル'

    def __str__(self):
        return self.name

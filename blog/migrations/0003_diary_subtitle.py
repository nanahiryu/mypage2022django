# Generated by Django 3.1.1 on 2022-02-24 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220224_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='subtitle',
            field=models.CharField(default='ないしょのはなし', max_length=256, verbose_name='サブタイトル'),
        ),
    ]

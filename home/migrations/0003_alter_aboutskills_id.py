# Generated by Django 4.0.6 on 2022-07-28 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220507_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutskills',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

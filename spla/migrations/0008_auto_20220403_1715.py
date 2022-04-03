# Generated by Django 3.1.1 on 2022-04-03 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spla', '0007_auto_20220330_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='main',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='weapon', to='spla.main'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='special',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='weapon', to='spla.special'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='sub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='weapon', to='spla.subweapon'),
        ),
    ]

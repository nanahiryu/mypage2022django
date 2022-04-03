from django.contrib import admin
from import_export import resources
from . import models
# Register your models here.

admin.site.register(models.SubWeapon)
admin.site.register(models.Special)
admin.site.register(models.Weapon_class)
admin.site.register(models.Weight)
admin.site.register(models.Main)
admin.site.register(models.Attack_class)
admin.site.register(models.Range)
admin.site.register(models.Weapon)

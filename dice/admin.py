from django.contrib import admin

from .models import Armor, ArmorType, Weapon, WeaponType

admin.site.register(Weapon)
admin.site.register(WeaponType)
admin.site.register(Armor)
admin.site.register(ArmorType)

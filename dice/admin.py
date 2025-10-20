from django.contrib import admin
from .models import Weapon, WeaponType, Armor, ArmorType 

admin.site.register(Weapon)
admin.site.register(WeaponType)
admin.site.register(Armor)
admin.site.register(ArmorType)


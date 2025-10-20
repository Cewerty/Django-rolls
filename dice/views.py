from django.shortcuts import render
from .models import Weapon, Armor, ArmorType, WeaponType
from django.db.models import Prefetch

def weapon_list(request):
    weapon_types = WeaponType.objects.order_by("name").prefetch_related(
        Prefetch("weapons", queryset=Weapon.objects.select_related("weapon_type").order_by("weapon_type__name", "name"))
    )
    armor_types = ArmorType.objects.order_by("name").prefetch_related(
        Prefetch("armors", queryset=Armor.objects.select_related("armor_type").order_by("armor_type__name", "name"))
    )
    return render(request, "dice/catalog.html", {'weapon_types': weapon_types,
                                                 'armor_types': armor_types,
                                                 'dice_api_url': "/api/roll",
                                                 })

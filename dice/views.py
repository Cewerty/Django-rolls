from django.shortcuts import render
from .models import Weapon

def weapon_list(request):
    weapons = Weapon.objects.all().order_by('-name')
    return render(request, "dice/catalog.html", {'weapons': weapons})

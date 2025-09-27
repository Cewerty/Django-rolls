from django.shortcuts import render, get_object_or_404
from .models import Weapon

def weapon_list(request):
    weapons = Weapon.objects.all().order_by('-name')
    return render(request, "dice/post_list.html", {'weapons': weapons})

def weapon_detail(request, pk):
    weapon = get_object_or_404(Weapon, pk=pk)
    return render(request, 'dice/post_detail.html', {'weapon': weapon})

from django.db.models import Prefetch
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Armor, ArmorType, Weapon, WeaponType


def equipment_list(request: HttpRequest) -> HttpResponse:
    """
    Display a catalog of weapons and armor organized by type.

    This view fetches all weapon types and armor types from the database,
    prefetches their related weapons and armors with optimized queries,
    and passes them to the template for rendering.

    Args:
    ----
        request: HttpRequest object containing metadata about the request.

    Returns:
    -------
        HttpResponse: Rendered HTML page with equipment catalog.

    Context:
    -------
        weapon_types: QuerySet of WeaponType objects with prefetched weapons.
        armor_types: QuerySet of ArmorType objects with prefetched armors.
        dice_api_url: String URL for the dice rolling API endpoint.

    """
    weapon_types = WeaponType.objects.order_by("name").prefetch_related(
        Prefetch("weapons", queryset=Weapon.objects.select_related("weapon_type").order_by("weapon_type__name", "name"))
    )
    armor_types = ArmorType.objects.order_by("name").prefetch_related(
        Prefetch("armors", queryset=Armor.objects.select_related("armor_type").order_by("armor_type__name", "name"))
    )
    return render(
        request,
        "dice/catalog.html",
        {
            "weapon_types": weapon_types,
            "armor_types": armor_types,
            "dice_api_url": "/api/roll",
        },
    )

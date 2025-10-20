from django.urls import path

from . import views

app_name = "dice"

urlpatterns = [
    path("", views.equipment_list, name="equipment_list"),
]

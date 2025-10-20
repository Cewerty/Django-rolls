from django.urls import path
from . import views

app_name = 'dice'

urlpatterns = [
    path('', views.weapon_list, name='weapon_list'),
    ]

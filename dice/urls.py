from django.urls import path
from . import views

app_name = 'dice'

urlpatterns = [
    path('', views.weapon_list, name='weapon_list'),
    path('dice/<int:pk>/', views.weapon_detail, name='weapon_detail'),
    ]

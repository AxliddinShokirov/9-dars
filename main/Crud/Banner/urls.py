
from django.urls import path , include
from . import views

urlpatterns = [
    path('banner_list', views.banner_lits, name='banner_list'),
    path('banner_create', views.banner_create, name='banner_create'),
    path('banner_delete/<int:pk>', views.banner_detail, name='banner_delete'),
    path('banner_detail/<int:pk>', views.banner_delete, name='banner_detail'),
    ]
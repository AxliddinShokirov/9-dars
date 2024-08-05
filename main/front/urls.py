from django.contrib import admin
from django.urls import path
from . import views
urlpatterns =[
      path('', views.front, name='front'),
      path('coach',views.coach, name='coach'),
      
 ]
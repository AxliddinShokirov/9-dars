from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('contacts/', views.contact_update, name='contact_update'),
    path('contact_delete/', views.contact_delete, name='contact_delete'),
    path('login/', include('main.login.urls')),
    ]

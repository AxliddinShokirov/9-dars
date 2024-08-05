from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.listBanner, name='listBanner'),
    path('detail/<int:id>/', views.detailBanner, name='detailBanner'),
    path('create/', views.createBanner, name='createBanner'),
    path('update/<int:id>', views.updateBanner, name='updateBanner'),
    path('delete/<int:id>', views.deleteBanner, name='deleteBanner'),
]
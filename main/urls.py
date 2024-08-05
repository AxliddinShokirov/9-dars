from django.contrib import admin
from django.urls import path , include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('deshboard/', include('main.Deshboard.urls')),
    path('', include('main.front.urls')), 
    path('login/', include('main.login.urls')),
    path('sappp/', include('main.Crud.urls')),
        ]
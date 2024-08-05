 
from django.urls import path , include

urlpatterns =[

    path('categ/', include('main.Crud.category.urls') )

]
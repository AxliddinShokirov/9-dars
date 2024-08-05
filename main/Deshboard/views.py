from django.shortcuts import render

from main import models

def index(request):
    banner=models.Banner.objects.all()
    products=models.Product.objects.all()
    catgory=models.Category.objects.all()
    contact=models.Contact.objects.last()
    info=models.Info.objects.all()
    gym=models.Gym.objects.all()
    coach=models.Coach.objects.all()
    contex={'banner':banner, 'products':products, 'catgory':catgory, 'contact':contact, 'info':info}
    
    return render(request, 'deshboard/index.html',contex)
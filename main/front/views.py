from django.shortcuts import render,redirect
from main import models

def front(request):
    banner=models.Banner.objects.all()
    products=models.Product.objects.all()
    catgory=models.Category.objects.all()
    contact=models.Contact.objects.last()
    info=models.Info.objects.all()
    img=models.Banner.objects.last()
    gym=models.Gym.objects.all()
    gyms=models.Gym.objects.last()
   
    
    return render(request, 'front/index.html', {'banner': banner, 'products': products , 'catgory': catgory, 'contact': contact, 'info': info, 'img': img, 'gym': gym, 'gyms': gyms})






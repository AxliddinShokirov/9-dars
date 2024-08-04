from django.shortcuts import render,  redirect
from main import models 


def banner_lits(request):
    banners = models.Banner.objects.all()
    return render(request,'deshboard/crud/list.html', {'banners': banners})

def banner_detail(request, banner_id):
    banner = models.Banner.objects.get(pk=banner_id)
    return render(request,'deshboard/crud/detail.html', {'banner': banner})

def banner_create(request):
    if request.method == 'POST':
        form = models.Banner(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('banner_list')
    else:
        form = models.Banner()
    return render(request,'main/banner_form.html', {'form': form})

def banner_update(request, banner_id):
    banner = models.Banner.objects.get(pk=banner_id)
    if request.method == 'POST':
        form = models.Banner(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            form.save()
            return redirect('banner_detail', banner_id=banner_id)
    else:
        form = models.Banner(instance=banner)
    return render(request,'main/banner_form.html', {'form': form})

def banner_delete(request, banner_id):
    banner = models.Banner.objects.get(pk=banner_id)
    banner.delete()
    return redirect('banner_list')



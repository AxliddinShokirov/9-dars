from django.shortcuts import render, redirect
from main import models


def listBanner(request):
    queryset = models.Banner.objects.all()
    context = {}
    context['queryset'] = queryset

    return render(request, 'deshboard/crude/banner/list.html', context)


def detailBanner(request, id):
    queryset = models.Banner.objects.get(id=id)
    context = {}
    context['queryset'] = queryset

    return render(request, 'deshboard/crude/banner/detail.html', context)


def createBanner(request):
    if request.method == 'POST':
        banner = models.Banner.objects.create(
            title = request.POST['title'],
            sub_title = request.POST['sub_title'],
            img = request.FILES.get('image')
        )
        return redirect('listBanner')
    return render(request, 'deshboard/crude/banner/create.html')


def updateBanner(request, id):
    data = models.Banner.objects.get(id=id)

    context = {
        'data': data
    }

    if request.method == 'POST':
        data.title = request.POST.get('title', data.title)
        data.sub_title = request.POST.get('sub_title', data.sub_title)
        img_file = request.FILES.get('image')
        data.img = img_file
        
        for key, value in request.FILES.items():
            print(f'File key: {key}, File: {value}')

        data.save()
        return redirect('listBanner')
    
    return render(request, 'deshboard/crude/banner/update.html', context)




def deleteBanner(request, id):
    models.Banner.objects.get(id=id).delete()
    return redirect('listBanner')
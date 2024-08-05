from main import models
from django.shortcuts import render, redirect

def contact_update(request):
    if request.method == 'POST':
        contact = models.Contact(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = models.Contact()
        return render(request, 'deshboard/contact', {'form': form})
    
def contact_delete(request):
    if request.method == 'POST':
        contact = models.Contact.objects.get(pk=request.POST.get('pk'))
        contact.delete()
        return redirect('contact')
    return render(request, 'contact/delete.html')

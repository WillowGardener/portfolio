from django.shortcuts import render
from django.http import HttpResponse
from .models import Camoimage
from .forms import ImageForm


    

def home(request):

    #this doesn't work. Why not?
    images = Camoimage.objects.all()
    for item in images:
        item.delete()
        

    form = ImageForm()
    context = {'form': form}
    return render(request, 'home.html', context) 

def camoize(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # pattern = request.POST['baseimage']
            
            pattern = form.save()

            pattern.camodraw()
            context = {'pattern': pattern}
    return render(request, 'camoize.html', context)






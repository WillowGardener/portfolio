from django.shortcuts import render
from .models import Grass
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def home(request):
    return render(request, 'home.html')


def run_simulation(request):
    for i in range(10):
        Grass.objects.create()
    grasses = Grass.objects.all()
    context = {
        'grasses': grasses
    }
    return render(request, 'simulation.html', context)
    
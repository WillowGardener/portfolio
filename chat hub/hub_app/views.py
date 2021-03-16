from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Card, Link

def home(request):
    cards = Card.objects.all()
    context = {
        'cards': cards,
    }
    return render(request, 'home.html', context)

def login(request):
    return render(request, 'login.html')

def travis(request):
    return render(request, 'travis.html')


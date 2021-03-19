from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Card, Link
from django.urls import reverse
from .forms import CardForm

def home(request):
    cards = Card.objects.all()
    context = {
        'cards': cards,
    }
    return render(request, 'home.html', context)

def login(request):
    return render(request, 'login.html')

def travis(request):
    cards = Card.objects.all()
    
    context = {
        'cards': cards,
    }
    return render(request, 'travis.html', context)

def add_card(request):
    Card.objects.create(name=None,text="")
    cards = Card.objects.all()
    context = {
        'cards': cards,
    }
    return render(request, 'travis.html', context)

def add_link(request, card_id):
    card_got = get_object_or_404(Card,pk=card_id)
    link_text = request.POST.get('link_text')
    Link.objects.create(text=link_text, card=card_got)
    cards = Card.objects.all()
    context = {
        'cards': cards,
    }
    return render(request, 'travis.html', context)

def delete_card(request, card_id):
    card_got = get_object_or_404(Card, pk=card_id)
    card_got.delete()
    cards = Card.objects.all()
    context = {
        'cards': cards,
    }
    return render(request, 'travis.html', context)


def edit_card(request, card_id):
    card_got = get_object_or_404(Card,pk=card_id)
    card_got.text = request.POST.get('card_text')
    card_got.save()
    cards = Card.objects.all()
    context = {
        'cards': cards,
    }
    return render(request, 'travis.html', context)
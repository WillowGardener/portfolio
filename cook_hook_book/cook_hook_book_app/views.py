from django.shortcuts import render

from .models import Card, Image, Post

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'home.html', context)

def new_post(request):
    

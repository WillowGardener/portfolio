from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Card, Image, Post

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'home.html', context)

def new_post(request):
    new_post = Post.objects.create()
    context = {
        'new_post': new_post,
    }
    return render(request, 'new_post.html', context)

def new_card(request, post_id):
    post_got = get_object_or_404(Post,pk=post_id)
    Card.objects.create(post=post_got)
    context = {
        'new_post': new_post,
    }
    return HttpResponseRedirect(reverse('cook_hook_book_app:new_post'), context)


def create_post(request):
    return HttpResponseRedirect(reverse('cook_hook_book_app:home'))
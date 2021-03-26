from django.shortcuts import render, get_object_or_404, redirect
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
    post = Post.objects.create()
    context = {
        'post': post,
    }
    return render(request, 'new_post.html', context)

def new_card(request, post_id):
    post = get_object_or_404(Post,pk=post_id)
    Card.objects.create(post=post)
    context = {
        'post': post,
    }
    
    return redirect('cook_hook_book_app:add_content', post_id)

def card_title(request, card_id):
    card = get_object_or_404(Card,pk=card_id)
    if request.method == 'POST':
        card.title = request.POST["card_title"]
        card.save()
    return redirect('cook_hook_book_app:add_content', card.post.id)

def add_image(request, card_id):
    card = get_object_or_404(Card,pk=card_id)
    if request.method == 'POST':
        image = Image.objects.create(card=card)
        image.image = request.POST["image"]
        image.position = request.POST["position"]
        image.caption = request.POST["caption"]
    return redirect('cook_hook_book_app:add_content', card.post.id)

def card_text(request, card_id):
    card = get_object_or_404(Card,pk=card_id)
    if request.method == 'POST':
        card.text = request.POST['card_text']
        card.save()
    return redirect('cook_hook_book_app:add_content', card.post.id)

def add_content(request, post_id):
    post = get_object_or_404(Post,pk=post_id)
    if request.method == 'POST':
        post.title = request.POST['post_title']
        post.category = request.POST['post_category']
        post.save()
    context = {
        'post': post,
    }
    return render(request,'add_content.html', context)
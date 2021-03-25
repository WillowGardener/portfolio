from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'cook_hook_book_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('new_post', views.new_post, name='new_post'),
]

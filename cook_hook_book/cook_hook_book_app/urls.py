from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'cook_hook_book'

urlpatterns = [
    path('', views.home, name='home'),
]

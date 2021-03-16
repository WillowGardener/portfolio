from django.urls import path
from . import views

app_name = 'hub_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('travis', views.travis, name='travis'),
    path('add', views.add_card, name='add_card'),
    path('delete/<int:card_id>', views.delete_card, name='delete_card')
]
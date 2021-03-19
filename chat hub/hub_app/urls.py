from django.urls import path
from . import views

app_name = 'hub_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('travis', views.travis, name='travis'),
    path('add', views.add_card, name='add_card'),
    path('delete/<int:card_id>', views.delete_card, name='delete_card'),
    path('edit/<int:card_id>', views.edit_card, name='edit_card'),
    path('add_link/<int:card_id>', views.add_link, name='add_link'),
    path('delete_link/<int:link_id>', views.delete_link, name='delete_link')
]
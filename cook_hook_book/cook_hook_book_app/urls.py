from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cook_hook_book_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('new_post', views.new_post, name='new_post'),
    path('new_card/<int:post_id>', views.new_card, name='new_card'),
    path('create_post', views.create_post, name='create_post'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


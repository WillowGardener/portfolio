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
    path('add_content/<int:post_id>', views.add_content, name='add_content'),
    path('card_title/<int:card_id>', views.card_title, name='card_title'),
    path('add_image/<int:card_id>', views.add_image,name='add_image'),
    path('card_text/<int:card_id>', views.card_text,name='card_text'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


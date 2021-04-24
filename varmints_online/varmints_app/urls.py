from django.urls import path
from . import views

app_name = 'varmints_app'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('run_simulation', views.run_simulation, name='run_simulation')
]
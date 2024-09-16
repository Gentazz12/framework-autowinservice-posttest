from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('layanan/', views.services, name='services'),
]

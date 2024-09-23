# autowin/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('layanan/', views.services_view, name='services'),  # Panggil services_view di sini
]

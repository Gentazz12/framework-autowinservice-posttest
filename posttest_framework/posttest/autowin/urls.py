# autowin/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('layanan/', views.services_view, name='services'),  # Panggil services_view di sini
    path('pelanggan/', views.pelanggan_index, name='pelanggan_index'),
    path('pelanggan/create/', views.pelanggan_create, name='pelanggan_create'),# Create
    path('pelanggan/update/<int:pelanggan_id>', views.pelanggan_update, name='pelanggan_update'),
    path('pelanggan/delete/<int:pelanggan_id>', views.pelanggan_delete, name='pelanggan_delete'),
]

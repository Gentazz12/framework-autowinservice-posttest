# views.py
from django.shortcuts import render
from autowin.models import Servis

def home(request):
    return render(request, 'bengkel/home.html')

def services_view(request):  # Pastikan ini ada
    servis_list = Servis.objects.all()
    return render(request, 'bengkel/services.html', {'servis_list': servis_list})

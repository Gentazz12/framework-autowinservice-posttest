from django.shortcuts import render

def home(request):
    return render(request, 'bengkel/home.html')

def services(request):
    return render(request, 'bengkel/services.html')

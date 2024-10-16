# views.py
from django.shortcuts import render, redirect, get_object_or_404
from autowin.models import Servis
from autowin.models import Pelanggan
from .forms import PelangganForm
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q

def home(request):
    return render(request, 'bengkel/home.html')

def services_view(request):  # Pastikan ini ada
    servis_list = Servis.objects.all()
    return render(request, 'bengkel/services.html', {'servis_list': servis_list})

# READ Mahasiswa
def pelanggan_index(request):
    query = request.GET.get('q')
    pelanggans = Pelanggan.objects.all()
    if query:
        pelanggans = Pelanggan.objects.filter(
            Q(nama__icontains=query) |
            Q(email__icontains=query) |
            Q(no_hp__icontains=query) |
            Q(alamat__icontains=query)
        )
    else:
        pelanggans = Pelanggan.objects.all()
    return render(request, 'pelanggan/index.html', {'pelanggans': pelanggans})

# CREATE Mahasiswa
def pelanggan_create(request):
    if request.method == 'POST':
        form = PelangganForm(request.POST)
        if form.is_valid():
            form.save() # Simpan data mahasiswa ke database
            messages.success(request, 'Pelanggan berhasil dibuat!') # Pesan sukses
            return redirect('pelanggan_index') # Redirect ke halaman index mahasiswa
    else:
        form = PelangganForm()
    return render(request, 'pelanggan/create.html', {'form': form})

# UPDATE Mahasiswa
def pelanggan_update(request, pelanggan_id):
    pelanggan = get_object_or_404(Pelanggan, id=pelanggan_id)
    if request.method == 'POST':
        form = PelangganForm(request.POST, instance=pelanggan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Pelanggan berhasil diubah!')
            return redirect('pelanggan_index')
    else:
        form = PelangganForm(instance=pelanggan)
    return render(request, 'pelanggan/update.html', {'form': form, 'pelanggan': pelanggan})

# DELETE Mahasiswa
def pelanggan_delete(request, pelanggan_id):
    pelanggan = get_object_or_404(Pelanggan, id=pelanggan_id)
    pelanggan.delete()
    messages.success(request, 'Data Pelanggan berhasil dihapus')
    return JsonResponse({'success': True})



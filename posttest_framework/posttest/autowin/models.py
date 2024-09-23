from django.db import models

class Pelanggan(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    no_hp = models.CharField(max_length=30)
    alamat = models.TextField()

    def __str__(self):
        return self.nama

class Servis(models.Model):
    pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE)
    jenis_servis = models.CharField(max_length=100)
    tanggal_servis = models.DateField()
    biaya = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.jenis_servis} - {self.pelanggan.nama}'
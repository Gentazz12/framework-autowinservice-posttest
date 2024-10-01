from django.db import models
from django.utils import timezone

# Model Pelanggan
class Pelanggan(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    no_hp = models.CharField(max_length=30)
    alamat = models.TextField()

    def __str__(self):
        return self.nama

# Model Servis
class Servis(models.Model):
    pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE)
    jenis_servis = models.CharField(max_length=100)
    tanggal_servis = models.DateField()
    biaya = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.jenis_servis} - {self.pelanggan.nama}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        RiwayatServis.objects.create(
            servis=self,
            tanggal=timezone.now(),
            keterangan=f'Servis {self.jenis_servis} untuk {self.pelanggan.nama} telah dibuat.'
        )

# Model RiwayatServis
class RiwayatServis(models.Model):
    servis = models.ForeignKey(Servis, on_delete=models.CASCADE)
    tanggal = models.DateTimeField()
    keterangan = models.TextField()

    def __str__(self):
        return f'Riwayat: {self.servis.jenis_servis} pada {self.tanggal}'

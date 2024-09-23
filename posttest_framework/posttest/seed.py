from autowin.models import Pelanggan, Servis
from faker import Faker
import random

fake = Faker()

# Seed Pelanggan
for _ in range(10):
    Pelanggan.objects.create(
        nama=fake.name(),
        email=fake.email(),
        no_hp=fake.phone_number(),
        alamat=fake.address()
    )

# Seed Servis
jenis_servis_list = ['Ganti Oli', 'Servis Umum', 'Servis Rem', 'Tune Up']
pelanggan_list = Pelanggan.objects.all()

for _ in range(10):
    Servis.objects.create(
        pelanggan=random.choice(pelanggan_list),
        jenis_servis=random.choice(jenis_servis_list),
        tanggal_servis=fake.date_this_year(),
        biaya=round(random.uniform(100000, 500000), 2)
    )

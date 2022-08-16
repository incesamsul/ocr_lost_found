from time import timezone
from django.db import models
from django.utils import timezone

class Barang(models.Model):
    # Nama Penumpang	Pesawat	Tanggal	Kode Booking
    nama_penumpang = models.CharField(max_length=100)
    pesawat = models.CharField(max_length=100)
    kode_booking = models.CharField(max_length=100)
    kode_penerbangan = models.CharField(max_length=100, default='')
    tanggal = models.CharField(max_length=100)
    tujuan = models.CharField(max_length=100, default='')
    # tanggal = models.DateTimeField(default=timezone.now)
      
      
class Image(models.Model):
    image = models.ImageField(upload_to='images')
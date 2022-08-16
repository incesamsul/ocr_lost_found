from django.contrib import admin
from numpy import imag

# Register your models here.

from . models import Image
from . models import Barang

admin.site.register(Image)
admin.site.register(Barang)
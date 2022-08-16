from urllib.request import urlopen
from django.shortcuts import redirect, render

import cv2
from matplotlib import image
import numpy as np
from . models import *
from django.contrib import messages
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from PIL import Image as pil_image
import pytesseract
from django.contrib.staticfiles.storage import staticfiles_storage

# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# img_path = staticfiles_storage.path('img/bukti.jpg')
# img = cv2.imread(img_path)
# img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# brightness = -110
# contrast = 170
# img = np.int16(img)
# img = img * (contrast/127+1) - contrast + brightness
# img = np.clip(img, 0, 255)
# img = np.uint8(img)
# img = cv2.bitwise_not(img)


# text = pytesseract.image_to_string(img)

def home(request):
    data = {
        'ocr' : 'wha'
    }   
    return render(request, 'pages/home.html', data)

def scan(request):
    return render(request, 'pages/scan.html')

def scanGaruda(request):
    return render(request, 'pages/scan-garuda.html')

def scanSriwijaya(request):
    return render(request, 'pages/scan-sriwijaya.html')

def scanCitilink(request):
    return render(request, 'pages/scan-citilink.html')

def scanSuperAirJet(request):
    return render(request, 'pages/scan-super-air-jet.html')

def scanLion(request):
    return render(request, 'pages/scan-lion.html')

def scanMenu(request):
    return render(request, 'pages/scan-menu.html')

def pos(request):
    barang = Barang.objects.all()
    context = {
        "barang": barang
    }
    return render(request, 'pages/pos.html', context)

def crop(request):
    image =  Image.objects.last()
    return render(request, 'pages/crop.html',{'image':image})

def add_item(request):
    if request.method == "POST":
        nama_penumpang = request.POST["nama_penumpang"]
        pesawat = request.POST["pesawat"]
        tanggal = request.POST["tanggal"]
        kode_booking = request.POST["kode_booking"]
        kode_penerbangan = request.POST["kode_penerbangan"]
        tujuan = request.POST["tujuan"]
        
        barang = Barang(nama_penumpang=nama_penumpang, pesawat=pesawat, tanggal=tanggal, kode_booking=kode_booking, kode_penerbangan=kode_penerbangan, tujuan=tujuan)
        barang.save()
        messages.info(request, "berhasil di tambah")
    else:
        pass
    
    barang = Barang.objects.all()
    context = {
        "barang": barang
    }
    return render(request, 'pages/home.html', context)
    
def image_upload(request):
    context = dict()
    if request.method == 'POST':
        path = request.POST["src"]
        image = NamedTemporaryFile()
        image.write(urlopen(path).read())
        image.flush()
        image = File(image)
        name = str(image.name).split('\\')[-1]
        name += '.jpg'
        image.name = name
        textOCR = pytesseract.image_to_string(pil_image.open(image))
        result  = textOCR.split(" ")
        listResult = []
        pesawat = request.POST["pesawat"]
        for x in result:
            listResult.append(x.replace("\n", "  ").split(" "))
        listResult.append(pesawat)
        
        if image is not None:
            obj = Image.objects.create(image=image)  # create a object of Image type defined in your model
            obj.save()
            context["path"] = obj.image.url  #url to image stored 
        else :
            return redirect('/scan/hmm', {"test" : listResult})
        return render(request, 'pages/home.html', {"data": listResult})  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.            
    return render(request, 'pages/scan.html/hmmm', {"data": listResult})  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.            


# SRIWIJAYA SCANNER
def scanner_sriwijaya(request):
    context = dict()
    if request.method == 'POST':
        path = request.POST["src"]
        image = NamedTemporaryFile()
        image.write(urlopen(path).read())
        image.flush()
        image = File(image)
        name = str(image.name).split('\\')[-1]
        name += '.jpg'
        image.name = name
        textOCR = pytesseract.image_to_string(pil_image.open(image))
        result  = textOCR.split(" ")
        listResult = []
        pesawat = request.POST["pesawat"]
        for x in result:
            listResult.append(x.replace("\n", "  ").split(" "))
        listResult.append(pesawat)
        
        if image is not None:
            obj = Image.objects.create(image=image)  # create a object of Image type defined in your model
            obj.save()
            context["path"] = obj.image.url  #url to image stored 
        else :
            return redirect('/scan/hmm', {"test" : listResult})
        return render(request, 'pages/input_sriwijaya.html', {"data": listResult})  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.            
    return render(request, 'pages/scan.html/hmmm', {"data": listResult})  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.            



# CITILINK SCANNER
def scanner_citilink(request):
    context = dict()
    if request.method == 'POST':
        path = request.POST["src"]
        image = NamedTemporaryFile()
        image.write(urlopen(path).read())
        image.flush()
        image = File(image)
        name = str(image.name).split('\\')[-1]
        name += '.jpg'
        image.name = name
        textOCR = pytesseract.image_to_string(pil_image.open(image))
        result  = textOCR.split(" ")
        listResult = []
        pesawat = request.POST["pesawat"]
        for x in result:
            listResult.append(x.replace("\n", "  ").split(" "))
        listResult.append(pesawat)
        
        if image is not None:
            obj = Image.objects.create(image=image)  # create a object of Image type defined in your model
            obj.save()
            context["path"] = obj.image.url  #url to image stored 
        else :
            return redirect('/scan/hmm', {"test" : listResult})
        return render(request, 'pages/input_citilink.html', {"data": listResult})  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.            
    return render(request, 'pages/scan.html/hmmm', {"data": listResult})  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.            


# SUPER AIR JET SCANNER
def scanner_super_air_jet(request):
    context = dict()
    if request.method == 'POST':
        path = request.POST["src"]
        image = NamedTemporaryFile()
        image.write(urlopen(path).read())
        image.flush()
        image = File(image)
        name = str(image.name).split('\\')[-1]
        name += '.jpg'
        image.name = name
        textOCR = pytesseract.image_to_string(pil_image.open(image))
        result  = textOCR.split(" ")
        listResult = []
        pesawat = request.POST["pesawat"]
        for x in result:
            listResult.append(x.replace("\n", "  ").split(" "))
        listResult.append(pesawat)
        
        if image is not None:
            obj = Image.objects.create(image=image)  # create a object of Image type defined in your model
            obj.save()
            context["path"] = obj.image.url  #url to image stored 
        else :
            return redirect('/scan/hmm', {"test" : listResult})
        return render(request, 'pages/input_super_air_jet.html', {"data": listResult})  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.            
    return render(request, 'pages/scan.html/hmmm', {"data": listResult})  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.            

# LION SCANNER
def scanner_lion(request):
    context = dict()
    if request.method == 'POST':
        path = request.POST["src"]
        image = NamedTemporaryFile()
        image.write(urlopen(path).read())
        image.flush()
        image = File(image)
        name = str(image.name).split('\\')[-1]
        name += '.jpg'
        image.name = name
        textOCR = pytesseract.image_to_string(pil_image.open(image))
        result  = textOCR.split(" ")
        listResult = []
        pesawat = request.POST["pesawat"]
        for x in result:
            listResult.append(x.replace("\n", "  ").split(" "))
        listResult.append(pesawat)
        
        if image is not None:
            obj = Image.objects.create(image=image)  # create a object of Image type defined in your model
            obj.save()
            context["path"] = obj.image.url  #url to image stored 
        else :
            return redirect('/scan/hmm', {"test" : listResult})
        return render(request, 'pages/input_lion.html', {"data": listResult})  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.            
    return render(request, 'pages/scan.html/hmmm', {"data": listResult})  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.            
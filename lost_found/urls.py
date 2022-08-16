from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.scanMenu, name='scan-menu'),
    path('scan', views.scan, name='scan'),
    path('scan-menu', views.scanMenu, name='scan-menu'),
    path('scan-garuda', views.scanGaruda, name='scan-garuda'),
    path('scan-sriwijaya', views.scanSriwijaya, name='scan-sriwijaya'),
    path('scan-citilink', views.scanCitilink, name='scan-citilink'),
    path('scan-super-air-jet', views.scanSuperAirJet, name='scan-super-air-jet'),
    path('scan-lion', views.scanLion, name='scan-lion'),
    path('crop', views.crop, name='crop'),
    path('pos', views.pos, name='pos'),
    path('add_item', views.add_item, name='add_item'),
    path('image_upload', views.image_upload, name='image_upload'),
    path('scanner_sriwijaya', views.scanner_sriwijaya, name='scanner_sriwijaya'),
    path('scanner_citilink', views.scanner_citilink, name='scanner_citilink'),
    path('scanner_super_air_jet', views.scanner_super_air_jet, name='scanner_super_air_jet'),
    path('scanner_lion', views.scanner_lion, name='scanner_lion'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
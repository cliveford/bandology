from django.urls import path
from . import views

urlpatterns = [
    path("bands/", views.api_all_bands), 
    path("musicians/", views.api_all_musicians),
    path("albums/", views.api_all_albums),
    path("instruments/", views.api_all_instruments),
    path("band/<int:id>", views.api_band_detail),
    path("musician/<int:id>", views.api_musician_detail),
    path("instrument/<int:id>", views.api_instrument_detail),
    path("album/<int:id>", views.api_album_detail),
    path("band/", views.api_band_create),
    path("album/", views.api_album_create),
    path("musician/", views.api_musician_create),
    path("instrument/", views.api_instrument_create),
    
    ]
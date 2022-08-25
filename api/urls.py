import imp
from django.urls import path
from . import views

urlpatterns = [
    path("bands/", views.api_all_bands, name='get-all-bands'), 
    path("musicians/", views.api_all_musicians, name='get-all-musicians'),
    path("albums/", views.api_all_albums, name='get-all-albums'),
    path("instruments/", views.api_all_instruments, name='get-all-instruments'),

    path("update/band/<int:id>", views.api_update_band, name='update-band-details'),
    path("update/album/<int:id>", views.api_update_album, name='update-album-details'),
    path("update/musician/<int:id>", views.api_update_musician, name='update-musician-details'),
    path("update/instrument/<int:id>", views.api_update_instrument, name='update-instrument-details'),

    path("band/<int:id>", views.api_band_detail, name='band-details'),
    path("musician/<int:id>", views.api_musician_detail, name='musician-details'),
    path("instrument/<int:id>", views.api_instrument_detail, name='instrument-details'),
    path("album/<int:id>", views.api_album_detail, name='album-details'),

    path("del/band/<int:id>", views.api_delete_band, name='delete-band'),
    path("del/musician/<int:id>", views.api_delete_musician, name='delete-musician'),
    path("del/instrument/<int:id>", views.api_delete_instrument, name='delete-instrument'),
    path("del/album/<int:id>", views.api_delete_album, name='delete-album'),

    path("add/band/", views.api_band_create, name='create-new-band'),
    path("add/album/", views.api_album_create, name='create-new-album'),
    path("add/musician/", views.api_musician_create, name='create-new-musician'),
    path("add/instrument/", views.api_instrument_create, name='create-new-instrument'),
    
    ]
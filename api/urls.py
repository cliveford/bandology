from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_all_bands), 
    path("musicians/", views.api_all_musicians),
    path("band/<int:id>", views.api_band_detail),
    path("band/", views.api_band_create),
    path("album/", views.api_album_create),
    path("albums/", views.api_all_albums),
    ]
import json
from unicodedata import name
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

from api.views import api_all_bands, api_all_albums, api_all_musicians, api_all_instruments, api_band_detail, api_album_detail
from ..models import Band, Album, Musician, Instrument
from ..serializers import BandSerializer, AlbumSerializer, MusicianSerializer, InstrumentSerializer


client = Client()

class GetAllTestCase(TestCase):

    def setUp(self):
        Band.objects.create(name='Rolling Stones', genre='Rock', formed='1962-08-04')

    def test_get_all_bands(self):
        response = client.get(reverse(api_all_bands))
        bands = Band.objects.all()
        serializer = BandSerializer(bands, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_albums(self):
        response = client.get(reverse(api_all_albums))
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_musicians(self):
        response = client.get(reverse(api_all_musicians))
        musicians = Musician.objects.all()
        serializer = MusicianSerializer(musicians, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_instruments(self):
        response = client.get(reverse(api_all_instruments))
        instruments = Instrument.objects.all()
        serializer = InstrumentSerializer(instruments, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetByIdTestCase(TestCase):

    def setUp(self):
        Band.objects.create(name='Rolling Stones', genre='Rock', formed='1962-08-04')

    def test_get_band_by_id(self):
        response = client.get(reverse(api_band_detail, kwargs={'id': 1}))
        band = Band.objects.get(id=1)

        serializer = BandSerializer(band)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def setUp(self):
        Band.objects.create(name='Rolling Stones', genre='Rock', formed='1962-08-04')
        band = Band.objects.get(id=1)
        Album.objects.create(title='Sticky Fingers', released='1969-12-05', band=band)

    def test_get_album_by_id(self):
        response = client.get(reverse(api_album_detail, kwargs={'id': 1}))
        album = Album.objects.get(id=1)

        serializer = AlbumSerializer(album)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
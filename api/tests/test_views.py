import json
from unicodedata import name
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

from api.views import api_all_bands, api_all_albums, api_all_musicians, api_all_instruments, api_band_detail, api_album_detail, api_musician_detail, api_instrument_detail
from ..models import Band, Album, Musician, Instrument
from ..serializers import BandSerializer, AlbumSerializer, MusicianSerializer, InstrumentSerializer


client = Client()

class GetAllTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Band.objects.create(name='Rolling Stones', genre='Rock', formed='1962-08-04')
        Band.objects.create(name='The Beatles', genre='Pop', formed='1962-08-04') 
        cls.bands = Band.objects.all() 
        cls.band = Band.objects.get(id=1)
        Album.objects.create(title='Sticky Fingers', released='1969-12-05', band=cls.band)  
        Album.objects.create(title='Stick People', released='1968-10-05', band=cls.band) 
        cls.albums = Album.objects.all()   
        Musician.objects.create(first_name='Mick', last_name='Jagger', band=cls.band)
        Musician.objects.create(first_name='Keith', last_name='Richards', band=cls.band)
        cls.musicians = Musician.objects.all()
        Instrument.objects.create(name='guitar')
        Instrument.objects.create(name='drums')
        cls.instruments = Instrument.objects.all()


    def test_get_all_bands(self):
        response = client.get(reverse(api_all_bands))
        serializer = BandSerializer(self.bands, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_albums(self):
        response = client.get(reverse(api_all_albums))
        serializer = AlbumSerializer(self.albums, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_musicians(self):
        response = client.get(reverse(api_all_musicians))
        serializer = MusicianSerializer(self.musicians, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_instruments(self):
        response = client.get(reverse(api_all_instruments))
        serializer = InstrumentSerializer(self.instruments, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class GetByIdTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Band.objects.create(name='Rolling Stones', genre='Rock', formed='1962-08-04') 
        cls.band = Band.objects.get(id=1) 
        Album.objects.create(title='Sticky Fingers', released='1969-12-05', band=cls.band)  
        cls.album = Album.objects.get(id=1)   
        Musician.objects.create(first_name='Mick', last_name='Jagger', band=cls.band)
        cls.musician = Musician.objects.get(id=1)
        Instrument.objects.create(name='guitar')
        cls.instrument = Instrument.objects.get(id=1)

    

    def test_get_band_by_id(self):
        response = client.get(reverse(api_band_detail, kwargs={'id': 1}))
        serializer = BandSerializer(self.band)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_album_by_id(self):
        response = client.get(reverse(api_album_detail, kwargs={'id': 1}))
        serializer = AlbumSerializer(self.album)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_musician_by_id(self):
        response = client.get(reverse(api_musician_detail, kwargs={'id': 1}))
        serializer = MusicianSerializer(self.musician)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_instrument_by_id(self):
        response = client.get(reverse(api_instrument_detail, kwargs={'id': 1}))
        serializer = InstrumentSerializer(self.instrument)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

   
# class GetByIdTestCase(TestCase):


#     def setUp(self):
#         Band.objects.create(name='Rolling Stones', genre='Rock', formed='1962-08-04')

#     def test_get_band_by_id(self):
#         response = client.get(reverse(api_band_detail, kwargs={'id': 1}))
#         band = Band.objects.get(id=1)

#         serializer = BandSerializer(band)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


#     def setUp(self):
#         Band.objects.create(name='Rolling Stones', genre='Rock', formed='1962-08-04')
#         band = Band.objects.get(id=1)
#         Album.objects.create(title='Sticky Fingers', released='1969-12-05', band=band)

#     def test_get_album_by_id(self):
#         response = client.get(reverse(api_album_detail, kwargs={'id': 1}))
#         album = Album.objects.get(id=1)

#         serializer = AlbumSerializer(album)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def setUp(self):
#         Band.objects.create(name='Rolling Stones', genre='Rock', formed='1962-08-04')
#         band = Band.objects.get(id=1)
#         print(band)
#         Musician.objects.create(first_name='Mick', last_name='Jagger', band=band)

#     def test_get_musician_by_id(self):
#         response = client.get(reverse(api_musician_detail, kwargs={'id': 1}))
#         musician = Musician.objects.get(id=1)

#         serializer = MusicianSerializer(musician)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

import json
from unicodedata import name
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

from api.views import api_album_create, api_all_bands, api_all_albums, api_all_musicians, api_all_instruments, api_band_create, api_band_detail, api_album_detail, api_delete_album, api_delete_band, api_delete_instrument, api_delete_musician, api_instrument_create, api_musician_create, api_musician_detail, api_instrument_detail, api_update_album, api_update_band, api_update_instrument, api_update_musician
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


class PutByIdTestCase(TestCase):

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

        cls.valid_band_payload = {
            'name': 'Rollin Bones',
            'genre': 'Funk',
            'formed': '1970-09-11'
        }
        cls.invalid_band_payload = {
            'name': 'Funny Bones',
            'genre': 'Funk',
            'formed': 2001
        }

        cls.valid_album_payload = {
             'title': 'Random',
             'released': '1971-09-09',
        }
        cls.invalid_album_payload = {
             'title': 'Random',
             'released': 3003,
        }

        cls.valid_musician_payload = {
            'first_name': 'Mick',
            'last_name': 'Funk',
        }
        cls.invalid_musician_payload = {
            'first_name': 'Bones',
            'last': 2001
        }

        cls.valid_instrument_payload = {
            'name': 'oboe'
        }
        cls.invalid_instrument_payload = {
            'something': 999
        }

    def test_valid_update_band(self):
        response = client.put(reverse(api_update_band, kwargs={'id': 1}), 
        data=json.dumps(self.valid_band_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_band(self):
        response = client.put(reverse(api_update_band, kwargs={'id': 1}), 
        data=json.dumps(self.invalid_band_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_album(self):
        response = client.put(reverse(api_update_album, kwargs={'id': 1}), 
        data=json.dumps(self.valid_album_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_album(self):
        response = client.put(reverse(api_update_album, kwargs={'id': 1}), 
        data=json.dumps(self.invalid_album_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_musician(self):
        response = client.put(reverse(api_update_musician, kwargs={'id': 1}), 
        data=json.dumps(self.valid_musician_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_musician(self):
        response = client.put(reverse(api_update_musician, kwargs={'id': 1}), 
        data=json.dumps(self.invalid_musician_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_instrument(self):
        response = client.put(reverse(api_update_instrument, kwargs={'id': 1}), 
        data=json.dumps(self.valid_instrument_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_instrument(self):
        response = client.put(reverse(api_update_instrument, kwargs={'id': 1}), 
        data=json.dumps(self.invalid_instrument_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    

class PostTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
 
        cls.valid_band_payload = {
            'name': 'Rollin Bones',
            'genre': 'Funk',
            'formed': '1970-09-11'
        }
        cls.invalid_band_payload = {
            'name': 'Funny Bones',
            'genre': 'Funk',
            'formed': 2001
        }

        cls.valid_album_payload = {
             'title': 'Random',
             'released': '1971-09-09',
        }
        cls.invalid_album_payload = {
             'title': 'Random',
             'released': 3003,
        }

        cls.valid_musician_payload = {
            'first_name': 'Mick',
            'last_name': 'Funk',
        }
        cls.invalid_musician_payload = {
            'first_name': 'Bones',
            'last': 2001
        }

        cls.valid_instrument_payload = {
            'name': 'oboe'
        }
        cls.invalid_instrument_payload = {
            'something': 999
        }


    def test_valid_create_band(self):
        response = client.post(reverse(api_band_create), 
        data=json.dumps(self.valid_band_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_create_band(self):
        response = client.post(reverse(api_band_create), 
        data=json.dumps(self.invalid_band_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_create_album(self):
        response = client.post(reverse(api_album_create), 
        data=json.dumps(self.valid_album_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_create_album(self):
        response = client.post(reverse(api_album_create), 
        data=json.dumps(self.invalid_album_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_create_musician(self):
        response = client.post(reverse(api_musician_create), 
        data=json.dumps(self.valid_musician_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_create_musician(self):
        response = client.post(reverse(api_musician_create), 
        data=json.dumps(self.invalid_musician_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_create_instrument(self):
        response = client.post(reverse(api_instrument_create), 
        data=json.dumps(self.valid_instrument_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_create_instrument(self):
        response = client.post(reverse(api_instrument_create), 
        data=json.dumps(self.invalid_instrument_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
   
class DeleteByIdTestCase(TestCase):

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

    def test_delete_instrument_by_id(self):
        response = client.delete(reverse(api_delete_instrument, kwargs={'id': 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_musician_by_id(self):
        response = client.delete(reverse(api_delete_musician, kwargs={'id': 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_album_by_id(self):
        response = client.delete(reverse(api_delete_album, kwargs={'id': 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_band_by_id(self):
        response = client.delete(reverse(api_delete_band, kwargs={'id': 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


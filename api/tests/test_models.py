from unicodedata import name
from django.test import TestCase
from ..models import Band


class BandTest(TestCase):

    def setUp(self):
        Band.objects.create(
            name='Testycles', genre='Jazz', formed='1990-08-10'
        )
        Band.objects.create(
            name='Testyfies', genre='Avant Garde', formed='1966-08-10'
        )

    def test_band_genre(self):
        band_testycles = Band.objects.get(name='Testycles')
        band_testyfies = Band.objects.get(name='Testyfies')
        self.assertEqual(band_testycles.get_genre(), 'Testycles belongs to Jazz genre.')
        self.assertEqual(band_testyfies.get_genre(), 'Testyfies belongs to Avant Garde genre.')
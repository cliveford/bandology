from pyexpat import model
from rest_framework import serializers
from .models import Band, Album, Musician, Instrument


class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ['name']


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ["first_name", "last_name", "band"]


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ["name", "genre", "formed"]


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["title", "released", "band"]





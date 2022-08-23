from pyexpat import model
from rest_framework import serializers
from .models import Band, Album, Musician, Instrument

class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ['name']


class MusicianSerializer(serializers.ModelSerializer):
    #instruments = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Musician
       #fields = ["first_name", "last_name", "instruments", "band"]
        fields = ["first_name", "last_name", "band"]


class BandSerializer(serializers.ModelSerializer):
    #musicians = serializers.StringRelatedField(many=True, required=False, read_only=True)
    #albums = serializers.StringRelatedField(many=True, required=False, read_only=True)

    class Meta:
        model = Band
        #fields = ["id", "name", "genre", "formed"]
        fields = ["name", "genre", "formed"]

    #def create(self, validated_data):
     #  return super().create(validated_data)

class AlbumSerializer(serializers.ModelSerializer):

    #band = BandSerializer(required=False, read_only=True)
    #band = BandSerializer(required=True)

    class Meta:
        model = Album
        fields = ["title", "released", "band"]





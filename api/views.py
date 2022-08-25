from django.shortcuts import render

from .models import Band, Album, Instrument, Musician
from .serializers import BandSerializer, MusicianSerializer, AlbumSerializer, InstrumentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


#----------------- Get Alls ----------------
@api_view(["GET"])
def api_all_bands(request):

    if request.method == "GET":

        bands = Band.objects.all()
        serializer = BandSerializer(bands, many=True)
        return Response(serializer.data)

@api_view(["GET"])
def api_all_musicians(request):

    if request.method == "GET":

        musicians = Musician.objects.all()
        serializer = MusicianSerializer(musicians, many=True)
        return Response(serializer.data)

@api_view(["GET"])
def api_all_albums(request):

    if request.method == "GET":

        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)

@api_view(["GET"])
def api_all_instruments(request):

    if request.method == "GET":

        instruments = Instrument.objects.all()
        serializer = InstrumentSerializer(instruments, many=True)
        return Response(serializer.data)

#---------------- update ----------------------------------

@api_view(["PUT"])
def api_update_band(request, id):

    try:
        band = Band.objects.get(pk=id)
    except Band.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = BandSerializer(band, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def api_update_album(request, id):

    try:
        album = Album.objects.get(pk=id)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = AlbumSerializer(album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def api_update_musician(request, id):

    try:
        musician = Musician.objects.get(pk=id)
    except Musician.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = MusicianSerializer(musician, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def api_update_instrument(request, id):

    try:
        instrument = Instrument.objects.get(pk=id)
    except Instrument.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = InstrumentSerializer(instrument, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#--------------- Get by id -------------------

@api_view(["GET"])
def api_band_detail(request, id):

    if request.method == "GET":
        try:
            band = Band.objects.get(pk=id)
        except Band.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BandSerializer(band)
        return Response(serializer.data)

@api_view(["GET"])
def api_album_detail(request, id):

    if request.method == "GET":
        try:
            album = Album.objects.get(pk=id)
        except Album.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AlbumSerializer(album)
        return Response(serializer.data)

@api_view(["GET"])
def api_musician_detail(request, id):

    if request.method == "GET":
        try:
            musician = Musician.objects.get(pk=id)
        except Musician.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MusicianSerializer(musician)
        return Response(serializer.data)

@api_view(["GET"])
def api_instrument_detail(request, id):

    if request.method == "GET":
        try:
            instrument = Instrument.objects.get(pk=id)
        except Instrument.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = InstrumentSerializer(instrument)
        return Response(serializer.data)

# ------------- deletes -------------------

@api_view(["DELETE"])
def api_delete_band(request, id):

    if request.method == "DELETE":
        try:
            band = Band.objects.get(pk=id)
        except Band.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        band.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["DELETE"])
def api_delete_album(request, id):

    if request.method == "DELETE":
        try:
            album = Album.objects.get(pk=id)
        except Album.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["DELETE"])
def api_delete_musician(request, id):

    if request.method == "DELETE":
        try:
            musician = Musician.objects.get(pk=id)
        except Musician.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        musician.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["DELETE"])
def api_delete_instrument(request, id):

    if request.method == "DELETE":
        try:
            instrument = Instrument.objects.get(pk=id)
        except Instrument.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        instrument.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# -------------- Posts -------------------        

@api_view(["POST"])
def api_band_create(request):

    if request.method == "POST":
        serializer = BandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def api_album_create(request):

    if request.method == "POST":
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def api_musician_create(request):

    if request.method == "POST":
        serializer = MusicianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def api_instrument_create(request):

    if request.method == "POST":
        serializer = InstrumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --------------------------------------------
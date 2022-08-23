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

#---------------- details ----------------------------------

@api_view(["PUT", "GET", "DELETE"])
def api_band_detail(request, id):

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

    if request.method == "GET":

        try:
            band = Band.objects.get(pk=id)
        except Band.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BandSerializer(band)
        return Response(serializer.data)

    elif request.method == "DELETE":
        band.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["PUT", "GET", "DELETE"])
def api_musician_detail(request, id):

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

    if request.method == "GET":

        serializer = MusicianSerializer(musician)
        return Response(serializer.data)

    elif request.method == "DELETE":
        musician.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["PUT", "GET", "DELETE"])
def api_album_detail(request, id):

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

    if request.method == "GET":

        serializer = AlbumSerializer(album)
        return Response(serializer.data)

    elif request.method == "DELETE":
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["PUT", "GET", "DELETE"])
def api_instrument_detail(request, id):

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

    if request.method == "GET":

        serializer = InstrumentSerializer(instrument)
        return Response(serializer.data)

    elif request.method == "DELETE":
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
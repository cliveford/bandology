from django.shortcuts import render

from .models import Band, Album, Musician
from .serializers import BandSerializer, MusicianSerializer, AlbumSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# from rest_framework import status

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

#--------------------------------------------------

@api_view(["PUT", "GET", "DELETE"])
def api_band_detail(request, id):

    if request.method == "PUT":
        serializer = BandSerializer(data=request.data)
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

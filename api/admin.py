from django.contrib import admin

from .models import Band, Musician, Album

admin.site.register(Band)
admin.site.register(Musician)
admin.site.register(Album)

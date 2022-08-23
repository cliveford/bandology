from django.contrib import admin

from .models import Band, Musician, Album, Instrument

admin.site.register(Band)
admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Instrument)

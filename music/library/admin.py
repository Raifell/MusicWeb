from django.contrib import admin
from .models import MusicGenre, MusicBand

admin.site.register(MusicBand)
admin.site.register(MusicGenre)

from django.shortcuts import render
from .models import MusicBand, MusicGenre


def main_page(request):
    return render(request, 'library/index_main.html')


def bands_page(request, genre):
    find = MusicGenre.objects.get(genre_name=genre).pk
    data = MusicBand.objects.filter(genre=find)
    return render(request, 'library/index_bands.html', {'data': data})


def band_info_page(request, genre, slug):
    find = MusicGenre.objects.get(genre_name=genre).pk
    data = MusicBand.objects.filter(genre=find).get(slug=slug)
    return render(request, 'library/index_info.html', {'data': data})

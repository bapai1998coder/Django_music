from django.http import Http404
from django.http import HttpResponse
from .models import Album,Song
from django.shortcuts import render,get_object_or_404
from django.template import loader


def index(request) :

    all_albums=Album.objects.all()


    return render(request, 'music/index.html', {'all_albums': all_albums})


def detail(request, album_id):

    album=get_object_or_404(Album, pk=album_id)

    return render(request, 'music/detail.html', {'album': album})

def favorite(request,album_id):
    album=get_object_or_404(Album,pk=album_id)

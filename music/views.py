from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Album

# Create your views her
#
# e.

def index(request) :
    all_album = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        "all_album" : all_album,
    }
    return HttpResponse(template.render(context, request))


    # html = ''
    # all_album = Album.objects.all()
    # for album in all_album:
    #     url = '/music/' + str(album.id) + '/'
    #     html += '<a href = "' + url +  '">' + album.title + '</a><br>'
    # return HttpResponse(html)

    # return HttpResponse("<h1> Hello world of music! </hi>")

def detail(request, album_id) :
    return HttpResponse("<h2> Details for album " + str(album_id) + " </h2>")

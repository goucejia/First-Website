from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.template import loader
from django.http import HttpResponse
from .models import Album, Song
from django.http import Http404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from .forms import UserForm

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_album'

    def get_queryset(self):
        return Album.objects.all()

# def index(request) :
#     all_album = Album.objects.all()
#     template = loader.get_template('music/index.html')
#     context = {
#         "all_album" : all_album,
#     }
#     return HttpResponse(template.render(context, request))
#     # return render(request, 'music/index.html', context)



class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

# def detail(request, album_id) :
#     # try:
#     #     album = Album.objects.get(pk = album_id)
#     # except Album.DoesNotExist:
#     #     raise Http404("Album Does Not Exist")
#
#     album = get_object_or_404(Album, pk=album_id)
#     return render(request, 'music/detail.html', {'album' : album})



def favorite(request, album_id):
    album = get_object_or_404(Album, pk = album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST["song"])
    except(KeyError, Song.DoesNotExist):
        return (request, 'music/detail.html'), {
            'album' : album,
            "error_msg" : "Song not valid",
        }
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'title', 'genre', 'album_logo']

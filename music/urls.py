# from django.urls import path, re_path
from django.conf.urls import url
from . import views

app_name = "music"

urlpatterns = [
    # http://127.0.0.1:8000/music/
    url(r'^$', views.IndexView.as_view(), name="index"), # based home page
    # url(r'^$', views.index, name="index"), # based home page

    # http://127.0.0.1:8000/music/<album_id> 
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = "display_album"),
    # url(r'^(?P<album_id>[0-9]+)/$', views.detail, name = "display_album"),

    # http://127.0.0.1:8000/music/<album_id>/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite$', views.favorite, name = "favorite"),

    # music/album/add
    url(r'album/add/$', views.AlbumCreate.as_view, name = 'album_add'),


]
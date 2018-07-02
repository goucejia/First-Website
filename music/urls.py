# from django.urls import path, re_path
from django.conf.urls import url
from . import views

app_name = "music"

urlpatterns = [
    # http://127.0.0.1:8000/music/
    url(r'^$', views.index, name="index"), # based home page

    # http://127.0.0.1:8000/music/<album_id>
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name = "display_album"),

    # http://127.0.0.1:8000/music/<album_id>/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite$', views.favorite, name = "favorite"),

    # # http://127.0.0.1:8000/music/<album_id>/unfavorite
    # url(r'^(?P<album_id>[0-9]+)/unfavorite$', views.unfavorite, name = "unfavorite"),

]
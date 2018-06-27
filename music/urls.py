from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/music/
    path('', views.index, name="index"), # based home page

    # http://127.0.0.1:8000/music/123x(id of Album / Music)
    re_path(r'^(?P<album_id>[0-9]+)/$', views.detail, name = "detail"),

]
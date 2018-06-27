from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index")  # base      http://127.0.0.1:8000/music/music/
]
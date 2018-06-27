from django.shortcuts import render
from django.http import HttpResponse

# Create your views her
#
# e.

def index(request) :
    return HttpResponse("<h1> Hello world of music! </hi>")

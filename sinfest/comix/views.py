from django.shortcuts import render
from . models import Comix

def index(request):
    comix = 
from django.shortcuts import render
from . models import Comix

def index(request):
    comix = Comix.objects.all()
    context = {
        'comix': comix,
        'title': 'Главная',
    }
    return render(request, template_name='comix/index.html', context=context)
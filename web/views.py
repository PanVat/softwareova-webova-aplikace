from django.shortcuts import render
from .models import Software, Verze


def index(request):
    context = {
        'software': Software.objects.all(),
        'verze': Verze.objects.all(),
    }
    return render(request, 'index.html', context)

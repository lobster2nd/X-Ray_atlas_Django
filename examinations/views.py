from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *


def index(request):
    return render(request, 'examinations/index.html', {'title': 'Главная страница'})


def body_part(request, part):
    return render(request, f'examinations/{part}.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
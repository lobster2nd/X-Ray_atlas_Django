from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *


def index(request):
    exams = Examinations.objects.all()
    cats = Category.objects.all()

    context = {
        'title': 'Главная страница',
        'exams': exams,
        'cats': cats
    }
    return render(request, 'examinations/index.html', context=context)


def show_exam(request, exam_id):
    return HttpResponse(f'{exam_id}')


def show_category(request, cat_id):
    exams = Examinations.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(exams) == 0:
        raise Http404()

    context = {
        'title': 'Категория',
        'exams': exams,
        'cats': cats,
    }
    return render(request, 'examinations/index.html', context=context)



def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
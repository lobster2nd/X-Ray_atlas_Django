from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from .models import *

menu = ['Главная', 'Открыть атлас', 'Добавить статью', 'Обратная связь', 'Войти']

def index(request):
    exams = Examinations.objects.all()
    cats = Category.objects.all()

    context = {
        'menu': menu,
        'title': 'Главная страница',
        'exams': exams,
        'cats': cats
    }
    return render(request, 'examinations/index.html', context=context)


def show_exam(request, exam_slug):
    exam =get_object_or_404(Examinations, slug=exam_slug)
    cats = Category.objects.all()

    context = {
        'menu': menu,
        'title': exam.title,
        'exam': exam,
        'cats': cats,
    }

    return render(request, 'examinations/exam.html', context=context)


def show_category(request, cat_slug):
    cat = Category.objects.filter(slug=cat_slug)
    exams = Examinations.objects.filter(cat_id=cat[0].id)
    cats = Category.objects.all()

    if len(exams) == 0:
        raise Http404()

    context = {
        'menu': menu,
        'title': cat_slug,
        'exams': exams,
        'cats': cats,
    }
    return render(request, 'examinations/index.html', context=context)



def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
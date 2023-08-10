from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .forms import AddExamForm

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'Открыть атлас', 'url_name': 'atlas'},
        {'title': 'Добавить статью', 'url_name': 'addpage'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
    ]


class ExaminationsHome(ListView):
    model = Examinations
    template_name = 'examinations/index.html'
    context_object_name = 'exams'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cats'] = Category.objects.all()
        return context

    def get_queryset(self):
        return Examinations.objects.filter(is_published=True)


class ShowExam(DetailView):
    model = Examinations
    template_name = 'examinations/exam.html'
    slug_url_kwarg = 'exam_slug'
    context_object_name = 'exam'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['exam']
        context['cats'] = Category.objects.all()
        return context


class ExaminationsCategory(ListView):
    model = Examinations
    template_name = 'examinations/index.html'
    context_object_name = 'exams'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = str(context['exams'][0].cat)
        context['cats'] = Category.objects.all()
        return context

    def get_queryset(self):
        return Examinations.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


class AddPage(CreateView):
    form_class = AddExamForm
    template_name = 'examinations/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        context['menu'] = menu
        context['title'] = 'Добавление исследования'
        return context


def atlas(request):
    return HttpResponse("page for atlas")


def contact(request):
    return HttpResponse("page for contact")


def login(request):
    return HttpResponse("page for login")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")



from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from .models import *
from .forms import AddExamForm
from .utils import *


class ExaminationsHome(DataMixin, ListView):
    model = Examinations
    template_name = 'examinations/index.html'
    context_object_name = 'exams'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Examinations.objects.filter(is_published=True)


class ShowExam(DataMixin, DetailView):
    model = Examinations
    template_name = 'examinations/exam.html'
    slug_url_kwarg = 'exam_slug'
    context_object_name = 'exam'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['exam'])
        return dict(list(context.items()) + list(c_def.items()))


class ExaminationsCategory(DataMixin, ListView):
    model = Examinations
    template_name = 'examinations/index.html'
    context_object_name = 'exams'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=str(context['exams'][0].cat))
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Examinations.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddExamForm
    template_name = 'examinations/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление исследования')
        return dict(list(context.items()) + list(c_def.items()))


def atlas(request):
    return HttpResponse("page for atlas")


def contact(request):
    return HttpResponse("page for contact")


def login(request):
    return HttpResponse("page for login")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")



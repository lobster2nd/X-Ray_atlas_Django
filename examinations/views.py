from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .forms import AddExamForm

menu = [{'title': 'Главная', 'url_name': ''},
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


def addpage(request):
    if request.method == 'POST':
        form = AddExamForm(request.POST)
        if form.is_valid():
            try:
                Examinations.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления исследования')

    else:
        form = AddExamForm()
    return render(request, 'examinations/addpage.html', {'form': form})


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

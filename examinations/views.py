from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse("<h1>Атлас укладок при рентгенологических исследованиях</h1>")


def head(request):
    return HttpResponse(f"Голова  {id}")


def spine(request):
    return HttpResponse("Позвоночник")


def upper_limp(request):
    return HttpResponse("Пояс верхней конечности")


def lower_limp(response):
    return HttpResponse("Пояс нижней конечности")


def other(response):
    return HttpResponse("Другие неконтрастные методы исследования")


#def skullPA(request, id):
#    return HttpResponse(f"{id}")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return HttpResponse("Страница приложения Candle")


def info(request):
    return HttpResponse("<h1>Страница общей информации</h1>")


def reviews(request, idr):
    if request.GET:
        print(request.GET)

    return HttpResponse(f'Отзыв номер {idr}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

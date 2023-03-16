from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import Candle

menu = ["ИНФО", "О НАС", "ДОСТАВКА", "ОТЗЫВЫ", "ВОЙТИ"]


def index(request):
    posts = Candle.objects.all()
    return render(request, 'candle/index.html', {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    })


def info(request):
    return render(request, 'candle/info.html', {'menu': menu, 'title': 'О сайте'})


def reviews(request, idr):
    if request.GET:
        print(request.GET)

    return HttpResponse(f'Отзыв номер {idr}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

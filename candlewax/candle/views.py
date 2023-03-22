from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

from .models import Candle, Info, About, Delivery, Reviews, Category

menu = [
    {'title': 'ИНФО', 'url_name': 'info'},
    {'title': 'О НАС', 'url_name': 'about'},
    {'title': 'ДОСТАВКА', 'url_name': 'delivery'},
    {'title': 'ОТЗЫВЫ', 'url_name': 'reviews'},
    {'title': 'ВОЙТИ', 'url_name': 'login'},
]

def index(request):
    posts = Candle.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }

    return render(request, 'candle/index.html', context=context)


def info(request):
    posts = Info.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'candle/info.html', context=context)


def about(request):
    posts = About.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'candle/about.html', context=context)

def delivery(request):
    posts = Delivery.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'candle/delivery.html', context=context)


def reviews(request):
    posts = Reviews.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'candle/reviews.html', context=context)


def login(request):
    return HttpResponse('Авторизация')


def show_buy(request, buy_id):
    return HttpResponse(f'Отображение корзины с id = {buy_id}')




def show_catalog(request, cat_id):
    posts = Candle.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по каталогу',
        'cat_selected': cat_id,
    }

    return render(request, 'candle/index.html', context=context)



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

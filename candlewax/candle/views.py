from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import *
from .models import Candle, Info, About, Delivery, Reviews, Category


def index(request):
    posts = Candle.objects.all()
    context = {
        'posts': posts,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'candle/index.html', context=context)


def info(request):
    posts = Info.objects.all()
    context = {
        'posts': posts,
        'title': 'Главная страница'
    }
    return render(request, 'candle/info.html', context=context)


def about(request):
    posts = About.objects.all()
    context = {
        'posts': posts,
        'title': 'Главная страница'
    }
    return render(request, 'candle/about.html', context=context)


def delivery(request):
    posts = Delivery.objects.all()
    context = {
        'posts': posts,
        'title': 'Отзывы'
    }
    return render(request, 'candle/delivery.html', context=context)


def reviews(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = AddPostForm()

    posts = Reviews.objects.all()
    context = {
        'form': form,
        'posts': posts,
        'title': 'Отзывы и предложения'
    }
    return render(request, 'candle/reviews.html', context=context)


def login(request):
    return HttpResponse('Авторизация')


def show_buy(request, buy_id):
    return HttpResponse(f'Отображение корзины с id = {buy_id}')


def show_product(request, prod_slug):
    post = get_object_or_404(Candle, slug=prod_slug)

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id
    }

    return render(request, 'candle/post.html', context=context)


def show_catalog(request, cat_slug):
    # cat = Category.objects.get(slug=cat_slug)
    posts = Candle.objects.filter(cat__slug=cat_slug)

    print(len(posts))
    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'title': 'Отображение по каталогу',
        'cat_selected': cat_slug,
    }

    return render(request, 'candle/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

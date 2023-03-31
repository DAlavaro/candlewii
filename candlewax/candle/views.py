from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView

from .forms import *
from .models import *

# класс главной страницы index.html
class CandleHome(ListView):
    model = Candle
    template_name = 'candle/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    # Функция для отображения только опубликованных записей на главной странице
    def get_queryset(self):
        return Candle.objects.filter(is_published=True)

# Функция главной страницы
# def index(request):
#     posts = Candle.objects.all()
#     context = {
#         'posts': posts,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#     return render(request, 'candle/index.html', context=context)

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




# Class для добавления нового отзыва
# class AddReviews(CreateView):
#     form_class = AddPostForm
#     template_name = 'candle/reviews.html'
#     context_object_name = 'posts'
#     success_url = reverse_lazy('home')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Отзывы и предложения'
#         return context

# Функция для добавления нового отзыва
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


class ShowPost(DeleteView):
    model = Candle
    template_name = 'candle/post.html'
    slug_url_kwarg = 'prod_slug'
    #pk_url_kward = 'pk'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        return context



# Функция для отображения информации по товару
# def show_product(request, prod_slug):
#     post = get_object_or_404(Candle, slug=prod_slug)
#
#     context = {
#         'post': post,
#         'title': post.title,
#         'cat_selected': post.cat_id
#     }
#
#     return render(request, 'candle/post.html', context=context)

# Class отображения списка по категориям
class CandleCatalog(ListView):
    model = Candle
    template_name = 'candle/index.html'
    context_object_name = 'posts'
    allow_empty = False

    # Функция для отображения выбранных и опубликованных записей
    def get_queryset(self):
        return Candle.objects.filter(cat__slug=self.kwargs['cat_slug'],
                                     is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория -' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context

# Функция отображения списка по категориям
# def show_catalog(request, cat_slug):
#     # cat = Category.objects.get(slug=cat_slug)
#     posts = Candle.objects.filter(cat__slug=cat_slug)
#
#     print(len(posts))
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'title': 'Отображение по каталогу',
#         'cat_selected': cat_slug,
#     }
#
#     return render(request, 'candle/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

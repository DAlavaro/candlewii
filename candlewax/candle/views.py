from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .utils import *

from .forms import *
from .models import *

# класс главной страницы index.html
class CandleHome(DataMixin, ListView):
    model = Candle
    template_name = 'candle/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    # Функция для отображения только опубликованных записей на главной странице
    def get_queryset(self):
        return Candle.objects.filter(is_published=True)


# класс страницы info.html
class CandleInfo(ListView):
    model = Info
    template_name = 'candle/info.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Информация'
        return context


# класс страницы about.html
class CandleAbout(ListView):
    model = About
    template_name = 'candle/about.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О нас'
        return context


class CandleDelivery(ListView):
    model = Delivery
    template_name = 'candle/delivery.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Доставка'
        return context


# Функция для добавления нового отзыва
# @login_required
# def reviews(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#
#     else:
#         form = AddPostForm()
#
#     posts = Reviews.objects.all()
#     context = {
#         'form': form,
#         'posts': posts,
#         'title': 'Отзывы и предложения'
#     }
#     return render(request, 'candle/reviews.html', context=context)


# Class для добавления нового отзыва
class AddReviews(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'candle/reviews.html'
    success_url = reverse_lazy('home')
    #login_url = reverse_lazy('home')
    raise_exception = True


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))

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
class CandleCatalog(DataMixin, ListView):
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
        c_def = self.get_user_context(
            title='Категория -' + str(context['posts'][0].cat),
            cat_selected=context['posts'][0].cat_id
        )
        return dict(list(context.items()) + list(c_def.items()))


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('info/', info, name='info'),
    path('about/', about, name='about'),
    path('delivery/', delivery, name='delivery'),
    path('reviews/', reviews, name='reviews'),
    path('login/', login, name='login'),
    path('buy/<int:buy_id>/', show_buy, name='buy'),
    path('catalog/<slug:cat_slug>', show_catalog, name='catalog'),
    path('product/<slug:prod_slug>', show_product, name='product'),
]